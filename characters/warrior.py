from tools import name_generator as ng
import random


class Warrior:

    health = 10

    def __init__(self, character='human', sex="gender", name='Anonymous'):
        self.character = character
        self.sex = sex
        self.name = name

    def __repr__(self):
        return 'race: {} - sex: {} - name: {} - health: {}'.format(self.character, self.sex, self.name, self.health)

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


if __name__ == "__main__":
    print("It's warrior class")