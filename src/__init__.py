from flask import Flask
from src.db.database import db


from decouple import config
from flask_jwt_extended import JWTManager
from src.routes.AuthRoutes import auth_bp
from src.routes.TaskRoutes import tasks_bp

app = Flask(__name__)




def init_app(configuration):


    app.config.from_object(configuration)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@{config('MYSQL_HOST')}/{config('MYSQL_DB')}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    app.config['JWT_SECRET_KEY'] = config('JWT_KEY')

    jwt = JWTManager(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    db.init_app(app)


    return app

