"""
WSGI config for root project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


path = "/home/fazliddin1234/AgroCom.root"

if path not in sys.path:
    sys.path.append(path)

venv_path = "/home/fazliddin1234/AgroCom/venv/bin"
activate_this = "/home/fazliddin1234/AgroCom/venv/bin/activate_this.py"

if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), dict(__file__=activate_this))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

application = get_wsgi_application()
