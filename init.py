from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config

db = SQLAlchemy()


def init_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['FLASK_ENV'] = config('FLASK_ENV', default='development')

    db.init_app(app)

    with app.app_context():
        if app.config['FLASK_ENV'] == 'development':
            db.create_all()

    from routes.inventario_routes import inventario_bp
    app.register_blueprint(inventario_bp, url_prefix='/api/inventario')

    return app