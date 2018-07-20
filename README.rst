django-miglean
==============

Django development utility command to remove the existing migrations. 

During development of an application the database schema changes in the beginning quite frequently. There remains a lot of migration files over multiple modules.

This tools helps to clean the migrations by doing the following steps

- Delete all migration inside each app of the project which uses this command.
- Delete the migrations in the database by utilizing the undocumented model :code:`django.db.migrations.recorder.MigrationRecorder.Migration`.
- Recreate migrations as new by running :code:`manage.py makemigrations` and `manage.py migrate`


Warning
---------

Do NOT use this tool in production. It is not well tested and unclear how it behave in any sitation. You may loose all your data.


Usage
-----

Run as :code:`manage.py` command via::

   (venv)$ python manage.py clean_migrations --dry-run False

or via :code:`pipenv`::

   $ pipenv run python manage.py clean_migrations --dry-run False

The argument :code:`--dry-run` is optional. Default value is :code:`True`. In this case
the cleanup is not executed. Instead one see which actions will be executed if
the flag is :code:`False`.

Installation
------------

1. Install from github with :code:`pip` or :code:`pipenv` ::
   
    $ pip install git+https://github.com/eugenma/django-miglean.git


2. Add into your :code:`settings.py` under ::


    INSTALLED_APPS = [
       # ...
       'migclean',
    ]


Requirements
^^^^^^^^^^^^

Tested with :code:`Django===1.11`.


Authors
-------

:code:`django-miglean` was written by `Eugen Massini <eugen.massini@gmail.com>`_.
