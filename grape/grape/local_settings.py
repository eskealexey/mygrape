import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_lvf@_rnl3-e)x#a^6vd5&ru+s!wp19m+#-pq=l-qdl=n)ldi)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'mygrape' ,
        'USER': 'root',
        'PASSWORD': 'Passw0rD' ,
        'HOST': '172.17.0.2',
        # 'PORT': '3306',

    }
}


STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR]
