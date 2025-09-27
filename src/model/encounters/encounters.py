# Modified by David Watts to prevent errors in testing

from abc import ABC, abstractmethod

from ..interfaces.i_encounter import IEncounter
from ..interfaces.i_player import IPlayer

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self, value):
        self.health = value

    def handle_encounter(self, player) -> IPlayer:
        player.heal(self.health)
        return player

class CowerEncounter(IEncounter):
    """Handles Cower Encounter"""
    HEALTH_INCREASE = 3

    def __init__(self):
        self.health_increase = self.HEALTH_INCREASE

    def handle_encounter(self, player) -> IPlayer:
        player.heal(self.health_increase)
        return player

class CombatEncounter(IEncounter):
    """Handles Combat Encounters"""
    MAX_DAMAGE = 4
    MIN_DAMAGE = 0

    def __init__(self, value):
        self.zombies = value

    def handle_encounter(self, player) -> IPlayer:
        damage = self.zombies - player.get_attack_power()
        if damage > self.MAX_DAMAGE:
            damage = self.MAX_DAMAGE
        elif damage < self.MIN_DAMAGE:
            damage = self.MIN_DAMAGE
        player.take_damage(damage)
        return player
        
class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self, new_item):
        self.item = new_item

    def handle_encounter(self, player) -> IPlayer:
        player.add_item_to_inventory(self.item)
        return player

class MessageEncounter(IEncounter):
    """Handles Message Encounters"""
    def __init__(self, new_code):
        self.message_code = new_code

    def handle_encounter(self, player) -> IPlayer:
        pass

class TotemEncounter(IEncounter):
    """Handles Totem Encounters"""
    def __init__(self, new_totem_state):
        self.totem_state = new_totem_state

    def handle_encounter(self, player) -> IPlayer:
        # player.setTotem??
        # return player
        pass