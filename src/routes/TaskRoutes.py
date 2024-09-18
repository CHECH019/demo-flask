from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services.TaskService import create_task, list_tasks

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def create_new_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    user_identity = get_jwt_identity()
    user_id = user_identity['user'] 
    result = create_task(title, description, user_id)
    return jsonify(result)

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_identity = get_jwt_identity()
    user_id = user_identity['user']  
    tasks = list_tasks(user_id)
    return jsonify(tasks)
