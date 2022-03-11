# PY Django Project Starter Template

*** It is still in progress ***

*** This project will be updated for each Django version. And there will be branches available representing the Django version. However, continues developement of the project will not be reflected to backwards. The latest version will have the most features and the less bugs, hopefully.***

Django Project Starter Template is a short cut for you to start a project easily and quicker without the effort of seperating settings files for prod and dev, creating an Env() for secret data, and so on. I have tried to use best django 3rd party applications as dependencies.

## How?
1. Rename .env-dist to .env
2. Generate a secret key on https://djecrety.ir/ and write it on .env file e.g. SECRET_KEY=your-top-secret-key-here
3. install requirements.txt into your environment
4. ./manage.py migrate
5. to start an app
    `mkdir apps/my_app && ./manage.py startapp my_app apps/my_app`
6. apps should be written as such: `apps.your_app` in apps.py and in settings->INSTALLED_APPS
7. You are good to start your project.

8. For production:
Change the line within manage.py file from `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')` to `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')` for productions environment. from `config.settings.dev` to `config.settings.prod`  

## What is it?
* The config app is the hearth of this django starter project template. Project wide settings, urls, wsgi and asgi files are within the config app.
    * Settings and urls files are seperated into three files: base, dev and prod. This is done in order to seperate the development and production environments as much as possible. e.g. base+dev is for development environment.
* All other apps are within apps folder.
    * Customizable User model
* The assets folder is for templates and staticfiles (files before collectstatic command is executed).
* The static folder is for the static files of the production environment.
* The media folder is for user uploaded files, images and etc.

## Dependencies
### Accounts Management
    - django-allauth
    - custom User model

### Debugging
    - Django Extensions
    - Django Debug Toolbar
    - iPython
    - ipdb

### Environment for sensitive settings data
    - Django Environ

### Logging
    - Sentry SDK

### REST API Creation and Usage
    - Django Rest Framework
    - requests

### Code Formatting
    - Black

### Others
    - Unidecode

### Tested Python version
    - Python 3.10

### Django version
    - Django 4.0.3
