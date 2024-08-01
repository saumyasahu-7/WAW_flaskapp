from flask import Blueprint, request, jsonify
from models.person import Student
from models.house import House

student_bp = Blueprint('student', __name__)

#API endpoints for Students
@student_bp.route('/students', methods=['GET', 'POST', 'PUT', 'DELETE'])
def students():
    #Reading data of all the students
    if(request.method=='GET'):
        all_students=[]
        for student in Student.objects():
            stud={
                'name':student.name,
                'id':student.person_id,
                'house':student.house.house_name,
                'points':student.points,
                'no of connections':len(student.personal_connections)
            }
            all_students.append(stud)
        return jsonify(all_students)
    
    #Creating new Students
    if(request.method=='POST'):
        data=request.json
        id='s'+str(Student.objects().count()+1)
        name=data.get('name')
        student=Student(name=name,person_id=id)
        student.assign_house()
        return jsonify({"message": "Student created"})
        
    #Updating data of a student
    if(request.method=='PUT'):
        student_id = request.args.get('student_id')
        new_data=request.json
        student=Student.objects(person_id=student_id).first()
        if not student:
            return jsonify({"message": "Student not found"})
        name=new_data.get('name')
        house=House.objects(house_name=new_data.get('house_name')).first()
        if(name):
            student.name = new_data.get('name', student.name)
            student.save()
        if(house):
            student.house= new_data.get('house', student.house)
            student.save()
        return jsonify({"message": "Student updated"})


    #deleting a student
    if(request.method=='DELETE'):
        student_id = request.args.get('student_id')
        student=Student.objects(person_id=student_id).first()
        if not student:
            return jsonify({"message": "Student not found"})
        student.delete()
        return jsonify({"message": "Student deleted"})