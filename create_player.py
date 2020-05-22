from characters import Player


def create_player():

    # create player
    decision = input("Create a new player? YES/NO").lower()
    if decision == 'yes':
        new_player = Player.Player()
        new_player.generate_character()
        # player.type_name()
        new_player.generate_name()
        new_player.generate_equipment()
        print(new_player)
        return new_player
    elif decision == 'no':
        print("No player, no game!")
        return False
    else:
        create_player()

