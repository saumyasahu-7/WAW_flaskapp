from flask import Blueprint, request, jsonify
from models.person import Student
from db import mongo
# from flask_validator import ValidateJson, ValidateInteger, ValidateString

addpoints_bp = Blueprint('addpoints', __name__)

def add_points_to_house():
    pass
# API endpoint for adding points to a student and their respective house
@addpoints_bp.route('/addpoints', methods=['PUT'])
def add_points():
    data = request.json
    student_id = data.get('student_id')
    points_added = data.get('points_added')

    student = mongo.db.students.find({"id":student_id})
    
    if not student:
        return jsonify({"message": "Student not found"}), 404

    

    return jsonify({"message": "Points added successfully", "student_id": student_id, "points_added": points_added}), 200
