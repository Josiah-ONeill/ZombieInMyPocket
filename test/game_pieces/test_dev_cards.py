from unittest import TestCase
from src.common.interfaces import IItem, IEncounter
from src.model.game_pieces import GamePieces
from src.model.game_time.game_time import GameTime

NUMBER_OF_CARDS = 8

class TestDevCards(TestCase):

    def setUp(self) -> None:
        self.time = GameTime()
        self.game_pieces = GamePieces(self.time)

    def test_starts_with_nine_dev_cards(self):
        expected = NUMBER_OF_CARDS
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_dev_card_removes_from_deck(self):
        self.game_pieces.draw_dev_card()
        expected = NUMBER_OF_CARDS - 1
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_last_card_reshuffles_deck(self):
        for _ in range(NUMBER_OF_CARDS):
            self.game_pieces.draw_dev_card()

        expected = 0
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

        self.game_pieces.draw_dev_card()
        expected = NUMBER_OF_CARDS - 1
        actual = self.game_pieces.dev_cards_remaining()
        self.assertEqual(expected, actual)

    def test_draw_last_card_increases_time(self):
        for _ in range(NUMBER_OF_CARDS):
            self.game_pieces.draw_dev_card()
        
        expected = 9
        actual = self.time.get_current_time()
        self.assertEqual(expected, actual)

        self.game_pieces.draw_dev_card()
        expected = 10
        actual = self.time.get_current_time()
        self.assertEqual(expected, actual)
    
    def test_get_item(self):
        the_card = self.game_pieces.draw_dev_card()
        the_item = the_card.get_item()
        self.assertTrue(isinstance(the_item, IItem))

    def test_get_encounter(self):
        the_card = self.game_pieces.draw_dev_card()
        the_encounter = the_card.get_encounter(9)
        self.assertTrue(isinstance(the_encounter, IEncounter))


