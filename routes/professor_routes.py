from flask import Blueprint, request, jsonify
from Wizards_and_Witches.person import Professor
from Wizards_and_Witches.houses import House

professor_bp=Blueprint('professor', __name__)
#API endpoints for Professor
@professor_bp.route('/professors', methods=['GET', 'POST', 'PUT', 'DELETE'])
def professors():
    #Reading data of all the professors
    if(request.method=='GET'):
        all_professors=[]
        for instance in Professor.professor_instances.values():
            prof={
                "professor_id": instance.id,
                "name": instance.name,
                "house": instance.house['house_name'],
                "no_of_connections": len(instance.personal_connections)
            }
            all_professors.append(prof)
        return jsonify(all_professors)
    
    #Creating new professors
    if(request.method=='POST'):
        data=request.json
        id='p'+str(Professor.professor_count)
        name=data.get("name")
        house_name=data.get("house")
        professor=Professor(name,id,House().mapping_to_house_name[house_name])
        Professor.professor_count+=1
        return 'Created Professor'
        
    #Updating data of a professor
    if(request.method=='PUT'):
        professor_id = request.args.get('professor_id')
        new_data=request.json
        name=new_data.get('name')
        house_name=new_data.get('house')
        instance=Professor.professor_instances[professor_id]
        if(instance.id==professor_id):
            if(name):
                instance.name=name
            if(house_name):
                instance.house=House().mapping_to_house_name[house_name]
        return 'Updated Professor'

    #deleting a professor
    if(request.method=='DELETE'):
        professor_id = request.args.get('professor_id')
        instance=Professor.professor_instances[professor_id]
        if(instance.id==professor_id):
            del Professor.professor_instances[professor_id]
            del instance
        return 'Deleted Professor'
