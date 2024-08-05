from db import app # Import mongo from db
from models.house import House
from routes.__init__ import init_app

if __name__ == "__main__":
    house = House("Gryffindor", "h1")
    house = House("Hufflepuff", "h2")
    house = House("Ravenclaw", "h3")
    house = House("Slytherin", "h4")

    init_app(app)
    app.run(debug=True, port=5001)
