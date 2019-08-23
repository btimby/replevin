# NOTE: This script expects to be run each hour.
# https://mariadb.com/kb/en/library/incremental-backup-and-restore-with-mariabackup/
# https://mariadb.com/kb/en/library/mariabackup-overview/#using-mariabackup

import os
from os.path import join as pathjoin


RETAIN_DAYS = 10
FULL_INTERVAL = 24

# TODO: load from file or use mariadb-backup config.
USERNAME = ''
PASSWORD = ''


def should_full_backup(dbname, dir):
    '''
    Determine if a full backup is necessary.

    If the last full backup is older than FULL_INTERVAL - 1 hours then a full
    backup is necessary.
    '''
    pass


def shift_backups(dbname, dir):
    '''
    Rename old backup sets and prune any beyond RETAIN_DAYS old.
    '''
    pass


def incremental(dbname, dir):
    '''
    Perform an incremental backup against the most recent full backup.
    '''
    pass


def full(dbname, dir):
    '''
    Perform a full backup.
    '''
    pass


def backup(dbname, dir):
    '''
    mariabackup --backup \
        --target-dir=/foo
        --user=mariabackup --password=password
    '''
    if should_full_backup(dbname, dir):
        shift_backups(dbname, dir)

    if os.path.isdir(pathjoin(dir, 'full')):
        # Perform incremental backup.
        incremental(dbname, dir)

    else:
        # Perform full backup.
        full(dbname, dir)


def verify(dbname, dir, host):
    '''
    Use docker to restore backup.

    Optionally connect to remote host via SCP to issue commands.
    '''
    pass


def restore(dbname, dir, increment=None):
    '''
    Restore an (incremental) backup.

    If increment is omitted, the most recent is assumed. If increment is "none"
    then the full backup is restored.

    cp /foo /tmp/restore-foo
    mariabackup --prepare --target-dir=/tmp/restore-foo
    mariabackup --prepare --target-dir=/tmp/restore-foo \
                --incremental-dir=/foo/inc0
    ... inc1 and so on ...
    mariabackup --copy-back --target-dir=/tmp/restore-foo
    '''
    # NOTE since mariabackup mutates the base backup and we don't wish to
    # destroy it (possible future restores) we copy it first.
    pass


def main():
    pass


if __main__== '__main__':
    main()
