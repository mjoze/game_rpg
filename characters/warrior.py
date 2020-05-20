from tools import name_generator as ng
from tools import equipment_generator as eg
import random


class Warrior:

    health = 10
    energy = 10

    def __init__(self, character='human', sex="gender", name='Anonymous', equipment=""):
        self.character = character
        self.sex = sex
        self.name = name
        self.equipment = equipment

    def __repr__(self):
        return 'race: {} - sex: {} - name: {} - health: {} - energy: {} - equipment: {}'.format(self.character,
                                                                                                self.sex,
                                                                                                self.name,
                                                                                                self.health,
                                                                                                self.energy,
                                                                                                self.equipment)

    def generate_character(self):
        characters = ['human', 'elf', 'ork']
        print('Available characters:')
        for i in characters:
            print(i)
        _character = input('Select character').lower()
        if _character in characters:
            print("your choice is" + _character)
            self.character = _character
        else:
            print("not available, random choice")
            self.character = characters[random.randrange(len(characters))]
        sex = ['male', 'female']
        for i in sex:
            print(i)
        _sex = input("Select sex")
        if _sex in sex:
            self.sex = _sex
        else:
            print("not available, random choice")
            self.sex = sex[random.randrange(len(sex))]

    def type_name(self):
        _name = input("What is your name?")
        self.name = _name

    def generate_name(self):

        if self.sex == "female":
            self.name = ng.generate_women()
        elif self.sex == "male":
            self.name = ng.generate_men()

    def generate_equipment(self):
        self.equipment = eg.equipment_generator()


if __name__ == "__main__":
    print("It's warrior class")