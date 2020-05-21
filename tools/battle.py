def battle(player, enemy):
    while True:
        print("Do you want to fight? ")
        decision = input("YES/NO?").lower()
        if decision == "yes":
            if player.health > 0:
                print("Players attack")
                a = player.fight()
                enemy.get_injured(a)
                print("enemy HP:", enemy.health)
            else:
                print("player is dead")
                return
            if enemy.health > 0:
                print("Enemies attack")
                b = enemy.attack()
                player.get_injured(b)
                print("player HP:", player.health)
            else:
                print("enemy is dead")
                player.energy += 10
                return player
        elif decision == "no":
            print("it is bad choice. i run away")
            return
        else:
            print("run away you coward")
            return
