from datetime import datetime
from src.db.database import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id_tarea = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)

    usuario = db.relationship('User', backref=db.backref('tareas', lazy=True))

    def __init__(self, titulo, descripcion, id_usuario):
        self.titulo = titulo
        self.descripcion = descripcion
        self.id_usuario = id_usuario

    def __repr__(self):
        return f'<Tarea {self.titulo}>'
