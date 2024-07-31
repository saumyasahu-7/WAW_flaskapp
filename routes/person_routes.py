from flask import Blueprint, request, jsonify
from Wizards_and_Witches.person import Person
from Wizards_and_Witches.houses import House

person_bp=Blueprint('person', __name__)

@person_bp.route('/person/connections')
def get_connections():
    id = request.args.get('id')
    connections=[]
    for instance in Person.instances[id].personal_connections:
        connection={}
        connection['name']=instance.name
        connections.append(connection)
    return jsonify(connections)