
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/simplicat/mysite/mysite/settings.py'
## and your manage.py is is at '/home/simplicat/mysite/manage.py'
path = '/home/manugomez95/TFG-ManuAlvaro/apiMotoGP/apiMotoGP'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiMotoGP.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()