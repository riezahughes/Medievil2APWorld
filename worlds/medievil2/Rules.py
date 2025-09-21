from BaseClasses import CollectionState


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
