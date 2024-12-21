class hero():
    def __init__(self, name, role, hp, mana, normal_attck):
     self.name = name
     self.role = role
     self.hp = hp
     self.mana = mana 
     self.normal_attck = normal_attck 

    def __str__(self):
        return "miya is a marksman hero"

    def describe(self):
       print(f"{self.name} is a {self.role}")


marksman = hero("miya", "marksman", "500", "115", "89")

print(f'''
{marksman.name}
{marksman.role}
{marksman.hp}
{marksman.mana}
{marksman.normal_attck}''')

print(marksman)
