from flask import Flask
from flask_pymongo import PyMongo
from mongoengine import connect, disconnect
from routes.__init__ import init_app
from models.house import House

disconnect()
connect(db="mydb", alias='default')

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if(__name__=="__main__"):
    Gryffindor=House.create_house("Gryffindor","h1")
    Hufflepuff=House.create_house("Hufflepuff","h2")
    Ravenclaw=House.create_house("Ravenclaw","h3")
    Slytherin=House.create_house("Slytherin","h4")
    app.run(debug=True, port=5001)