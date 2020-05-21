
def handle_places_church(_place_church, _player):
    # church

    while _place_church.god_strength > 0:

        print("You can walk to church, pray or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "walk":
            _player.walk(place_church)
        elif decision == "pray":
            _place_church.pray(_player)
        elif decision == "quest":
            print("misja")
            return _place_church.mission(_player)
        elif decision == "q":
            return
        else:
            print("unknown choice")
        return _player


def handle_places_gymnasion(_place_gymnasion, _player):
    print(_player)
    while _place_gymnasion.mission_goal == 0:
        print("You are in gymnasion. You can train or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return _place_gymnasion.mission(_player)
        elif decision == "train":
            _place_gymnasion.up_energy(_player)
        elif decision == "q":
            return False
        else:
            print("unknown choice")


def handle_places_saloon(_place_saloon, _player):
    while _place_saloon.mission_goal == 0:
        print("You are in saloon. You can drink or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return _place_saloon.mission()
        elif decision == "drink":
            _place_saloon.drink()
        elif decision == "q":
            return
        else:
            print("unknown choice")
