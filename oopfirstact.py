class hero():
    def __init__(self, name, role, dmg_type, health, auto_attck_dmg, mana):
         self.name = name
         self.role = role
         self.dmg_type = dmg_type
         self.health = health
         self.mana = mana
         self.auto_attck_dmg = auto_attck_dmg
         
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
        
hero_mm1 = hero("claude", "marksman", "burst damage",2370,97,450)
hero_fighter1 = hero("paquito", "fighter", "close damage",2798,121,0)
hero_support1 = hero("rafaela", "support", "heal",2441,177,545,)
hero_tank1 = hero("minotaur", "aoe", "sustain",2859,123,0)
hero_support1 = hero("floryn", "debuff", "heal",2401,119,550)

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} hp
{hero_mm1.mana} mana
{hero_mm1.auto_attck_dmg} basic damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} hp
{hero_fighter1.mana} mana
{hero_fighter1.auto_attck_dmg} basic damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}


{hero_support1.name}
{hero_support1.role}
{hero_support1.health} hp
{hero_support1.mana} mana
{hero_support1.auto_attck_dmg} basic damage
{hero_support1.dmg_type}
{hero_support1.describe()}

{hero_tank1.name}
{hero_tank1.role}
{hero_tank1.health} hp
{hero_tank1.mana} mana
{hero_tank1.auto_attck_dmg} basic damage
{hero_tank1.dmg_type}
{hero_tank1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} hp
{hero_fighter1.mana} mana
{hero_fighter1.auto_attck_dmg} basic damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

''')
