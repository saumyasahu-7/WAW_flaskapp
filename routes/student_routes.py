from flask import Blueprint, request, jsonify
from Wizards_and_Witches.person import Student
from Wizards_and_Witches.houses import House

student_bp = Blueprint('student', __name__)

#API endpoints for Students
@student_bp.route('/students', methods=['GET', 'POST', 'PUT', 'DELETE'])
def students():
    #Reading data of all the students
    if(request.method=='GET'):
        all_students=[]
        for instance in Student.student_instances.values():
            stud={
                "student_id": instance.id,
                "name": instance.name,
                "house": instance.house['house_name'],
                "points": instance.points,
                "no_of_connections": len(instance.personal_connections)
            }
            all_students.append(stud)
        return jsonify(all_students)
    
    #Creating new Students
    if(request.method=='POST'):
        data=request.json
        id='s'+str(Student.student_count)
        name=data.get('name')
        student=Student(name,id)
        Student.student_count+=1
        return 'Created Student'
        
    #Updating data of a student
    if(request.method=='PUT'):
        student_id = request.args.get('student_id')
        new_data=request.json
        name=new_data.get('name')
        house_name=new_data.get('house')
        instance=Student.student_instances[student_id]
        if(instance.id==student_id):
            if(name):
                instance.name=name
            if(house_name):
                instance.house=House().mapping_to_house_name[house_name]
        return 'Updated Student'


    #deleting a student
    if(request.method=='DELETE'):
        student_id = request.args.get('student_id')
        instance=Student.student_instances[student_id]
        if(instance.id==student_id):
            del Student.student_instances[student_id]
            del instance
        return 'Deleted Student'