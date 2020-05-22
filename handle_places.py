
def handle_places_church(new_place_church, new_player):
    # church

    while new_place_church.god_strength == 0:

        print("You can walk to church, pray or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "walk":
            new_player.walk(new_place_church)
        elif decision == "pray":
            new_place_church.pray(new_player)
        elif decision == "quest":
            print("misja")
            return new_place_church.mission(new_player)
        elif decision == "q":
            return
        else:
            print("unknown choice")
        return new_player


def handle_places_gymnasion(new_place_gymnasion, new_player):
    print(new_player)
    while new_place_gymnasion.mission_goal == 0:
        print("You are in gymnasion. You can train or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return new_place_gymnasion.mission(new_player)
        elif decision == "train":
            new_place_gymnasion.up_energy(new_player)
        elif decision == "q":
            return False
        else:
            print("unknown choice")


def handle_places_saloon(new_place_saloon, new_player):
    while new_place_saloon.mission_goal == 0:
        print("You are in saloon. You can drink or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return new_place_saloon.mission()
        elif decision == "drink":
            new_place_saloon.drink()
        elif decision == "q":
            return
        else:
            print("unknown choice")
