from characters import warrior


class Player(warrior.Warrior):

    def __init__(self):
        super().__init__()

    def get_injured(self, injured):
        if self.health <= 0:
            print("dead")
        else:
            self.health -= injured

    def walk(self, place):
        print(place)
        self.energy -= place.energy

    def up_health(self, _health):
        self.health += _health

    def fight(self):
        print("fight")
