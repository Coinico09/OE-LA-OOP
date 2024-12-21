class Party:
    def __init__(self, theme):
        self.theme = theme
    def __specialdish(self):
        print(f"secret dish: lechon {self.theme}")
    def celebration(self):
        print(f"{self.theme} foods: carbonara, rice, ham, chicken, ice cream")
        print("specialdish: crispy pata")
        self.__specialdish()
        
xmasparty = Party ("xmas")
xmasparty.celebration()
