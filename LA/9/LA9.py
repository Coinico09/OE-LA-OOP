class car:
    def __init__(self,brand):
       self.brand = brand 
    def __str__(self):
       return f"car {self.brand}"


my_car = car ("mitsubishi")
del my_car
print(my_car)
