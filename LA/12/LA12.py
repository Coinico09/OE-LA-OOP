class toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describetoy(self):
        print(f"toys name : {self.name}, {self.price}")

class laruan(toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toysrus = laruan ("hotwheels jeep", 300)
toysrus.describetoy()
        
