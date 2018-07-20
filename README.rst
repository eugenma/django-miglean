django-miglean
==============

Django development utility command to remove the existing migrations. 

During development of an application the database schema changes in the beginning quite frequently. There remains a lot of migration files over multiple modules.

This tools helps to clean the migrations by doing the following steps

- Delete all migration inside each app of the project which uses this command.
- Delete the migrations in the database by utilizing the undocumented model `django.db.migrations.recorder.MigrationRecorder.Migration`.
- Recreate migrations as new by running `manage.py makemigrations` and `manage.py migrate`


Warning
---------

Do NOT use this tool in production. It is not well tested and unclear how it behave in any sitation. You may loose all your data.


Usage
-----

Run as `manage.py` command via::

   (venv)$ python manage.py clean_migrations --dry-run False

or via `pipenv`::

   $ pipenv run python manage.py clean_migrations --dry-run False

The argument `--dry-run` is optional. With default value `True`. In this case
the cleanup is not executed. Instead one see which actions will be executed if
the flag is `False`.

Installation
------------

1. Install from github with `pip` or `pipenv`::
   
   $ pip install git+https://github.com/tangentlabs/django-oscar-paypal.git


2. Add into your `settings.py` under::

   INSTALLED_APPS = [
      # ...
      'migclean',
   ]


Requirements
^^^^^^^^^^^^

Tested with `Django===1.11`.


Authors
-------

`django-miglean` was written by `Eugen Massini <eugen.massini@gmail.com>`_.
