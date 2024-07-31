from flask import Blueprint, request, jsonify
from Wizards_and_Witches.houses import House

house_bp=Blueprint('house', __name__)
#API endpoints for houses
@house_bp.route('/houses', methods=['GET'])
def houses():
    if(request.method=='GET'):
        house_and_points=[]
        for house in House().all_houses:
            house_detail={}
            house_detail['house_name']=house['house_name']
            house_detail['points']=house['points']
            house_and_points.append(house_detail)
        return jsonify(house_and_points)

#API endpoint for getting professors in a house
@house_bp.route('/houses/professors')
def get_professors_in_house():
    house_id = request.args.get('house_id')
    professors_in_house=[]
    for house in House().all_houses:
        if(house['house_id']==house_id):
            for instance in house['professors']:
                prof={
                "professor_id": instance.id,
                "name": instance.name,
                "house": instance.house['house_name'],
                "no_of_connections": len(instance.personal_connections)
                }
                professors_in_house.append(prof)
            break
    return jsonify(professors_in_house)

#API endpoint for getting students in a house
@house_bp.route('/houses/students')
def get_students_in_house():
    house_id = request.args.get('house_id')
    students_in_house=[]
    for house in House().all_houses:
        if(house['house_id']==house_id):
            for instance in house['students']:
                stud={
                    "student_id": instance.id,
                    "name": instance.name,
                    "house": instance.house['house_name'],
                    "points": instance.points,
                    "no_of_connections": len(instance.personal_connections)
                }
                students_in_house.append(stud)
            break
    return jsonify(students_in_house)