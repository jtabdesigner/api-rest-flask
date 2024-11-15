from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = None
db = SQLAlchemy()
cache = Cache()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    global app

    if app is None:
        app = Flask(__name__)

        # Configurações do app
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
        app.config['CACHE_TYPE'] = 'simple'
        app.config['JWT_SECRET_KEY'] = 'your-secret-key'

        # Inicialização de db, cache, jwt
        db.init_app(app)
        cache.init_app(app)
        jwt.init_app(app)
        migrate.init_app(app, db)

        from routes import api_blueprint
        app.register_blueprint(api_blueprint)

    return app

# Se o arquivo for executado diretamente, rodar o servidor Flask
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
