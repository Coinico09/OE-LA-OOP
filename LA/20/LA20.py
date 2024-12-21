class Adobo:
    def __init__(self, karne, tuyo, masabaw):
        self.karne = karne
        self.tuyo = tuyo
        self.masabaw = masabaw

    def __str__(self):
        return f"Ang adobo ko ay pwedeng {self.karne}, {self.tuyo}, {self.masabaw}"

    def may_carrot_ba(self):
        return self.masabaw

adobong_dry = Adobo("manok", "tubig, asin", "toyo, asukal")
adobo2 = Adobo("A5", "tubig", "toyo, suka")
adobo3 = Adobo("Pork", "water", "toyo, asin, asukal")

print(adobong_dry.may_carrot_ba())
print(adobo2.may_carrot_ba())
print(adobo3.may_carrot_ba())
