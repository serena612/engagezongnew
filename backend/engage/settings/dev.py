import os

from .base import *

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '172.19.224.1', 'dev.engageplaywin.com', '192.168.153.143', 'engage.devapp.co','cms.engage.devapp.co']



GAME_CLIENTS_TOKENS = {
    'clash_royale': os.getenv('CLASH_ROYALE_TOKEN', '') 
}
