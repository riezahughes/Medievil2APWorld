import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions


class GoalOptions:
    DEFEAT_DEMON = 0
    # HIDDEN_ROOMS = 1
    # CHALICE = 2
    # ALL = 3


class ProgressionOptions:
    VANILLA = 0
    # OPEN = 1


class CheatMenuOptions:
    OFF = 0
    ON = 1


class GuaranteedItemsOption(ItemDict):
    """Guarantees that the specified items will be in the item pool"""

    display_name = "Guaranteed Items"


class GoalOption(Choice):
    """Lets the user choose the completion goal
    Defeat Demon - Beat the boss at the end
    Hidden Rooms - Find all of Dan Hand's secret rooms
    All - Get all hidden rooms, chalices AND defeat the demon
    Chalices - Collect all chalices (Collect all chalices doesn't work right now)"""

    display_name = "Completion Goal"
    default = GoalOptions.DEFEAT_DEMON
    option_demon = GoalOptions.DEFEAT_DEMON
    # option_hidden_rooms = GoalOptions.HIDDEN_ROOMS
    # option_chalice = GoalOptions.CHALICE
    # option_both = GoalOptions.ALL


class ProgressionOption(Choice):
    """Lets users choose how they wish to progress
    Vanilla - Plays the game like normal
    (Will only do Vanilla for now)"""

    display_name = "Game Progression Options"
    default = ProgressionOptions.VANILLA
    option_vanilla = ProgressionOptions.VANILLA
    # option_open = ProgressionOptions.OPEN


# class IncludeSecretRoomsInChecks(Toggle):
#     """Toggle whether to include dan hand secret areas items in checks (not implimented. Will always be on)"""

#     display_name = "Include Secret Items"
#     default = 1
#     option_true = 1
#     option_false = 0


# class IncludeSavingPumpkinSoulsInChecksToggle(Toggle):
#     """Include saving all souls in each room in Kew Gardens"""

#     display_name = "Include Saving Souls in Kew Gardens"
#     default = 1
#     option_true = 1
#     option_false = 0


class IncludeChalicesInChecksToggle(Toggle):
    """Include Chalices in Checks"""

    display_name = "Include Chalices"
    default = 1
    option_true = 1
    option_false = 0


class KeyItemSanityToggle(Toggle):
    """Sets whether to mix key items into the pool (Doesn't work yet. Will add the items, but not the logic)"""

    display_name = "KeySanity"
    default = 0
    option_true = 1
    option_false = 0


# class IncludeDankensteinPartsInItemPoolToggle(Toggle):
#     """Include the dankenstein pieces in the item pool (Arms, Legs, Torso and Bum will need to be found to clear dankenstein)"""

#     display_name = "Include Dankenstein Parts"
#     default = 0
#     option_true = 1
#     option_false = 0


class CheatMenuChoice(Choice):
    """Sets the cheat menu to be available in the pause menu. This allows level skip, chalice completion and
    invulnerability. Please note, though. That the chalices are counted via checks as getting the actual number isn't
    viable at the moment. Sorry!"""

    display_name = "Cheat Menu"
    default = CheatMenuOptions.OFF
    option_off = CheatMenuOptions.OFF
    option_on = CheatMenuOptions.ON


class BreakAmmoLimit(Toggle):
    """Allow weapon ammo to be higher than the default"""

    display_name = "Break Ammo Count Limit"
    default = 1
    option_true = 1
    option_false = 0


class BreakPercentageLimit(Toggle):
    """Allow weapon percentages to be higher than the default"""

    display_name = "Break Weapon Percentage Limit"
    default = 1
    option_true = 1
    option_false = 0


class AmmoAndChargeToggle(Toggle):
    """Allow Ammo and Charge in the pool"""

    display_name = "Ammo and Charge in Item Pool"
    default = 1
    option_true = 1
    option_false = 0


class TrapToggle(Toggle):
    """Allow traps in the pool"""

    display_name = "Traps in Item Pool"
    default = 1
    option_true = 1
    option_false = 0


class DeathLinkToggle(Toggle):
    """Sets if you want deathlink or not"""

    display_name = "Death Link"
    default = 0
    option_true = 1
    option_false = 0


@dataclass
class Medievil2Options(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    # include_dankenstein_parts: IncludeDankensteinPartsInItemPoolToggle
    # include_secret_rooms_in_checks: IncludeSecretRoomsInChecks
    include_chalices_in_checks: IncludeChalicesInChecksToggle
    keyitemsanity: KeyItemSanityToggle
    traps: TrapToggle
    ammo: AmmoAndChargeToggle
    deathlink: DeathLinkToggle
    break_ammo_limit: BreakAmmoLimit
    break_percentage_limit: BreakPercentageLimit
    cheat_menu: CheatMenuChoice
    guaranteed_items: GuaranteedItemsOption
