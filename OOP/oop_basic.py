
class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        
    def bark(self):
        print(self.name, "woof woof")
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age    
                
dogs_name = ["Star", "Comet"]
dogs_age = [3, 5]