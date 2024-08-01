from flask import Blueprint, request, jsonify
from models.person import Person
from models.house import House

person_bp=Blueprint('person', __name__)

@person_bp.route('/person/connections')
def get_connections():
    id = request.args.get('id')
    person=Person.objects(person_id=id).first()
    connections=[]
    for connection in person.personal_connections:
        connected={
            'id':connection.person_id,
            'name':connection.name
        }
        connections.append(connected)
    return jsonify(connections)