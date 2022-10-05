# Django settings for solimatt project.
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY', "s0m3_s3kr1t_k3y")

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", "True") == "True"

ALLOWED_HOSTS = ['solimatt.juntagrico.science', 'localhost', 'juntagrico.solimatt.ch', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'juntagrico',
    'impersonate',
    'adminsortable2',
    'crispy_forms',
    'solimatt',
    'polymorphic',
]

ROOT_URLCONF = 'solimatt.urls'

DATABASES = {
    'default': {
        #'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE', 'django.db.backends.postgresql'),
        #'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME', 'juntagrico'),
        #'USER': os.environ.get('JUNTAGRICO_DATABASE_USER', 'solila'),
        # ''junatagrico', # The following settings are not used with sqlite3:
        #'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD', 'solila'),  # ''junatagrico',
        #'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST', 'localhost'),
        # 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        #'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', '5432'),  # ''', # Set to empty string for default.
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'),
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','solimatt.db'),
        # 'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        # 'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        # 'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # 'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['solimatt/templates'],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': True
        },
    },
]

WSGI_APPLICATION = 'solimatt.wsgi.application'

LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS = ['%d.%m.%Y', ]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25'))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'True') == 'True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False') == 'True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

WHITELIST_EMAILS = []


def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/my/home"

"""
    Admin Settings
"""
ADMINS = [
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
    ('Juntagrico', os.environ.get('JUNTAGRICO_DS_EMAIL'))
]
MANAGERS = ADMINS

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
    Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

VOCABULARY = {
    'member': 'Mitglied',
    'member_pl': 'Mitglieder',
    'assignment': 'Arbeitseinsatz',
    'assignment_pl': 'Arbeitseinsätze',
    'share': 'Anteilschein',
    'share_pl': 'Anteilscheine',
    'subscription': 'Abo',
    'subscription_pl': 'Abos',
    'co_member': 'Mitabonnent',
    'co_member_pl': 'Mitabonnenten',
    'price': 'Betriebsbeitrag',
    'member_type': 'Mitglied',
    'member_type_pl': 'Mitglieder',
    'depot': 'Depot',
    'depot_pl': 'Depots'
}
ORGANISATION_NAME = "Solimatt"
ORGANISATION_NAME_CONFIG = {"type": "Verein",
                            "gender": "F"}
ORGANISATION_LONG_NAME = "Solimatt"
ORGANISATION_ADDRESS = {"name": "Solimatt",
                        "street": "Hof Baselmatt",
                        "number": "21",
                        "zip": "4435",
                        "city": "Niederdorf"}
ORGANISATION_PHONE = ''
ORGANISATION_BANK_CONNECTION = {"PC": "0",
                                "IBAN": "CH93 0839 2000 1595 7030 1",
                                "BIC": "",
                                "NAME": "Freie Gemeinschaftsbank, Genossenschaft, Meret Oppenheim-Strasse 10, 4002 Basel",
                                "ESR": ""}
INFO_EMAIL = "juntagrico@solimatt.ch"
SERVER_URL = "solimatt.ch"
BUSINESS_REGULATIONS = ""
BYLAWS = "https://solila.ch/wordpress/wp-content/uploads/2020/10/Statuten_SoliLa_Genossenschaft.pdf"
MAIL_TEMPLATE = "mails/email.html"
STYLES = {'static': ['css/solimatt.css']}
FAVICON = "/static/juntagrico/img/favicono.ico"
FAQ_DOC = ""
EXTRA_SUB_INFO = ""
ACTIVITY_AREA_INFO = ""
SHARE_PRICE = "200"
ENABLE_SHARES = True
BASE_FEE = ""
CURRENCY = "CHF"
ASSIGNMENT_UNIT = "ENTITY"
PROMOTED_JOB_TYPES = []
PROMOTED_JOBS_AMOUNT = 2
DEPOT_LIST_GENERATION_DAYS = [1, 2, 3, 4, 5, 6, 7]
BILLING = False
BUSINESS_YEAR_START = {"day": 1, "month": 1}
BUSINESS_YEAR_CANCELATION_MONTH = 10
MEMBERSHIP_END_MONTH = 6
IMAGES = {'status_100': '/static/juntagrico/img/status_100.png',
          'status_75': '/static/juntagrico/img/status_75.png',
          'status_50': '/static/juntagrico/img/status_50.png',
          'status_25': '/static/juntagrico/img/status_25.png',
          'status_0': '/static/juntagrico/img/status_0.png',
          'single_full': '/static/juntagrico/img/single_full.png',
          'single_empty': '/static/juntagrico/img/single_empty.png',
          'single_core': '/static/juntagrico/img/single_core.png',
          'core': '/static/juntagrico/img/core.png'}
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
