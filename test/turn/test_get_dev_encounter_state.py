import unittest
from unittest.mock import create_autospec

from src.model.turn.turn_common import Triggers, ServiceMethods, ServiceNames
from src.model.turn.turn_flow import TurnFlow
from src.model.turn.turn_states import GetDevEncounter

class TestGetDevEncounterState(unittest.TestCase):
    def setUp(self):
        self.the_turn = create_autospec(TurnFlow)
        self.the_state = GetDevEncounter()
        self.the_state.context = self.the_turn
        self.the_state.enter()

    
    def test_enterd(self):
        self.assertEqual(self.the_state.trigger, Triggers.RUN_ENCOUNTER)


    def test_request(self):
        self.the_state.handle_request()
        calls = self.the_turn.call_service_method.call_args_list

        self.assertEqual(calls[0][0], (ServiceNames.GAME_PIECES, ServiceMethods.DRAW_DEV_CARD))
        self.assertEqual(calls[1][0], (ServiceNames.GAME_TIME, ServiceMethods.GET_CURRENT_TIME))
        self.assertEqual(self.the_turn.call_service_method.call_count, 2)