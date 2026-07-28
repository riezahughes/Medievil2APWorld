"""
Regression tests for VictoryConditions.py. Only one real goal option currently exists
(DEFEAT_DEMON); the others are commented out in Options.py.
"""

from . import Medievil2TestBase
from ..Options import ProgressionOptions


class DefeatDemonGoalTest(Medievil2TestBase):
    def test_not_beatable_until_the_demon_is_reachable(self) -> None:
        self.assertBeatable(False)
        self.collect_by_name("Dan Hand")
        self.assertBeatable(True)


class DefeatDemonGoalOpenModeTest(Medievil2TestBase):
    options = {
        "progression_option": ProgressionOptions.OPEN,
    }

    def test_beatable_with_zero_items_in_open_mode(self) -> None:
        self.assertBeatable(True)
