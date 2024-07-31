from flask import Blueprint, request, jsonify
from Wizards_and_Witches.person import Student

addpoints_bp=Blueprint('addpoints', __name__)
#API endpoint for adding points to student and their respective house
@addpoints_bp.route('/addpoints', methods=['PUT'])
def add_points():
    if(request.method=='PUT'):
        data=request.json
        student_id=data.get('student_id')
        points_added=data.get('points_added')
        for instance in Student.student_instances.values():
            if(instance.id==student_id):
                instance.add_points(points_added)
                break
    return "Points added"