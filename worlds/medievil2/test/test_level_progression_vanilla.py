"""
Regression tests for set_vanilla_level_progression in Rules.py (default progression_option
and keyitemsanity off). None of the "Cleared: X" locations have any item gating in this
mode (set_item_rules is only called when keyitemsanity is on), so the entire chain reduces
to pure region reachability plus the single has_dan_hand_skill check gating Greenwich
Observatory.
"""

from . import Medievil2TestBase


class VanillaLevelProgressionTest(Medievil2TestBase):
    def test_chain_only_requires_dan_hand(self) -> None:
        for entrance in (
            "Menu -> The Museum",
            "The Museum -> Tyrannosaurus Wrecks",
            "Tyrannosaurus Wrecks -> Hub",
            "Hub -> Tyrannosaurus Wrecks",
            "Hub -> Kensington",
            "Kensington -> The Tomb",
            "Hub -> The Freakshow",
        ):
            with self.subTest(entrance=entrance):
                self.assertTrue(self.can_reach_entrance(entrance))

        self.assertFalse(self.can_reach_entrance("Hub -> Greenwich Observatory"))
        self.collect_by_name("Dan Hand")
        self.assertTrue(self.can_reach_entrance("Hub -> Greenwich Observatory"))

        for entrance in (
            "Greenwich Observatory -> Greenwich, Naval Academy",
            "Hub -> Kew Gardens",
            "Hub -> Dankenstein",
            "Dankenstein -> Iron Slugger",
            "Hub -> Iron Slugger",
            "Hub -> Wulfrum Hall",
            "Wulfrum Hall -> The Count",
            "Hub -> The Count",
            "Hub -> Whitechapel",
            "Hub -> The Sewers",
            "Hub -> The Time Machine",
            "The Time Machine -> The Time Machine, The Sewers",
            "The Time Machine, The Sewers -> The Ripper",
            "Hub -> Cathedral Spires",
            "Cathedral Spires -> Cathedral Spires, The Descent",
            "Hub -> The Demon",
        ):
            with self.subTest(entrance=entrance):
                self.assertTrue(self.can_reach_entrance(entrance))

        self.assertBeatable(True)

    def test_greenwich_observatory_is_the_only_gate_in_the_whole_chain(self) -> None:
        self.assertFalse(self.can_reach_region("Greenwich Observatory"))
        self.assertFalse(self.can_reach_region("Greenwich, Naval Academy"))
        self.assertFalse(self.can_reach_entrance("Hub -> The Demon"))
        self.collect_by_name("Dan Hand")
        self.assertTrue(self.can_reach_entrance("Hub -> The Demon"))
