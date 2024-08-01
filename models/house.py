from mongoengine import *

disconnect()
connect(db="houses", alias='default')

class House(Document):

    house_id = StringField(required=True, unique=True)
    house_name = StringField(required=True)
    points = IntField(default=0)
    students = ListField(ReferenceField('Student'))
    professors = ListField(ReferenceField('Professor'))

    def create_house(house_name, house_id):
        if(House.objects(house_id=house_id).first()==None):
            house=House(house_name=house_name, house_id=house_id)
            house.save()
            return house
        
    def add_points_to_house(self,points):
        self.points+=points
        self.save()

    def add_student_to_house(self,student):
        student.save()
        self.students.append(student)
        self.save()

    def add_professor_to_house(self,professor):
        professor.save()
        self.professors.append(professor)
        self.save()