"""
Regression tests for set_keyitemsanity_progression in Rules.py (progression_option is
irrelevant here since Open mode never overrides most of these "Hub -> X" entrances -- see
test_level_progression_open.py). This also exercises the set_key_blocks fix: locations like
"Cleared: The Museum" must now require ALL of their listed items, not just the last one in
the list (the bug this replaced only checked the last item).
"""

from . import Medievil2TestBase


class KeyItemSanityProgressionTest(Medievil2TestBase):
    options = {
        "keyitemsanity": 1,
    }

    def test_museum_requires_all_four_items_not_just_the_last(self) -> None:
        self.assertFalse(self.can_reach_location("Cleared: The Museum"))
        self.collect_by_name(["Torch", "Cannon Ball", "Museum Key"])
        self.assertFalse(self.can_reach_location("Cleared: The Museum"))
        self.collect_by_name("Dinosaur Key")
        self.assertTrue(self.can_reach_location("Cleared: The Museum"))
        self.assertTrue(self.can_reach_entrance("The Museum -> Tyrannosaurus Wrecks"))

    def test_full_keyitemsanity_chain(self) -> None:
        self.collect_by_name(["Torch", "Cannon Ball", "Museum Key", "Dinosaur Key"])
        self.assertTrue(self.can_reach_entrance("The Museum -> Tyrannosaurus Wrecks"))
        self.assertTrue(self.can_reach_entrance("Tyrannosaurus Wrecks -> Hub"))
        self.assertTrue(self.can_reach_entrance("Hub -> Kensington"))

        self.assertFalse(self.can_reach_entrance("Kensington -> The Tomb"))
        self.collect_by_name(["Depot Key", "Town House Key", "Pocket Watch"])
        self.assertTrue(self.can_reach_entrance("Kensington -> The Tomb"))

        self.assertFalse(self.can_reach_entrance("The Tomb -> Hub"))
        self.collect_by_name(["Staff of Anubis", "Scroll of Sekhmet", "Tablet of Horus"])
        self.assertTrue(self.can_reach_entrance("The Tomb -> Hub"))

        self.assertFalse(self.can_reach_entrance("Hub -> The Freakshow"))
        self.collect_by_name(["Elephant Key 1", "Elephant Key 2"])
        self.assertTrue(self.can_reach_entrance("Hub -> The Freakshow"))

        self.assertFalse(self.can_reach_entrance("Hub -> Greenwich Observatory"))
        self.collect_by_name("Dan Hand")
        self.assertTrue(self.can_reach_entrance("Hub -> Greenwich Observatory"))

        self.assertFalse(self.can_reach_entrance("Greenwich Observatory -> Greenwich, Naval Academy"))
        self.collect_by_name("Bellows")
        self.assertTrue(self.can_reach_entrance("Greenwich Observatory -> Greenwich, Naval Academy"))

        self.assertFalse(self.can_reach_entrance("Hub -> Kew Gardens"))
        self.collect_by_name("Potting Shed Key")
        self.assertFalse(self.can_reach_entrance("Hub -> Kew Gardens"))
        self.collect_by_name(["Progressive Valve", "Progressive Valve", "Progressive Valve"])
        self.assertTrue(self.can_reach_entrance("Hub -> Kew Gardens"))

        self.assertTrue(self.can_reach_entrance("Hub -> Dankenstein"))
        self.assertTrue(self.can_reach_entrance("Dankenstein -> Iron Slugger"))
        self.assertTrue(self.can_reach_entrance("Hub -> Iron Slugger"))

        self.assertFalse(self.can_reach_entrance("Hub -> Wulfrum Hall"))
        self.collect_by_name("Front Door Key")
        self.assertTrue(self.can_reach_entrance("Hub -> Wulfrum Hall"))
        self.assertTrue(self.can_reach_entrance("Wulfrum Hall -> The Count"))
        self.assertTrue(self.can_reach_entrance("Hub -> The Count"))

        self.assertFalse(self.can_reach_entrance("Hub -> Whitechapel"))
        self.collect_by_name(["Library Key", "Club Membership Card", "Beard", "Unicorn Shield", "Griffin Shield"])
        self.assertTrue(self.can_reach_entrance("Hub -> Whitechapel"))

        self.assertFalse(self.can_reach_entrance("Hub -> The Sewers"))
        self.collect_by_name("Poster")
        self.assertTrue(self.can_reach_entrance("Hub -> The Sewers"))

        self.assertFalse(self.can_reach_entrance("Hub -> The Time Machine"))
        self.collect_by_name(
            ["Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"]
        )
        self.assertTrue(self.can_reach_entrance("Hub -> The Time Machine"))

        self.assertFalse(self.can_reach_entrance("The Time Machine -> The Time Machine, The Sewers"))
        self.collect_by_name("King Mullock's Key")
        self.assertTrue(self.can_reach_entrance("The Time Machine -> The Time Machine, The Sewers"))

        self.assertFalse(self.can_reach_entrance("The Time Machine, The Sewers -> The Ripper"))
        self.collect_by_name("Good Lightning")
        self.assertFalse(self.can_reach_entrance("The Time Machine, The Sewers -> The Ripper"))
        self.collect_by_name("Time Stone")
        self.assertTrue(self.can_reach_entrance("The Time Machine, The Sewers -> The Ripper"))

        lost_souls = self.get_items_by_name("Lost Soul")
        self.assertGreaterEqual(len(lost_souls), 12, "test assumes at least 12 Lost Soul copies in the pool")

        self.assertFalse(self.can_reach_entrance("Hub -> Cathedral Spires"))
        self.collect(lost_souls[:5])
        self.assertTrue(self.can_reach_entrance("Hub -> Cathedral Spires"))

        self.collect(self.get_items_by_name("Progressive Golden Cog"))
        self.assertFalse(self.can_reach_entrance("Cathedral Spires -> Cathedral Spires, The Descent"))
        self.collect(lost_souls[5:12])  # 5 + 7 = 12 total
        self.assertTrue(self.can_reach_entrance("Cathedral Spires -> Cathedral Spires, The Descent"))

        self.assertTrue(self.can_reach_entrance("Hub -> The Demon"))
        self.assertBeatable(True)

    def test_reaching_the_demon_requires_all_twelve_lost_souls_even_via_the_hub_shortcut(self) -> None:
        """
        "Hub -> The Demon" is a direct shortcut into The Demon's region that bypasses
        "Cathedral Spires -> Cathedral Spires, The Descent" entirely. Both it and
        "Cathedral Spires, The Descent -> The Demon" must independently require the full
        12 Lost Souls, since collecting the 2 Progressive Golden Cogs alone (which is all
        "Cleared: Cathedral Spires, The Descent" itself checks) isn't enough.
        """
        # Collect everything needed to reach Hub and beyond except Lost Souls, so the only
        # remaining variable is the lost soul count itself.
        self.collect_by_name(
            [
                "Torch",
                "Cannon Ball",
                "Museum Key",
                "Dinosaur Key",
                "Depot Key",
                "Town House Key",
                "Pocket Watch",
                "Staff of Anubis",
                "Scroll of Sekhmet",
                "Tablet of Horus",
                "Elephant Key 1",
                "Elephant Key 2",
                "Dan Hand",
                "Bellows",
                "Potting Shed Key",
                "Front Door Key",
                "Library Key",
                "Club Membership Card",
                "Beard",
                "Unicorn Shield",
                "Griffin Shield",
                "Poster",
                "Time Machine Piece (Contact Room)",
                "Time Machine Piece (Earth Room)",
                "Time Machine Piece (Space Room)",
                "King Mullock's Key",
                "Good Lightning",
                "Time Stone",
            ]
        )
        self.collect(self.get_items_by_name("Progressive Valve"))
        self.collect(self.get_items_by_name("Progressive Golden Cog"))

        lost_souls = self.get_items_by_name("Lost Soul")
        self.assertGreaterEqual(len(lost_souls), 12, "test assumes at least 12 Lost Soul copies in the pool")
        self.collect(lost_souls[:11])
        self.assertFalse(self.can_reach_entrance("Hub -> The Demon"))
        self.assertFalse(self.can_reach_entrance("Cathedral Spires, The Descent -> The Demon"))

        self.collect(lost_souls[11:12])
        self.assertTrue(self.can_reach_entrance("Hub -> The Demon"))
        self.assertTrue(self.can_reach_entrance("Cathedral Spires, The Descent -> The Demon"))
