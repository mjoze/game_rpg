import random


def generate_women():
    female_names = ["Daisy", "Monica", "Anna", "Lisa"]
    return random.randrange(len(female_names))


def generate_men():
    male_names = ["Mark", "Scott", "Brian", "Peter"]
    return random.randrange(len(male_names))


if __name__ == "__main__":
    print("Name generator")
