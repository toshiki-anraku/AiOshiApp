import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI_FORMAT', 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}').format(**{
        'user':     os.environ.get('DB_USER', 'postgres'),
        'password': os.environ.get('DB_PASSWORD', 'postgres'),
        'host':     os.environ.get('DB_HOST', 'postgres_con'),
        'port':     os.environ.get('DB_PORT', '5432'),
        'name':     os.environ.get('DB_NAME', 'ai_oshi_db'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig