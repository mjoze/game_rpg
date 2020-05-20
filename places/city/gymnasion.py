class Gymnasion:

    mission_goal = 0

    def __init__(self):
        pass

    def __repr__(self):
        return "Gymnasion -- Place to up your energy" if self.mission_goal == 0 else "Gymnasion -- mission" \
                                                                                     " accomplished." \
                                                                                     " building not available"

    def up_energy(self, player):
        print("you train ")
        return player.up_energy(4)

    def mission(self):
        print("Kill the evil master")
        self.mission_goal += 1

