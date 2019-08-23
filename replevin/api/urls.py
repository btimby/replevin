from django.urls import include, path

from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register('ssh_keys', views.SSHKeyViewSet)
router.register('aws_keys', views.AWSKeyViewSet)
router.register('servers', views.ServerViewSet)
router.register('crons', views.CronViewSet)
router.register('s3destinations', views.S3DestinationViewSet)
router.register('localdestinations', views.LocalDestinationViewSet)
router.register('remotedestinations', views.RemoteDestinationViewSet)
router.register('destinationfiles', views.DestinationFileViewSet)
router.register('fullbackups', views.FullBackupViewSet)
router.register('incrementalbackups', views.IncrementalBackupViewSet)
router.register('dumpbackups', views.DumpBackupViewSet)
router.register('restores', views.RestoreViewSet)
router.register('databases', views.DatabaseViewSet)
router.register('backupresults', views.BackupResultViewSet)
router.register('restoreresults', views.RestoreResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
