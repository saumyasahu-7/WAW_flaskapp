#singleton House class
class House:
    _instance = None
    all_houses=[]
    mapping_to_house_name={}
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(House, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.Gryffindor = self._create_house('Gryffindor','h1', 'Fire')
            self.Hufflepuff = self._create_house('Hufflepuff', 'h2','Earth')
            self.Ravenclaw = self._create_house('Ravenclaw', 'h3','Air')
            self.Slytherin = self._create_house('Slytherin', 'h4','Water')

            self.all_houses.append(self.Gryffindor)
            self.all_houses.append(self.Hufflepuff)
            self.all_houses.append(self.Ravenclaw)
            self.all_houses.append(self.Slytherin)
            
            self.mapping_to_house_name["Gryffindor"]=self.Gryffindor
            self.mapping_to_house_name["Hufflepuff"]=self.Hufflepuff
            self.mapping_to_house_name["Ravenclaw"]=self.Ravenclaw
            self.mapping_to_house_name["Slytherin"]=self.Slytherin
    

    def list_members(self,house_name:str, students: list, professors: list):
        print('The list of Students in', house_name,':')
        for student in students:
            print(student.name)
        print('The list of Professors in', house_name,':')
        for professor in professors:
            print(professor.name)

    def display_house_points(self,house_name:str, points: int):
        print(house_name, 'has', points,'points.')

    def _create_house(self, name, id, element):
        return {
            'house_id':id,
            'house_name': name,
            'element': element,
            'students': [],
            'professors': [],
            'points': 0,
            'list_members': self.list_members,
            'display_house_points': self.display_house_points
        }