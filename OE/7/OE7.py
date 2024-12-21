class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper

noctis = TekkenCharacter("noctis", "blizzard spike")

@noctis.introduce
def character_intro():
    print(f"I am {noctis.name} and I can use {noctis.ability}.")

character_intro()
