from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.TextField()
