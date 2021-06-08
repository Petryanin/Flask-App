import os
from secrets import token_hex

user = os.environ['USER']


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}::@localhost/appdb'
    SECRET_KEY = os.urandom(16)

    ### Flask-security ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
