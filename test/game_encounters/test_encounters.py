import unittest

from src.common import ItemName
from src.model import Player
from src.model.item import get_item
from src.model.encounters import *


class TestEncounters(unittest.TestCase):
    def setUp(self):
        self.player = Player(initial_health=4)
        self.not_player = None
    

    @staticmethod
    def run_encounter(encounter, player, vaule=None):
        if vaule is not None:
            the_encunter = encounter(vaule)
        else:
            the_encunter = encounter()
        the_encunter.handle_encounter(player)


    def test_health_happy_day(self):
        self.run_encounter(HealthEncounter, self.player, 2)
        self.assertEqual(self.player.get_health(), 6)


    def test_health_bad_day(self):
        with self.assertRaises(TypeError) as context:
            self.run_encounter(HealthEncounter, self.not_player, 2)

    def test_cower_happy_day(self):
        self.run_encounter(CowerEncounter, self.player)
        self.assertEqual(self.player.get_health(), 7)


    def test_cower_bad_day(self):
        with self.assertRaises(TypeError) as context:
            self.run_encounter(CowerEncounter, self.not_player)


    def test_combat_happy_day(self):
        self.run_encounter(CombatEncounter, self.player, 3)
        self.assertEqual(self.player.get_health(), 2)
    

    def test_combat_bad_day(self):
        with self.assertRaises(TypeError) as context:
            self.run_encounter(CombatEncounter, self.not_player, 3)
    

    def test_combat_max_damage(self):
        self.player.heal(1) #toatal health = 5
        self.run_encounter(CombatEncounter, self.player, 6)
        #player should loss 4 health
        self.assertEqual(self.player.get_health(), 1)


    def test_combat_min_damage(self):
        self.run_encounter(CombatEncounter, self.player, -1)
        self.assertEqual(self.player.get_health(), 4)


    def test_item_happy_day(self):
        self.run_encounter(ItemEncounter, self.player, get_item(ItemName.GOLF_CLUB))
        self.assertEqual(self.player.get_inventory()[0].name, get_item(ItemName.GOLF_CLUB).name)
    

    def test_item_bad_day(self):
        with self.assertRaises(TypeError) as context:
            self.run_encounter(ItemEncounter, self.not_player, get_item(ItemName.GOLF_CLUB))


    # def test_message(self):
    #     message = MessageEncounter(1)
    #     message.handle_encounter(self.player)
    #     self.assertEqual(1, 1)


    # def test_totem(self):
    #     totem = TotemEncounter(True)
    #     totem.handle_encounter(self.player)
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
