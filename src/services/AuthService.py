import traceback

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from src.models.UserModel import User
from src.db.database import db

def register_user(username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {"message": "¡Usuario creado exitosamente!"}

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={"user": user.id_user})
        return {"token": access_token}
    else:
        return {"message": "Credenciales inválidas"}, 401
