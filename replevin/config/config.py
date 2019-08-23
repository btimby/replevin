import os

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from django.core.cache import cache
from django.conf import settings

from .models import Field


def _make_cache_key(name):
    return 'config:%s' % name


def _validate(name):
    if name not in settings.CONFIG:
        raise AttributeError('Invalid config field %s' % name)


@receiver(post_delete, sender=Field)
@receiver(post_save, sender=Field)
def _evict_value(sender, instance, **kwargs):
    cache.delete(_make_cache_key(instance.name))


@receiver(pre_save, sender=Field)
def _validate_pre_save(sender, instance, **kwargs):
    _validate(instance.name)


class Config(object):
    def __getattr__(self, name):
        _validate(name)

        cast = settings.CONFIG[name][0]
        cache_key = _make_cache_key(name)

        value = os.environ.get(name)
        if value is not None:
            return cast(value)

        value = cache.get(cache_key)
        if value is not None:
            return value

        try:
            value = cast(Field.objects.get(name=name).value)
            cache.set(cache_key, value)
            return value
        except Field.DoesNotExist:
            pass

        return settings.CONFIG[name][1]

    def __setattr__(self, name, value):
        try:
            field = Field.objects.get(name=name)
        except Field.DoesNotExist:
            field = Field()
        field.value = str(value)
        field.save()

        cache.set(_make_cache_key(name), value)


config = Config()
