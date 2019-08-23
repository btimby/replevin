from django.shortcuts import render

from rest_framework import viewsets

from main import models
from api import serializers


class SSHKeyViewSet(viewsets.ModelViewSet):
    queryset = models.SSHKey.objects.all()
    serializer_class = serializers.SSHKeySerializer


class AWSKeyViewSet(viewsets.ModelViewSet):
    queryset = models.AWSKey.objects.all()
    serializer_class = serializers.AWSKeySerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all()
    serializer_class = serializers.ServerSerializer


class CronViewSet(viewsets.ModelViewSet):
    queryset = models.Cron.objects.all()
    serializer_class = serializers.CronSerializer


class S3DestinationViewSet(viewsets.ModelViewSet):
    queryset = models.S3Destination.objects.all()
    serializer_class = serializers.S3DestinationSerializer


class LocalDestinationViewSet(viewsets.ModelViewSet):
    queryset = models.LocalDestination.objects.all()
    serializer_class = serializers.LocalDestinationSerializer


class RemoteDestinationViewSet(viewsets.ModelViewSet):
    queryset = models.RemoteDestination.objects.all()
    serializer_class = serializers.RemoteDestinationSerializer


class DestinationFileViewSet(viewsets.ModelViewSet):
    queryset = models.DestinationFile.objects.all()
    serializer_class = serializers.DestinationFileSerializer


class FullBackupViewSet(viewsets.ModelViewSet):
    queryset = models.FullBackup.objects.all()
    serializer_class = serializers.FullBackupSerializer


class IncrementalBackupViewSet(viewsets.ModelViewSet):
    queryset = models.IncrementalBackup.objects.all()
    serializer_class = serializers.IncrementalBackupSerializer


class DumpBackupViewSet(viewsets.ModelViewSet):
    queryset = models.DumpBackup.objects.all()
    serializer_class = serializers.DumpBackupSerializer


class RestoreViewSet(viewsets.ModelViewSet):
    queryset = models.Restore.objects.all()
    serializer_class = serializers.RestoreSerializer


class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = models.Database.objects.all()
    serializer_class = serializers.DatabaseSerializer


class BackupResultViewSet(viewsets.ModelViewSet):
    queryset = models.BackupResult.objects.all()
    serializer_class = serializers.BackupResultSerializer


class RestoreResultViewSet(viewsets.ModelViewSet):
    queryset = models.RestoreResult.objects.all()
    serializer_class = serializers.RestoreResultSerializer
