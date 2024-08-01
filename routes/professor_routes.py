from flask import Blueprint, request, jsonify
from models.person import Professor
from models.house import House

professor_bp=Blueprint('professor', __name__)
#API endpoints for Professor
@professor_bp.route('/professors', methods=['GET', 'POST', 'PUT', 'DELETE'])
def professors():
    #Reading data of all the professors
    if(request.method=='GET'):
        all_professors=[]
        for professor in Professor.objects():
            prof={
                'name':professor.name,
                'id':professor.person_id,
                'house':professor.house.house_name,
                'no of connections':len(professor.personal_connections)
            }
            all_professors.append(prof)
        return jsonify(all_professors)
    
    #Creating new professors
    if(request.method=='POST'):
        data=request.json
        id='p'+str(Professor.objects().count()+1)
        name=data.get('name')
        house_name=data.get('house_name')
        professor=Professor(name=name,person_id=id,house=House.objects(house_name=house_name).first())
        house=House.objects(house_name=house_name).first()
        professor.add_to_house(house)
        return jsonify({"message": "Professor created"})
        
    #Updating data of a professor
    if(request.method=='PUT'):
        professor_id = request.args.get('professor_id')
        new_data=request.json
        professor=Professor.objects(person_id=professor_id).first()
        if not professor:
            return jsonify({"message": "professor not found"})
        name=new_data.get('name')
        house=House.objects(house_name=new_data.get('house_name')).first()
        if(name):
            professor.name = name
            professor.save()
        if(house):
            professor.house= House.objects(house_name=house_name)
            professor.save()
        return jsonify({"message": "professor updated"})

    #deleting a professor
    if(request.method=='DELETE'):
        professor_id = request.args.get('professor_id')
        professor=Professor.objects(person_id=professor_id).first()
        if not professor:
            return jsonify({"message": "Professor not found"})
        professor.delete()
        return jsonify({"message": "Professor deleted"})
