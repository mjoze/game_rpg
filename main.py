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


def player_options(player):
    # player options

    while player.health > 0 and player.energy > 0:
        print("||||    Place in city    ||||")
        for i in places:
            print(i)
        print("Quit -- press 'q'")
        print("Player Statistics -- press 's'")
        choice = input("-- Your place?").lower()
        if choice == 'church':
            if place_church.mission_goal == 1:
                print("Church not available")
            else:
                if place_church.god_strength > 0:
                    handle_places_church()
        elif choice == 'gymnasion':
            if place_gymnasion.mission_goal == 1:
                print("gymnasion not available")
            else:
                handle_places_gymnasion(place_gymnasion, player)
        elif choice == "q":
            return
        elif choice == "s":
            show_player_stats(player)
        else:
            print("breakdance")


def show_player_stats(_player):
    print("energy: {}. Hp: {}. equipment: {}.".format(_player.energy, _player.health, _player.equipment))


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
            return place_church.mission(player)
        elif decision == "q":
            return
        else:
            print("breakdance")
        return player


def handle_places_gymnasion(_place_gymnasion, _player):
    print(player)
    if _place_gymnasion.mission_goal == 0:
        print("You are in gymnasion. You can train or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "quest":
            print("misja")
            return _place_gymnasion.mission(_player)
        elif decision == "train":
            return _place_gymnasion.up_energy(_player)
        elif decision == "q":
            return
        else:
            print("breakdance")


player = create_player()
player_options(player)


def start_game():
    pass


def continue_game():
    pass


def save_game():
    pass


def quit_game():
    pass


