from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from project.main.routes import main
from project.admin.routes import admin
from project import config
from project.models import db, User, Collection

# create and configure app
app = Flask(__name__)
app.config.from_object(config.Config)
migrate = Migrate(app, db)

# initialize included apps
with app.app_context():
    db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User, 'Collection': Collection}

# register blueprints
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
