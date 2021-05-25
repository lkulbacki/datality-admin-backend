# datality-admin-backend

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

# Prerequisites

- Project built and tested with python 3.9.4

Future plans: migration to Docker

# Development environment setup
`pyenv install 3.9.4`
`pyenv virtualenv 3.9.4 datality-admin`
`pyenv local 3.9.4/envs/datality-admin`
`pip install --upgrade pip`
`pip install -r requirements.txt`

You may need to configure connection to postgresql and creation of appropriate .env file inside main folder,
consisting of following constants:
`SECRET_KEY` - Django secret key
`POSTGRESQL_CONNECTION_STRING_ADMIN_USERS`, `POSTGRESQL_CONNECTION_STRING_PRODUCTS`, `POSTGRESQL_CONNECTION_STRING_OFFERS`

Hint: due to historical reasons, project uses and operates between three different databases. The connection string above
should represent them.

Once databases are configured, you can proceed with migrations:
`python manage.py migrate`

# To start development server locally
`python manage.py runserver`
