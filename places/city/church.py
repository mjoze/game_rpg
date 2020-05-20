class Church:

    energy = 4
    god_strength = 20
    mission_goal = 0

    def __init__(self):
        pass

    def __repr__(self):
        return ("Church -- you can pray to heal. God strength = {}".format(self.god_strength) if self.god_strength > 0\
            else "empty church without god. No options") if self.mission_goal == 0 else "building not available"

    def pray(self, hero):
        print("Your prayers have been answered: HP + 10")
        self.god_strength -= 8
        if self.god_strength <= 0:
            print("god is dead. Church is collapse")
        else:
            print("God strength:", self.god_strength)
            print("HP:", hero.health)
            return hero.up_health(10)

    def god_up(self, god_health):
        self.god_strength += god_health

    def mission(self):
        print("Kill the evil god")
        self.mission_goal += 1

