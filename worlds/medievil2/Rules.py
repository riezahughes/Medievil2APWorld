from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState, Iterable
from .Options import IncludeChalicesInChecksToggle


def is_level_cleared(self, location: str, state: CollectionState):
    return state.can_reach_location("Cleared: " + location, self.player)


def is_boss_defeated(self, boss: str, state: CollectionState):  # can used later
    return state.has("Boss: " + boss, self.player, 1)


def has_keyitems_required(self, items: list[str], state: CollectionState):
    passed_check = True
    for item in items:
        if state.has("Key Item: " + item, self.player, 1) is False:
            passed_check = False
    return passed_check


def set_vanilla_level_progression(self):
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Menu", state))
    set_rule(self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), lambda state: is_level_cleared(self, "The Museum", state))
    set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Hub", state))
    set_rule(self.get_entrance("Hub -> Tyrannosaurus Wrecks"), lambda state: is_level_cleared(self, "The Museum", state))
    set_rule(self.get_entrance("Hub -> Kensington"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(self.get_entrance("Kensington -> The Tomb"), lambda state: is_level_cleared(self, "Kensington", state))
    set_rule(self.get_entrance("Hub -> The Freakshow"), lambda state: is_level_cleared(self, "The Tomb", state))
    set_rule(self.get_entrance("Hub -> Greenwich Observatory"), lambda state: is_level_cleared(self, "The Freakshow", state))
    set_rule(
        self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), lambda state: is_level_cleared(self, "Greenwich Observatory", state)
    )
    set_rule(self.get_entrance("Hub -> Kew Gardens"), lambda state: is_level_cleared(self, "Naval Academy", state))
    set_rule(self.get_entrance("Hub -> Dankenstein"), lambda state: is_level_cleared(self, "Kew Gardens", state))
    set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Hub -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Hub -> Wulfrum Hall"), lambda state: is_level_cleared(self, "Iron Slugger", state))
    set_rule(self.get_entrance("Wulfrum Hall -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("Hub -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("Hub -> Whitechapel"), lambda state: is_level_cleared(self, "The Count", state))
    set_rule(self.get_entrance("Hub -> The Sewers"), lambda state: is_level_cleared(self, "Whitechapel", state))
    set_rule(self.get_entrance("Hub -> The Time Machine"), lambda state: is_level_cleared(self, "The Sewers", state))
    set_rule(self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), lambda state: is_level_cleared(self, "The Time Machine", state))
    set_rule(
        self.get_entrance("The Time Machine, The Sewers -> The Ripper"), lambda state: is_level_cleared(self, "The Time Machine, The Sewers", state)
    )
    set_rule(self.get_entrance("Hub -> Cathedral Spires"), lambda state: is_level_cleared(self, "The Ripper", state))
    set_rule(self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"), lambda state: is_level_cleared(self, "Cathedral Spires", state))
    set_rule(self.get_entrance("Hub -> The Demon"), lambda state: is_level_cleared(self, "Cathedral Spires, The Descent", state))
