import unittest

from Player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()

    def testEmptyEquipment(self):
        self.assertEqual(self.player.equipment, "")

    def testInjured(self):
        health = self.player.health
        damage = 1
        self.player.get_injured(damage)
        self.assertEqual(self.player.health, health - damage)