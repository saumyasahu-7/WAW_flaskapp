from flask import Flask
from routes import init_app
from flask_pymongo import PyMongo

# Initialize PyMongo without app
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    # Configure the MongoDB connection
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
    # Initialize PyMongo with the app
    mongo.init_app(app)
    # Import and register blueprints (or routes)
    init_app(app)
    return app

app = create_app()

@app.route('/')
def hello_world():
    # Use the mongo instance to insert a document
    mongo.db.inventory.insert_one({"a": 1})
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)
