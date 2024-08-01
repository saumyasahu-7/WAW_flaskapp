from flask import Blueprint, request, jsonify
from models.house import House

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
    professors_in_house=house.professors
    return jsonify(professors_in_house)

#API endpoint for getting students in a house
@house_bp.route('/houses/students')
def get_students_in_house():
    house_id = request.args.get('house_id')
    house=House.objects(house_id=house_id).first()
    
    if not house:
        return jsonify({"message":"House not found"})
    students_in_house=house.students
    return jsonify(students_in_house)