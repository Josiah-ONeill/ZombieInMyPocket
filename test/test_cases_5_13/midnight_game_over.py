import unittest
from src.enums_and_types import GameOverReason
from src.model.game_over import GameOver
from src.model.game_time import GameTime
from src.model.interfaces import IGameOver

class MidnightGameOver(unittest.TestCase):
    """
    Midnight loss condition is enforced
    • Given the time reaches midnight
    • When checking the game status
    • Then the game ends and the player loses
    """
    def setUp(self):
        self.game_over: IGameOver = GameOver()
        self.expected_reason = GameOverReason.OUT_OF_TIME

    def test_time_condition_false(self):
        game_time = GameTime()
        game_time.increase_current_time()
        game_time.increase_current_time()
        expected_state = game_time.is_time_valid()
        self.assertEqual(expected_state, True)

    def test_time_condition_true(self):
        game_time = GameTime()
        game_time.increase_current_time()
        game_time.increase_current_time()
        game_time.increase_current_time()
        expected_state = game_time.is_time_valid()
        self.assertEqual(expected_state, False)

if __name__ == '__main__':
    unittest.main()