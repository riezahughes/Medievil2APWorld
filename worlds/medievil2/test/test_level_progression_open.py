"""
Regression tests for set_open_world_progression in Rules.py. When keyitemsanity is off, it
only ever sets rules on sub-area connections within a level chain (e.g. Museum ->
Tyrannosaurus Wrecks, Dankenstein -> Iron Slugger); it never touches any "Hub -> X" entrance
at all (not even Greenwich Observatory's has_dan_hand_skill check that vanilla mode has),
and "Cleared: X" locations have no item gating either. So with keyitemsanity off, every
"Hub -> X" entrance -- including "Hub -> The Museum", which had to be explicitly fixed to
stop referencing a nonexistent "Cleared: Menu" location -- is unconditionally open, and the
whole game is beatable with zero items.

Note: set_open_world_progression only overrides a handful of specific entrances regardless
of keyitemsanity. If keyitemsanity is also on, set_keyitemsanity_progression's own "Hub ->
X" rules are NOT overridden by open mode (open mode never touches most "Hub -> X" entrances
at all), so most of the game stays exactly as gated as in vanilla + keyitemsanity. See
test_keyitemsanity_progression.py for that behavior.
"""

from . import Medievil2TestBase
from ..Options import ProgressionOptions


class OpenLevelProgressionTest(Medievil2TestBase):
    options = {
        "progression_option": ProgressionOptions.OPEN,
    }

    def test_every_hub_entrance_is_unconditionally_open(self) -> None:
        for entrance in (
            "Hub -> The Museum",
            "Hub -> Kensington",
            "Hub -> The Freakshow",
            "Hub -> Greenwich Observatory",
            "Hub -> Kew Gardens",
            "Hub -> Dankenstein",
            "Hub -> Iron Slugger",
            "Hub -> Wulfrum Hall",
            "Hub -> The Count",
            "Hub -> Whitechapel",
            "Hub -> The Sewers",
            "Hub -> The Time Machine",
            "Hub -> Cathedral Spires",
            "Hub -> The Demon",
        ):
            with self.subTest(entrance=entrance):
                self.assertTrue(self.can_reach_entrance(entrance))
        self.assertBeatable(True)
