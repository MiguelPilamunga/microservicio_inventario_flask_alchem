from decouple import config

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST_DEV')}:{config('DB_PORT', default='3306')}/{config('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = config('FLASK_ENV', default='development')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False