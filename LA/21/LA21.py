class Adobo:
    def __init__(self, karne, tuyo, masabaw):
        self.karne = karne  # Public
        self._tuyo = tuyo   # Protected
        self.__masabaw = masabaw  # Private
        
    def __str__(self):
        return f"Ang adobo ko ay pwedeng {self.karne}, {self._tuyo}, {self.__masabaw}"
        
    def may_carrot_ba(self):
        return self.__masabaw
        
    def set_masabaw(self, new_value):
        self.__masabaw = new_value

    def getter(self):
        return self.__masabaw

    def setter(self, new_value):
        self.__masabaw = new_value

adobong_tuyo = Adobo("chicken", "water", "asin")
adobo2 = Adobo("A5", "water", "toyo")
adobo3 = Adobo("Pork", "water", "onion")

adobong_tuyo.setter("Paminta")
print(adobong_tuyo.getter())  

