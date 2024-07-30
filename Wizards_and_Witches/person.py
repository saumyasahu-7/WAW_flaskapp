from Wizards_and_Witches.houses import House
import random
class Person:
    instances={}
    def __init__(self, name: str, id: str, house=None):
        self.name=name
        self.house=house
        self.personal_connections=[]
        self.id=id

    def connect(self, person_to_connect: 'Person'):
        self.personal_connections.append(person_to_connect)

    def display_house(self):
        print(self.name, 'belongs to', self.house['house_name'])
    
    def display_connections(self):
        print(self.name,'has the following connections:')
        for ele in self.personal_connections:
            print(ele.name)

class Student(Person):
    student_instances={}
    def __init__(self, name: str, id:str, house=None):
        super().__init__(name, id)
        self.points=0
        Person.instances[id]=self
        Student.student_instances[id]=self
        self.assign_house()

    def __add_to_house(self):
        self.house['students'].append(self)

    def display_student_points(self):
        print(self.name, 'has', self.points, 'points.')

    def assign_house(self):
        #used House() to access instance attributes of House
        house_chosen=random.choice(House().all_houses)
        self.house=house_chosen
        self.__add_to_house()

    def add_points(self,points):
        self.points=self.points+points
        self.house['points']+=self.house['points']+points

class Professor(Person):
    professor_instances={}
    def __init__(self, name: str, id:str, house=None):
        super().__init__(name, id, house)
        self.__add_to_house()
        Person.instances[id]=self
        Professor.professor_instances[id]=self

    def __add_to_house(self):
        self.house['professors'].append(self)