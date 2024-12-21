class Sisig:
    def __init__(self, onion, calamansi, labuyo, ears, liver, belly):
        self.__onion = onion 
        self.__calamansi = calamansi
        self.__labuyo = labuyo
        self.__ears = ears
        self.__liver = liver
        self.__belly = belly
    
    def __str__(self):
        return f'''My sisig has {self.__onion} pcs of minced onion, {self.__calamansi} pcs of calamansi, {self.__labuyo} labuyo, {self.__ears} kg of ears, {self.__liver} kg of liver {self.__belly} kg of belly.'''
        
        
sizling_sisig = Sisig(2,2,1,1,1,1)
print(sizling_sisig)
       
