from characters import warrior, Player
import random


class Enemy():

    dificcult = random.randint(1, 3)
    health = 4 * dificcult
    power = 2 * dificcult

    def __init__(self, name, race, sex):
        self.name = name
        self.race = race
        self.sex = sex

    def get_injured(self, injured):
        if self.health <= 0:
            print("dead")
        else:
            self.health = self.health - injured

    def attack(self):
        print("Attack power:", self.power)
        return self.power




