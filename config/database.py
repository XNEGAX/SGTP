import os
DB_HOST = os.environ.get("db_host")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'AaUUUUUUUU',
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}
