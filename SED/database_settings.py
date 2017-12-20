# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SED_Database',
        'MYSQL_USER': 'sed_admin',
        'USER': 'sed_admin',
        'PASSWORD':'sed_password',
        'MYSQL_PASSWORD':'sed_password2',
        'HOST': 'sed_database', #need to change to match container
        'PORT': '3306',
    }
}