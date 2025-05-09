"""
Django settings for grape project.
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spravgrape',
    'tinymce',

    'app',
    'sickpest',
    'preparats',
    'dung',
    'jornal',
    'record',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grape.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'grape.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 900,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': 'paste,autolink,lists,spellchecker,pagebreak,style,layer,table,save,advlink, image, media, link, emoticons, insertdatetime, preview, searchreplace, print, contextmenu, wordcount, fullscreen, horizontalrule,',
    'paste_as_text': False,
    'toolbar': 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat',
    # 'file_picker_callback': '''
    #     function(callback, value, meta) {
    #         window.open('/admin/filebrowser/browse/?pop=1', '_blank');
    #     }
    #     ''',
    'table_default_attributes': {
           'class': 'table',  # можно использовать классы Bootstrap
       },
       'table_default_styles': {
           'width': '100%',
           'border': '1px solid #ddd',
           'border-collapse': 'collapse',
       },
    'file_browser_callback': 'mce_filebrowser',
}
       # 'content_css': '/static/app/css/style_app.css',  # путь к вашему CSS
FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

# X_FRAME_OPTIONS = 'SAMEORIGIN'

FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp'],
    'Document': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.txt'],
    'Video': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav'],
}
FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/files/'
MEDIA_ROOT = BASE_DIR / 'files'


try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
