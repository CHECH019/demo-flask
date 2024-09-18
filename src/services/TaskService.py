from src.models.TaskModel import Task
from src import db

def create_task(title, description, user_id):
    new_task = Task(titulo=title, descripcion=description, id_usuario=user_id)
    db.session.add(new_task)
    db.session.commit()
    return {"message": "¡Tarea creada exitosamente!"}

def list_tasks(user_id):
    tasks = Task.query.filter_by(id_usuario=user_id).all()
    return [{"id": task.id_tarea, "title": task.titulo, "description": task.descripcion} for task in tasks]
