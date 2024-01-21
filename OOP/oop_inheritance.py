class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"My name is {self.name}, I'm {self.age} years old")
    
    def speak(self):
        print("I don't know what to say")
        
class Dog(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
    
    def speak(self):
        print("woof woof")
        
    def show(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I'm a {self.species}")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("meow meow")
    
    def show(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I'm {self.color}")
    
class Fish(Pet):
    pass
        

pet = Pet("Nolan", 10)
pet.speak()
s = Dog("Sao", 3, "corgi")
s.show()
s.speak()
c = Cat("Chill", 5, "gray")
c.show()