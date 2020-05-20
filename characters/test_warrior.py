import unittest

from warrior import Warrior
from tools.name_generator import generate_men, generate_women


class WarriorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.warrior = Warrior("male", "elf", "Mae", "ciupaga")

    def testGenerateCharacter(self):
        self.assertEqual(self.warrior.equipment, "ciupaga")

    def testGenerateName(self):
        self.warrior2 = Warrior(sex="male")
        name = self.warrior2.generate_name()
        self.warrior2.name = name
        self.assertEqual(self.warrior2.name, name)

    def testTypeName(self):
        self.warrior3 = Warrior()
        typing_name = self.warrior3.type_name()
        self.warrior3.name = typing_name
        self.assertEqual(self.warrior3.name, typing_name)