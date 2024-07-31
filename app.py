from flask import Flask
from routes import init_app

def create_app():
    app = Flask(__name__)
    # Import and register blueprints (or routes)
    init_app(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)