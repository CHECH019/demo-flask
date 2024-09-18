from config import config
from src import init_app
from src import db
from src.models import UserModel,TaskModel

configuration = config['development']
app = init_app(configuration)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
