from characters import Player
from places.city import church, gymnasion


def create_player():

    # create player
    decision = input("Create a new player? YES/NO").lower()
    if decision == 'yes':
        _player = Player.Player()
        _player.generate_character()
        # player.type_name()
        _player.generate_name()
        _player.generate_equipment()
        print(_player)
        return _player
    elif decision == 'no':
        print("No player, no game!")
        return False
    else:
        create_player()


def player_options(_player, _places, _place_church, _place_gymnasion):
    # player options

    while _player.health > 0 and _player.energy > 0:
        print("||||    Place in city    ||||")
        for i in places:
            print(i)
        print("Quit -- press 'q'")
        print("Player Statistics -- press 's'")
        choice = input("-- Your place?").lower()
        if choice == 'church':
            if _place_church.mission_goal == 1:
                print("Church not available")
            else:
                if _place_church.god_strength > 0:
                    handle_places_church(_place_church, _player)
        elif choice == 'gymnasion':
            if _place_gymnasion.mission_goal == 1:
                print("gymnasion not available")
            else:
                _handle_places_gymnasion(_place_gymnasion, _player)
        elif choice == "q":
            return
        elif choice == "s":
            show_player_stats(_player)
        else:
            print("unknown choice")


def show_player_stats(_player):
    print("energy: {}. Hp: {}. equipment: {}.".format(_player.energy, _player.health, _player.equipment))


def handle_places_church(_place_church, _player):
    # church

    while _place_church.god_strength > 0:

        print("You can walk to church, pray or get quest.  ")
        decision = input('What is your decision? Or press "q" to quit').lower()
        if decision == "walk":
            _player.walk(place_church)
        elif decision == "pray":
            _place_church.pray(player)
        elif decision == "quest":
            print("misja")
            return _place_church.mission(player)
        elif decision == "q":
            return
        else:
            print("unknown choice")
        return _player


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
            print("unknown choice")


# create places
place_church = church.Church()
place_gymnasion = gymnasion.Gymnasion()
places = [place_church, place_gymnasion]
# create player
player = create_player()
# game
if player:
    player_options(player, places, place_church, place_gymnasion)



