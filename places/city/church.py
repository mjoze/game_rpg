from tools import battle
from characters.Enemy import Enemy


class Church:

    energy = 4
    god_strength = 20
    mission_goal = 0

    def __init__(self):
        pass

    def __repr__(self):
        return ("Church -- you can pray to heal. God strength = {}".format(self.god_strength) if self.god_strength > 0\
            else "empty church without god. No options") if self.mission_goal == 0 else "Church -- building not available"

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

    def mission(self, hero):
        print("Kill the evil god")
        god_enemy = Enemy("Zeus", "God", "male")
        battle.battle(hero, god_enemy)
        self.mission_goal += 1

