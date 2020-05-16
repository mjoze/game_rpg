from characters import warrior


class Player(warrior.Warrior):

    def __init__(self):
        super().__init__()

    def get_injured(self, injured):
        self.health -= injured

    def walk(self, place):
        self.energy -= place.energy

    def up_health(self, _health):
        self.health += _health
