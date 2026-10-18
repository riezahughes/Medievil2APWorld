"""
Item pool composition tests for BuildItemPool in Items.py. Key items (including Progressive
Valve / Progressive Golden Cog) must only be in the pool when keyitemsanity is on; the client
relies on the vanilla key items otherwise.
"""

from collections import Counter

from ..Items import Medievil2ItemCategory, item_dictionary
from . import Medievil2TestBase


def _pool_counts(test: Medievil2TestBase) -> Counter:
    return Counter(item.name for item in test.multiworld.itempool)


def _key_item_names(test: Medievil2TestBase) -> list[str]:
    return [name for name in _pool_counts(test) if item_dictionary[name].category == Medievil2ItemCategory.KEY_ITEMS]


class ItemPoolNoKeyItemSanityTest(Medievil2TestBase):
    options = {
        "keyitemsanity": 0,
    }

    def test_no_progressive_items_in_pool(self) -> None:
        counts = _pool_counts(self)
        self.assertEqual(counts["Progressive Valve"], 0)
        self.assertEqual(counts["Progressive Golden Cog"], 0)

    def test_no_key_items_in_pool(self) -> None:
        self.assertEqual(_key_item_names(self), [])


class ItemPoolKeyItemSanityTest(Medievil2TestBase):
    options = {
        "keyitemsanity": 1,
    }

    def test_progressive_item_counts(self) -> None:
        counts = _pool_counts(self)
        self.assertEqual(counts["Progressive Valve"], 3)
        self.assertEqual(counts["Progressive Golden Cog"], 2)

    def test_key_items_present(self) -> None:
        self.assertGreater(len(_key_item_names(self)), 2)
