from flask import Blueprint, request, jsonify
from src.services.AuthService import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result = register_user(username, password)
    return jsonify(result)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result = login_user(username, password)
    return jsonify(result)
