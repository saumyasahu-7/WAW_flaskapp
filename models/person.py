from mongoengine import *
from .house import House
import random

disconnect()
connect(db="persons", alias='default')

class Person(Document):
    meta = {'allow_inheritance': True}

    name = StringField(required=True)
    house = ReferenceField(House)
    personal_connections = ListField(ReferenceField('self'))
    person_id = StringField(required=True, unique=True)

    def connect(self, person_to_connect: 'Person'):
        self.personal_connections.append(person_to_connect)
        person_to_connect.personal_connections.append(self)
        self.save()
        person_to_connect.save()

    def disconnect(self, person_to_connect: 'Person'):
        self.personal_connections.remove(person_to_connect)
        person_to_connect.personal_connections.remove(self)
        self.save()
        person_to_connect.save()

class Student(Person):
    points=IntField(default=0)

    def __add_to_house(self):
        self.house.add_student_to_house(self)
        self.house.save()

    def assign_house(self):
        #used House() to access instance attributes of House
        house_chosen=random.choice(House.objects())
        self.house=house_chosen
        self.save()
        self.__add_to_house()

    def add_points(self,points):
        self.points=self.points+points
        self.house.add_points_to_house(points)
        self.save()

class Professor(Person):

    def add_to_house(self,house):
        self.house.add_professor_to_house(self)
        self.save()