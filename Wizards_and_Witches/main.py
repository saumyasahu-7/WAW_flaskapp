from person import Student, Professor
from houses import House
from collections import deque, defaultdict

#adding students
Harry=Student('Harry','s1')
Harry.assign_house()

Hermoine=Student('Hermoine','s2')
Hermoine.assign_house()

Draco=Student('Draco','s2')
Draco.assign_house()

#Adding professors(professors have pre decided house)
Dumbledore=Professor('Dumbledore','p1',House().Gryffindor)
Hagrid=Professor('Hagrid','p2',House().Hufflepuff)

#displaying houses of students and professors
def show_house():
    Harry.display_house()
    Hermoine.display_house()
    Draco.display_house()
    Dumbledore.display_house()
    Hagrid.display_house()
    print()

#listing members in each house
def show_members():
    #used House() to access instance attributes of House
    House().Gryffindor['list_members']('Gryffindor',House().Gryffindor['students'],House().Gryffindor['professors'])
    House().Hufflepuff['list_members']('Hufflepuff',House().Hufflepuff['students'],House().Hufflepuff['professors'])
    House().Ravenclaw['list_members']('Ravenclaw',House().Ravenclaw['students'],House().Ravenclaw['professors'])
    House().Slytherin['list_members']('Slytherin',House().Slytherin['students'],House().Slytherin['professors'])
    print()

#add points
def give_points():
    Harry.add_points(5)
    Hermoine.add_points(7)
    Draco.add_points(27)

#displaying points
def show_points():
    Harry.display_student_points()
    Harry.house['display_house_points'](Harry.house['house_name'],Harry.house['points'])
    Hermoine.display_student_points()
    Hermoine.house['display_house_points'](Hermoine.house['house_name'],Hermoine.house['points'])
    Draco.display_student_points()
    Draco.house['display_house_points'](Draco.house['house_name'],Draco.house['points'])
    print()

#connecting people
def connect_people():
    Draco.connect(Dumbledore)
    Dumbledore.connect(Draco)
    Harry.connect(Hagrid)
    Hagrid.connect(Harry)
    Hermoine.connect(Hagrid)
    Hagrid.connect(Hermoine)
    Hagrid.connect(Dumbledore)
    Dumbledore.connect(Hagrid)

def show_connections():
    Harry.display_connections()
    Hermoine.display_connections()
    Draco.display_connections()
    Dumbledore.display_connections()
    Hagrid.display_connections()
    print()

#searching shortest path
def shortest_connecting_path():
    queue=deque()
    dist=defaultdict(lambda:1e9)
    dist[Harry]=0
    queue.append([Harry,0])

    while(len(queue)>0):
        top=queue.popleft()
        curr_person=top[0]
        curr_dist=top[1]
        for connection in curr_person.personal_connections:
            if(dist[connection]>curr_dist+1):
                dist[connection]=curr_dist+1
                queue.append([connection,curr_dist+1])
                
    if(dist[Hermoine]==1e9):
        print("Harry and Hermoine are not conected")
    else:
        print('The shortest connecting path between Harry and Hermoine is of distance:',dist[Hermoine])

show_house()
show_members()
give_points()
show_points()
connect_people()
show_connections()
shortest_connecting_path()
