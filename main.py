from characters import Player
from places.city import church

# create places
place_church = church.Church()
places = [place_church]


def create_player():

    # create player
    print("Create a new player")
    player = Player.Player()
    player.generate_character()
    player.type_name()
    player.generate_equipment()
    print(player)
    return player


def player_options():
    # player options
    print("place in city")
    for i in places:
        print(i)


def handle_places_church():
    # church
    print("You can walk to church and pray. ")

    while place_church.god_strength > 0:
        decision = input('What is your decision.').lower()
        if decision == "walk":
            player.walk(place_church)
        elif decision == "pray":
            place_church.pray(player)
        print(player)


player = create_player()
handle_places_church()


def continue_game():
    pass


def save_game():
    pass


def quit_game():
    pass


