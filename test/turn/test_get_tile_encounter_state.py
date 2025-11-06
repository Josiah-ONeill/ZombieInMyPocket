import unittest
from unittest.mock import create_autospec

from src.common import IEncounter, Direction
from src.model.turn.turn_common import Triggers
from src.model.turn.turn_flow import TurnFlow
from src.model.turn.turn_states import GetTileEncounter
from src.model.game_pieces import Tile

class TestGetTileEncounterState(unittest.TestCase):
    def setUp(self):
        self.the_turn = create_autospec(TurnFlow)
        self.the_encouter = create_autospec(IEncounter)
        self.the_state = GetTileEncounter()
        self.the_state.context = self.the_turn

        self.tile_with_encounter = self.family_room_tile = Tile(
            "Family Room",
            False,
            (Direction.WEST, Direction.NORTH, Direction.EAST),
            None,
            self.the_encouter
        )

        self.tile_without_encounter = self.family_room_tile = Tile(
            "Family Room",
            False,
            (Direction.WEST, Direction.NORTH, Direction.EAST),
            None,
            None
        )

        
    
    def test_enterd(self):
        self.the_state.enter(self.tile_with_encounter)
        self.assertEqual(self.the_state.trigger, Triggers.RUN_ENCOUNTER)

    
    def test_exit_with_encounter(self):
        self.the_state.enter(self.tile_with_encounter)
        self.the_state.handle_request()
        call = self.the_turn.state_finished.call_args_list[0][0]
        print(call)
        the_trigger = call[0]
        the_result = call[1]

        #exit with the trigger to run the encounter
        self.assertEqual(the_trigger, Triggers.RUN_ENCOUNTER)

        #pass the encounter to the next state
        self.assertEqual(the_result[0], self.the_encouter)

        #pass the trigger to end the encounter to the next state
        self.assertEqual(the_result[1], Triggers.TILE_ENCOUNTER_END)

        #only called once
        self.assertEqual(self.the_turn.state_finished.call_count, 1)


    def test_exit_without_encounter(self):
        self.the_state.enter(self.tile_without_encounter)
        self.the_state.handle_request()
        call = self.the_turn.state_finished.call_args_list[0][0]
        print(call)
        the_trigger = call[0]
        the_result = call[1]

        #exit with the trigger to run the encounter
        self.assertEqual(the_trigger, Triggers.TILE_ENCOUNTER_END)

        #pass no args to the next state
        self.assertIsNone(the_result)

        #only called once
        self.assertEqual(self.the_turn.state_finished.call_count, 1)

    