from flask import Blueprint, request, jsonify
from models.person import Person
from collections import deque, defaultdict

connection_bp=Blueprint('connection', __name__)

#API endpoints for connections
@connection_bp.route('/connections', methods=['GET', 'POST', 'DELETE'])
def connections():
    #making connection between 2 people
    if(request.method=='POST'):
        data=request.json
        person1=Person.objects(person_id=data.get("id1")).first()
        person2=Person.objects(person_id=data.get("id2")).first()

        person1.connect(person2)
        return 'Connection Made'
    
    #Reading shortest connecting path length
    if(request.method=='GET'):
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
        person1=Person.objects(person_id=data.get("id1")).first()
        person2=Person.objects(person_id=data.get("id2")).first()

        person1.disconnect(person2)
        return 'Connection Made'