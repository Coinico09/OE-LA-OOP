class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack (self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} with {self.attack_power} damage")
        print(f"{target.name} has now {target.health}")
        if target.health <= 0:
            print(f" {target.name} is defeated")
            
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} Current health: {self.health}")
        
echo = Player ("echo", 280, 70)
venture = Player ("venture", 375, 30)
echo.attack(venture)
venture.attack(echo)


while echo.health > 0 and venture.health > 0:
    echo.attack(venture)
    if venture.health <= 0:
        print(f" {echo.name} wins!")
        break
    venture.attack(echo)
    if echo.health <= 0:
        print(f"{venture.name} wins!")
        break
echo.heal(200)
