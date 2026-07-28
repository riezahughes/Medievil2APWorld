"""
Regression tests for set_chalice_vanilla_rules and has_cleared_levels in Rules.py. Unlike
Medievil 1's hall-of-heroes progression (which had a late-binding closure bug), each
"Chalice Reward: X" location here is set with a literal hardcoded count in its own lambda,
so there's no closure bug to worry about -- each reward genuinely requires its own count.

has_cleared_levels only tracks 10 SPECIFIC levels (not every level in the game): The
Museum, Kensington, The Freakshow, Greenwich Observatory, Kew Gardens, Dankenstein, Wulfrum
Hall, Whitechapel, The Sewers, and The Ripper. Tyrannosaurus Wrecks, The Tomb, Naval
Academy, Iron Slugger, Cathedral Spires (and its Descent), and The Demon are NOT tracked.
"""

from . import Medievil2TestBase

REWARD_NAME_BY_COUNT = {
    1: "Cane Stick",
    2: "Hammer",
    3: "Crossbow",
    4: "Axe",
    5: "Bombs",
    6: "Broadsword",
    7: "Lightning",
    8: "Blunderbuss",
    9: "Magic Sword",
    10: "Gatling Gun",
}


class ChaliceRewardNoKeyItemSanityTest(Medievil2TestBase):
    def _reward_reachable(self, count: int) -> bool:
        return self.can_reach_location(f"Chalice Reward: {REWARD_NAME_BY_COUNT[count]}")

    def test_all_ten_rewards_reachable_with_only_dan_hand(self) -> None:
        """
        Without keyitemsanity, none of the 10 tracked "Cleared: X" locations have any item
        gating. The Museum, Kensington, and The Freakshow are reachable with zero items
        (rewards 1-3), and once Dan Hand opens the path to Greenwich Observatory (and thus
        the rest of the vanilla chain), all remaining rewards become reachable too.
        """
        for i in range(1, 4):
            with self.subTest(reward=i):
                self.assertTrue(self._reward_reachable(i))
        for i in range(4, 11):
            with self.subTest(reward=i):
                self.assertFalse(self._reward_reachable(i))
        self.collect_by_name("Dan Hand")
        for i in range(1, 11):
            with self.subTest(reward=i):
                self.assertTrue(self._reward_reachable(i))


class ChaliceRewardChalicesDisabledTest(Medievil2TestBase):
    options = {
        "include_chalices_in_checks": 0,
    }

    def test_reward_and_pickup_locations_do_not_exist(self) -> None:
        for location in ("Chalice Reward: Cane Stick", "Chalice: The Museum"):
            with self.subTest(location=location):
                with self.assertRaises(KeyError):
                    self.world.get_location(location)


class ChaliceRewardWithKeyItemSanityTest(Medievil2TestBase):
    """
    With keyitemsanity on, most of the 10 tracked "Cleared: X" locations gain real item
    gating, so the reward count only rises as those items are collected.
    """

    options = {
        "keyitemsanity": 1,
    }

    def _reward_reachable(self, count: int) -> bool:
        return self.can_reach_location(f"Chalice Reward: {REWARD_NAME_BY_COUNT[count]}")

    def test_rewards_gated_behind_real_level_clears(self) -> None:
        self.assertFalse(self._reward_reachable(1))

        self.collect_by_name(["Torch", "Cannon Ball", "Museum Key", "Dinosaur Key"])  # The Museum
        self.assertTrue(self._reward_reachable(1))
        self.assertFalse(self._reward_reachable(2))

        self.collect_by_name(["Depot Key", "Town House Key", "Pocket Watch"])  # Kensington
        self.assertTrue(self._reward_reachable(2))
        self.assertFalse(self._reward_reachable(3))

        self.collect_by_name(["Staff of Anubis", "Scroll of Sekhmet", "Tablet of Horus"])  # needed for The Tomb, not tracked
        self.collect_by_name(["Elephant Key 1", "Elephant Key 2"])  # The Freakshow
        self.assertTrue(self._reward_reachable(3))
        self.assertFalse(self._reward_reachable(4))

        self.collect_by_name("Dan Hand")  # Greenwich Observatory
        self.assertTrue(self._reward_reachable(4))
        self.assertFalse(self._reward_reachable(5))

        self.collect_by_name(["Bellows"])  # needed for Naval Academy, not tracked, but Kew Gardens needs it reachable
        self.collect_by_name("Potting Shed Key")
        self.collect(self.get_items_by_name("Progressive Valve"))  # Kew Gardens needs 3 valves
        self.assertTrue(self._reward_reachable(5))

        # Dankenstein has no item blocks at all, so it's already reachable as soon as Kew
        # Gardens is cleared (Hub -> Dankenstein only needs Cleared: Kew Gardens) -- no
        # separate item collection needed for reward 6.
        self.assertTrue(self._reward_reachable(6))
        self.assertFalse(self._reward_reachable(7))

        self.collect_by_name("Front Door Key")  # Wulfrum Hall
        self.assertTrue(self._reward_reachable(7))
        self.assertFalse(self._reward_reachable(8))

        self.collect_by_name(["Library Key", "Club Membership Card", "Beard", "Unicorn Shield", "Griffin Shield"])  # Whitechapel
        self.assertTrue(self._reward_reachable(8))
        self.assertFalse(self._reward_reachable(9))

        self.collect_by_name("Poster")  # The Sewers
        self.assertTrue(self._reward_reachable(9))
        self.assertFalse(self._reward_reachable(10))

        self.collect_by_name(
            ["Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"]
        )
        self.collect_by_name(["King Mullock's Key", "Good Lightning", "Time Stone"])  # The Ripper
        self.assertTrue(self._reward_reachable(10))
