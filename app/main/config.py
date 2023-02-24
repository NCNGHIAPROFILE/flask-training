import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # import secrets
    # secrets.token_hex(12)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f91dedd759d745e9bfebd4a3f942cec3'
    DEBUG = False

key = Config.SECRET_KEY

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Web_Flask_Training.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)