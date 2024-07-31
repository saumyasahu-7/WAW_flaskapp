from flask import Flask, request, jsonify
from collections import deque, defaultdict
from Wizards_and_Witches.houses import House
from Wizards_and_Witches.person import Person, Student, Professor
app = Flask(__name__)

#API endpoints for Students
@app.route('/students', methods=['GET', 'POST', 'PUT', 'DELETE'])
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

@app.route('/person/connections')
def get_connections():
    id = request.args.get('id')
    connections=[]
    for instance in Person.instances[id].personal_connections:
        connection={}
        connection['name']=instance.name
        connections.append(connection)
    return jsonify(connections)

#API endpoints for Professor
@app.route('/professors', methods=['GET', 'POST', 'PUT', 'DELETE'])
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

#API endpoints for houses
@app.route('/houses', methods=['GET'])
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
@app.route('/houses/professors')
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
@app.route('/houses/students')
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

#API endpoint for adding points to student and their respective house
@app.route('/addpoints', methods=['POST'])
def add_points():
    data=request.json
    student_id=data.get('student_id')
    points_added=data.get('points_added')
    for instance in Student.student_instances:
        if(instance.id==student_id):
            instance.add_points(points_added)
            break
    return "Points added"

#API endpoints for connections
@app.route('/connections', methods=['GET', 'POST', 'DELETE'])
def connections():
    #making connection between 2 people
    if(request.method=='POST'):
        data=request.json
        id1=data.get("id1")
        id2=data.get("id2")

        Person.instances[id1].personal_connections.append(Person.instances[id2])
        Person.instances[id2].personal_connections.append(Person.instances[id1])
        return 'Connection Made'
    
    #Reading shortest connecting path length
    if(request.method=='GET'):
        data=request.json
        id1 = request.args.get('id1')
        id2 = request.args.get('id2')
        queue=deque()
        dist=defaultdict(lambda:1e9)
        dist[Person.instances[id1]]=0
        queue.append([Person.instances[id1],0])

        while(len(queue)>0):
            top=queue.popleft()
            curr_person=top[0]
            curr_dist=top[1]
            for connection in curr_person.personal_connections:
                if(dist[connection]>curr_dist+1):
                    dist[connection]=curr_dist+1
                    queue.append([connection,curr_dist+1])
                    
        if(dist[Person.instances[id2]]==1e9):
            return {"message":"not connected"}
        else:
            return {"length of shorted connecting path":dist[Person.instances[id2]]}
        
    #deleting connection between 2 people
    if(request.method=='DELETE'):
        data=request.json
        id1=data.get("id1")
        id2=data.get("id2")

        Person.instances[id1].personal_connections.remove(Person.instances[id2])
        Person.instances[id2].personal_connections.remove(Person.instances[id1])
        return 'Connection Deleted'

@app.route('/', methods=['GET'])
def wizards_and_witches():
    return "Wizards and Witches"

if(__name__=="__main__"):
    app.run(debug=True)
