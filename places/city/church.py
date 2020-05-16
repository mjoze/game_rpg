class Church:

    energy = 4
    god_strength = 20

    def __init__(self):
        pass

    def __repr__(self):
        return "it's a church. you can pray to heal. God strength = {}".format(self.god_strength)

    def pray(self, hero):
        print("Your prayers have been answered: HP + 10")
        self.god_strength -= 5
        if self.god_strength <= 0:
            print("god is dead")
        else:
            return hero.up_health(10)

