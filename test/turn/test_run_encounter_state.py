import unittest
from unittest.mock import create_autospec

from src.common.interfaces import IEncounter
from src.model.turn.turn_flow import TurnFlow
from src.model.turn.turn_common import Triggers
from src.model.turn.turn_states import RunEncounter
from src.model.encounters import HealthEncounter

class TestRunEncounterState(unittest.TestCase):
    def setUp(self):
        self.the_turn = create_autospec(TurnFlow)
        self.the_encounter = create_autospec(HealthEncounter)
        self.the_state = RunEncounter()
        self.the_state.context = self.the_turn
        self.the_state.enter(self.the_encounter, Triggers.DEV_ENCOUNTER_END)


    def test_enterd(self):
        self.assertTrue(isinstance(self.the_state._encounter, IEncounter))
        self.assertEqual(self.the_state.trigger, Triggers.DEV_ENCOUNTER_END)


    def test_encounter_called(self): 
        self.the_state.handle_request()
        self.assertEqual(self.the_encounter.handle_encounter.call_count, 1)

    def test_exit(self): 
        self.the_state.handle_request()
        self.the_turn.state_finished.assert_called_with(
            Triggers.DEV_ENCOUNTER_END, (Triggers.START_TILE_ENCOUNTER, )
            )

