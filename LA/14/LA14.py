class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"Name: {self.name}  Age: {self.age}")
        
        
        
class Tobey(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age,)
        self.movietitle = movietitle


class Andrew(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age,)
        self.movietitle = movietitle

