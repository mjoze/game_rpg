import random


def equipment_generator():
    armor = {'Axe': 5, 'Sword': 6, 'Stick': 2}
    random_armor = random.choice(list(armor.items()))
    return random_armor


