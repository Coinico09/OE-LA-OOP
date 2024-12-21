class Dog:
    def __init__(self, name):
        self.name = name 
  
    def speak(self):  
        print(f"{self.name} Bark!")  
  
class Cat:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        print(f"{self.name} Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f" {self.name} Chrip!")
        
class Fish:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "..."
    
    def animal_sound(animal):
        print(f"{animal.name} says: {animal.speak}")

dog = Dog ("dog")
cat = Cat("cat")
bird = Bird("bird")
fish = Fish("fish")

