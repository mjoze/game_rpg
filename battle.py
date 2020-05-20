from characters import Enemy, Player


def battle(player, enemy):
    while player.health > 0:

        print("Players attack")
        a = player.fight()
        enemy.get_injured(a)
        print("enemy HP:",enemy.health)

        print("Enemies attack")
        b = enemy.attack()
        player.get_injured(b)
        print("player HP:", player.health)
