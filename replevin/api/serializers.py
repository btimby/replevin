from rest_framework import serializers

from main.models import SSHKey, AWSKey, Server, Cron, S3Destination, \
                        LocalDestination, RemoteDestination, FullBackup, \
                        IncrementalBackup, DumpBackup, Restore, Database, \
                        BackupResult, RestoreResult, DestinationFile


class SSHKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SSHKey
        fields = '__all__'


class AWSKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AWSKey
        fields = '__all__'


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class CronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cron
        fields = '__all__'


class S3DestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = S3Destination
        fields = '__all__'


class LocalDestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalDestination
        fields = '__all__'


class RemoteDestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemoteDestination
        fields = '__all__'


class DestinationFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DestinationFile
        fields = '__all__'


class FullBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullBackup
        fields = '__all__'


class IncrementalBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IncrementalBackup
        fields = '__all__'


class DumpBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DumpBackup
        fields = '__all__'


class RestoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restore
        fields = '__all__'


class DatabaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'


class BackupResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BackupResult
        fields = '__all__'


class RestoreResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestoreResult
        fields = '__all__'
