from characters import Player


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

