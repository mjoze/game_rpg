class Church:

    def __init__(self):
        pass

    def __repr__(self):
        return "it's a church. you can pray to heal"

    def pray(self, hero):
        print("Your prayers have been answered: HP + 10")
        return hero.up_health(10)

