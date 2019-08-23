from django.db import models


class CreatedModifiedMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class SSHKey(CreatedModifiedMixin):
    name = models.CharField(max_length=128)
    private_key = models.TextField()
    username = models.CharField(max_length=128)


class AWSKey(CreatedModifiedMixin):
    aws_access_key_id = models.TextField()
    aws_secret_access_key = models.TextField()


class Server(CreatedModifiedMixin):
    name = models.CharField(max_length=64)
    host = models.GenericIPAddressField()
    port = models.PositiveSmallIntegerField()
    ssh_key = models.ForeignKey(SSHKey, on_delete=models.PROTECT)
    mysql_user = models.CharField(max_length=64)
    mysql_pass = models.CharField(max_length=64)


class Cron(CreatedModifiedMixin):
    name = models.CharField(max_length=128)
    minute = models.CharField(max_length=32)
    hour = models.CharField(max_length=32)
    day_of_week = models.CharField(max_length=32)
    day_of_month = models.CharField(max_length=32)
    month_of_year = models.CharField(max_length=32)


class Destination(CreatedModifiedMixin):
    name = models.CharField(max_length=128)


class S3Destination(Destination):
    destination = models.OneToOneField(
        Destination, related_name='s3', parent_link=True,
        on_delete=models.CASCADE)
    aws_key = models.ForeignKey(AWSKey, on_delete=models.PROTECT)
    s3_bucket_name = models.CharField(max_length=128)


class LocalDestination(Destination):
    destination = models.OneToOneField(
        Destination, related_name='local', parent_link=True,
        on_delete=models.CASCADE)
    path = models.TextField()


class RemoteDestination(Destination):
    destination = models.OneToOneField(
        Destination, related_name='remote', parent_link=True,
        on_delete=models.CASCADE)
    host = models.CharField(max_length=128)
    ssk_key = models.ForeignKey(SSHKey, on_delete=models.PROTECT)
    path = models.TextField()


class DestinationFile(CreatedModifiedMixin):
    destination = models.ForeignKey(Destination, on_delete=models.PROTECT)
    identifier = models.CharField(max_length=128)


class Backup(CreatedModifiedMixin):
    name = models.CharField(max_length=128)
    cron = models.ForeignKey(Cron, on_delete=models.PROTECT)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.PROTECT)


class FullBackup(Backup):
    backup = models.OneToOneField(
        Backup, related_name='full', parent_link=True,
        on_delete=models.CASCADE)


class IncrementalBackup(Backup):
    backup = models.OneToOneField(
        Backup, related_name='incremental', parent_link=True,
        on_delete=models.CASCADE)
    base = models.ForeignKey(
        FullBackup, related_name='increments', on_delete=models.CASCADE,
        help_text='The full backup that this increment extends')


class DumpBackup(Backup):
    GZIP_NONE = 0
    GZIP_SERVER = 1
    GZIP_CLIENT = 2

    GZIP_NAMES = {
        GZIP_NONE: 'Do not compress backup',
        GZIP_SERVER: 'Gzip on the server (less data transferred)',
        GZIP_CLIENT: 'Gzip on the client (less server CPU / RAM)',
    }

    backup = models.OneToOneField(
        Backup, related_name='dump', parent_link=True,
        on_delete=models.CASCADE)
    gzip = models.PositiveSmallIntegerField(
        choices=list(GZIP_NAMES.items()), help_text='How to compress dump')
    single_transaction = models.BooleanField(
        default=True, help_text='Use transaction to avoid locking')
    grants = models.BooleanField(
        default=True, help_text='Dump grants to portable format, no need to '
        'backup mysql database')
    routines = models.BooleanField(
        default=True, help_text='Backup stored procedures and functions')


class Restore(CreatedModifiedMixin):
    backup = models.ForeignKey(
        Backup, on_delete=models.PROTECT, help_text='The backup to restore')
    server = models.ForeignKey(
        Server, on_delete=models.PROTECT, help_text='The server to restore to')
    cron = models.ForeignKey(
        Cron, on_delete=models.PROTECT, help_text='How often to test restore')


class Database(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(Backup, related_name='databases')
    name = models.CharField(max_length=128)


class Result(models.Model):
    class Meta:
        abstract = True

    started = models.DateTimeField(null=False)
    finished = models.DateTimeField(null=False)
    bytes = models.PositiveIntegerField()
    table_count = models.PositiveIntegerField()
    row_count = models.PositiveIntegerField()
    routine_count = models.PositiveIntegerField()
    log = models.FileField()


class BackupResult(Result):
    backup = models.ForeignKey(Backup, on_delete=models.CASCADE)
    destination_file = models.ForeignKey(
        DestinationFile, on_delete=models.PROTECT)


class RestoreResult(Result):
    restore = models.ForeignKey(Restore, on_delete=models.CASCADE)
