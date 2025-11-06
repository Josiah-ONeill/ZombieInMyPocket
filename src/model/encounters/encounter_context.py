


class EncounterContext:
    def __init__(self, player):
        self.player = player
        self.current_encounter = None

    def handle_encounter(self):
        if self.current_encounter is not None:
            self.current_encounter.handle_encounter(self.player)

    def set_encounter(self, encounter):
        self.current_encounter = encounter

    def unset_encounter(self):
        self.current_encounter = None