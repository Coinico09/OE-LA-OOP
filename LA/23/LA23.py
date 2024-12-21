class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper

tanjiro = AnimeCharacter("tanjiro", "water breathing style")

@tanjiro.introduce
def character_intro():
    print(f"I am {tanjiro.name} and I can use {tanjiro.ability}.")

character_intro()
