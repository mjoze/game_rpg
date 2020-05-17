class Church:

    energy = 4
    god_strength = 20

    def __init__(self):
        pass

    def __repr__(self):
        return "Church -- you can pray to heal. God strength = {}".format(self.god_strength) if self.god_strength > 0\
            else "empty church without god. No options"

    def pray(self, hero):
        print("Your prayers have been answered: HP + 10")
        self.god_strength -= 5
        if self.god_strength <= 0:
            print("god is dead. Church is collapse")
        else:
            print(self.god_strength)
            return hero.up_health(10)

    def god_up(self, god_health):
        self.god_strength += god_health
