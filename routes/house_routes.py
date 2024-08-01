from flask import Blueprint, request, jsonify
from models.house import House
from models.person import Professor, Student

house_bp=Blueprint('house', __name__)
#API endpoints for houses
@house_bp.route('/houses', methods=['GET'])
def houses():
    if(request.method=='GET'):
        house_and_points=[]
        for house in House.objects():
            h={
                "name":house.house_name,
                "points":house.points
            }
            house_and_points.append(h)
        return jsonify(house_and_points)

#API endpoint for getting professors in a house
@house_bp.route('/houses/professors')
def get_professors_in_house():
    house_id = request.args.get('house_id')
    house=House.objects(house_id=house_id).first()
    
    if not house:
        return jsonify({"message":"House not found"})
    professors_in_house=[]
    for professor in house.professors:
            prof={
                'name':professor.name,
                'id':professor.person_id,
                'house':house.house_name,
                'no of connections':len(professor.personal_connections)
            }
            professors_in_house.append(prof)
    return jsonify(professors_in_house)

#API endpoint for getting students in a house
@house_bp.route('/houses/students')
def get_students_in_house():
    house_id = request.args.get('house_id')
    house=House.objects(house_id=house_id).first()
    
    if not house:
        return jsonify({"message":"House not found"})
    students_in_house=[]
    for student in house.students:
            stud={
                'name':student.name,
                'id':student.person_id,
                'house':house.house_name,
                'no of connections':len(student.personal_connections)
            }
            students_in_house.append(stud)
    return jsonify(students_in_house)