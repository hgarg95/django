import os
from django.conf import settings


DEBUG = False
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES = {'default': dj_database_url.config()}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



# import psycopg2
# import urlparse

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.d2phbs18hrpoqu,
#     user=url.gbupcyqzfdyeoz,
#     password=url.i_SMwtd-kkuBMMQ9pZ7YH3Bx0B ,
#     host=url.ec2-54-235-152-114.compute-1.amazonaws.com,
#     port=url.5432
# )

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500


ALLOWED_HOST = ['*']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )