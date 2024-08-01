from flask import Blueprint, request, jsonify
from Wizards_and_Witches.person import Person
from Wizards_and_Witches.houses import House

person_bp=Blueprint('person', __name__)

@person_bp.route('/person/connections')
def get_connections():
    id = request.args.get('id')
    person=Person.objects(person_id=id).first()
    connections=person.personal_connections
    return jsonify(connections)