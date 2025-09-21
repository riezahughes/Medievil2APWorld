def defeat_demon_victory(self, state):
    return state.can_reach_location("Cleared: The Demon", self.player)
