from typing import Sequence, Iterator
from collections import namedtuple
import os
import shutil
import sys

from django.core.management import BaseCommand, call_command
from django.conf import settings
from django.db.migrations.recorder import MigrationRecorder
from django.apps import apps


AppContent = namedtuple('AppContent', ['app', 'content', ])

MIGRATIONS_DIRNAME = "migrations"


class Command(BaseCommand):
    help = 'Cleans all migration files. Just for testing environments. Do not use in production.'

    def add_arguments(self, parser):
        parser.add_argument('--no-dry-run', dest='dry_run', action='store_false', help='The real execution (Default is dry run.)')
        parser.set_defaults(dry_run=True)


    def handle(self, *args, **options):
        self.dry_run = options['dry_run']

        self.stdout.write(f"Clean migrations in project directory '{settings.BASE_DIR}'.")

        self.delete_files()
        self.delete_records()

        self.execute_command('makemigrations')
        self.execute_command('migrate', '--fake')

    def delete_files(self):
        def filter_init(ac):
            return filter(lambda c: c != "__init__.py", ac)

        def from_path(app):
            content = os.listdir(self.get_migration_path(app))
            return AppContent(app, list(filter_init(content)))

        projects_with_migrations = filter(lambda p: os.path.isdir(self.get_migration_path(p)), apps.app_configs)
        projects_with_content = map(from_path, projects_with_migrations)
        projects_with_non_empty_content = filter(lambda ac: any(ac.content), projects_with_content)

        for app in projects_with_non_empty_content:
            self.stdout.write(f"Clean '{os.path.join(app.app, MIGRATIONS_DIRNAME)}':")
            for migration_content in app.content:
                self.delete_file_or_dir(app.app, migration_content)

    def delete_file_or_dir(self, app, content):
        path = self.get_migration_path(app)
        path = os.path.join(path, content)

        def apply_delete(method, name):
            if self.dry_run:
                self.stdout.write(f"\tdelete {name} '{content}'")
            else:
                method(path)

        if os.path.isfile(path):
            apply_delete(os.remove, "file")

        if os.path.isdir(path):
            apply_delete(shutil.rmtree, "directory")

    def delete_records(self):
        if self.dry_run:
            records = MigrationRecorder.Migration.objects.values_list('app', flat=True).distinct()
            self.stdout.write(f"Delete Migration records:")
            self.stdout.write(f"\t{list(records)}")
        else:
            MigrationRecorder.Migration.objects.all().delete()

    def execute_command(self, *commands: str) -> None:
        print(f"Execute command: python manage.py {' '.join(commands)}")
        if not self.dry_run:
            call_command(*commands)

    def get_migration_path(self, app: str):
        return os.path.join(settings.BASE_DIR, app, MIGRATIONS_DIRNAME)
