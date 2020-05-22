import create_player
import handle_places
from places.city import church, gymnasion, saloon
from src import places_ascii


def player_options(new_player, new_places, new_place_church, new_place_gymnasion, new_place_saloon):
    # player options

    while new_player.health > 0 and new_player.energy > 0:
        print("||||    Place in city    ||||")
        print(places_ascii.city())
        print("#################################")
        for i in new_places:
            print(i)
        print("#################################")
        print("Quit -- press 'q'")
        print("Player Statistics -- press 's'")
        choice = input("-- Your place?").lower()
        if choice == 'church':
            if new_place_church.mission_goal == 1:
                print("Church not available")
            else:
                if new_place_church.god_strength > 0:
                    print(places_ascii.church_ascii())
                    handle_places.handle_places_church(new_place_church, new_player)
        elif choice == 'gymnasion':
            if new_place_gymnasion.mission_goal == 1:
                print("gymnasion not available")
            else:
                print(places_ascii.gymnasion_ascii())
                handle_places.handle_places_gymnasion(new_place_gymnasion, new_player)
        elif choice == "saloon":
            if new_place_saloon.mission_goal == 1:
                print("gymnasion not available")
            else:
                handle_places.handle_places_saloon(new_place_saloon, new_player)
        elif choice == "q":
            return
        elif choice == "s":
            handle_player_stats(new_player)
        else:
            print("unknown choice")


def handle_player_stats(new_player):
    print("energy: {}. Hp: {}. equipment: {}.".format(new_player.energy, new_player.health, new_player.equipment))


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



