from characters import Player
from places.city import church, gymnasion


# create places
place_church = church.Church()
place_gymnasion = gymnasion.Gymnasion()
places = [place_church, place_gymnasion]


def create_player():

    # create player
    print("Create a new player")
    player = Player.Player()
    player.generate_character()
    # player.type_name()
    player.generate_name()
    player.generate_equipment()
    print(player)
    return player


def player_options():
    # player options

    while player.health > 0 and player.energy > 0:
        print("||||    Place in city    ||||")
        for i in places:
            print(i)
        choice = input("-- Your place?")
        if choice == 'church':
            if place_church.mission_goal == 1:
                print( "Church not available")
            else:
                if place_church.god_strength > 0:
                    handle_places_church()
        elif choice == 'gymnasion':
            if place_church.mission_goal == 1:
                print( "gymnasion not available")
            else:
                handle_places_gymnasion()
        else:
            print("breakdance")


def handle_places_church():
    # church

    while place_church.god_strength > 0:

        print("You can walk to church, pray or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "walk":
            player.walk(place_church)
        elif decision == "pray":
            place_church.pray(player)
        elif decision == "quest":
            print("misja")
            return place_church.mission()
        elif decision == "q":
            return
        else:
            print("breakdance")
        print(player)


def handle_places_gymnasion():
    print(player)
    if place_gymnasion.mission_goal == 0:
        print("You are in gymnasion. You can train or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return place_gymnasion.mission()
        elif decision == "q":
            return
        else:
            print("breakdance")


player = create_player()
player_options()
# handle_places_gymnasion()


def continue_game():
    pass


def save_game():
    pass


def quit_game():
    pass


