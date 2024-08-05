from flask import Blueprint

# Import route modules
from .student_routes import student_bp
from .professor_routes import professor_bp
from .house_routes import house_bp
from .connection_routes import connection_bp
from .addpoints_routes import addpoints_bp
from .person_routes import person_bp

def init_app(app):
    app.register_blueprint(student_bp)
    app.register_blueprint(professor_bp)
    app.register_blueprint(house_bp)
    app.register_blueprint(connection_bp)
    app.register_blueprint(addpoints_bp)
    app.register_blueprint(person_bp)
