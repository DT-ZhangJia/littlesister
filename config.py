"""
little sister config
"""
# pylint: disable=invalid-name, too-few-public-methods

class Config:
    """config"""
    SECRET_KEY = ''
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[SVInsight Sister]'
    FLASKY_MAIL_SENDER = ''
    FLASKY_ADMIN = ''

    @staticmethod
    def init_app(app):
        """pass"""
        pass


class DevelopmentConfig(Config):
    """Dev"""
    DEBUG = True
    MAIL_SERVER = ''
    MAIL_PORT = 
    MAIL_USE_TLS = 
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = ''


class TestingConfig(Config):
    """test"""
    TESTING = True

class ProductionConfig(Config):
    """production"""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
