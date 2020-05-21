import create_player
import handle_places
from places.city import church, gymnasion, saloon
from src import places_ascii


def player_options(_player, _places, _place_church, _place_gymnasion, _place_saloon):
    # player options

    while _player.health > 0 and _player.energy > 0:
        print("||||    Place in city    ||||")
        print(places_ascii.city())
        print("#################################")
        for i in places:
            print(i)
        print("#################################")
        print("Quit -- press 'q'")
        print("Player Statistics -- press 's'")
        choice = input("-- Your place?").lower()
        if choice == 'church':
            if _place_church.mission_goal == 1:
                print("Church not available")
            else:
                if _place_church.god_strength > 0:
                    print(places_ascii.church_ascii())
                    handle_places.handle_places_church(_place_church, _player)
        elif choice == 'gymnasion':
            if _place_gymnasion.mission_goal == 1:
                print("gymnasion not available")
            else:
                print(places_ascii.gymnasion_ascii())
                handle_places.handle_places_gymnasion(_place_gymnasion, _player)
        elif choice == "saloon":
            if _place_saloon.mission_goal == 1:
                print("gymnasion not available")
            else:
                handle_places.handle_places_saloon(_place_saloon, _player)
        elif choice == "q":
            return
        elif choice == "s":
            handle_player_stats(_player)
        else:
            print("unknown choice")


def handle_player_stats(_player):
    print("energy: {}. Hp: {}. equipment: {}.".format(_player.energy, _player.health, _player.equipment))


# create places
place_church = church.Church()
place_gymnasion = gymnasion.Gymnasion()
place_saloon = saloon.Saloon()
places = [place_church, place_gymnasion, place_saloon]
# create player
player = create_player.create_player()
# game
if player:
    player_options(player, places, place_church, place_gymnasion, place_saloon)



