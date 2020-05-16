import os
from datetime import timedelta


class BaseConfig:
    """Base configuration
    Here is the basic configuration:
    
    TESTING: Testing mode
    SQLALCHEMY_TRACK_MODIFICATIONS: Activate runtime notifications
    SECRET_KEY: Contain the secret key to sign the session cokie
    TOKEN_SECRET: Contains the seed to decrypt the Opt
    PERMANENT_SESSION_LIFETIME: Contains the expiration time for the session

    """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    TOKEN_SECRET = 'oeRaYY7Wo24sDqKSX3IM9ASGmdGPmkTd9jo1QTy4b7P9Ze5_9hKolVX8xNrQDcNRfVEdTZNOuOyqEGhXEbdJI'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
