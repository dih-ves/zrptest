DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = '89d98sj[jsnkh&56|611cz/bsppetnkc]a31]ske'

SECRET_KEY = 's&21d5f4z#&/!xv5n/48t8s3q1&1a'