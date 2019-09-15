from flask import Flask, g, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api/v1')
ma = Marshmallow()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Include our Routes
        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        from .resources import students
        api.add_resource(students.StudentsResource, '/students')
        api.add_resource(students.StudentResource, '/students/<id>/')
        app.register_blueprint(api_bp)
        # Create tables for our models
        db.create_all()

    return app
