from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# DATABASES = {
#     'default': {
#         'ENGINE': django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default: dj_database_url.parse('os.environ.get("DATABASE_URL")')'
}