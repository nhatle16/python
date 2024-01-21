class Person:
    num_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def add_person(cls):
        cls.num_of_people += 1
        
    @classmethod
    def number_of_people(cls):
        return cls.num_of_people
                    
p1 = Person("person1")
print(Person.number_of_people())
p2 = Person("person2")
print(Person.number_of_people())