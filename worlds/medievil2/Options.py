import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions

class GoalOptions():
    DEFEAT_DEMON = 0
    HIDDEN_ROOMS = 1
    CHALICE = 2
    BOTH = 3

class ProgressionOptions():
    VANILLA = 0
    RANDOM = 1

class GuaranteedItemsOption(ItemDict):
    """Guarantees that the specified items will be in the item pool"""
    display_name = "Guaranteed Items"

class GoalOption(Choice):
    """Lets the user choose the completion goal
    Defeat Zarok - Beat the boss at the end
    Chalices - Collect all chalices (Collect all chalices doesn't work right now)"""
    display_name = "Completion Goal"
    default = GoalOptions.DEFEAT_DEMON
    option_demon = GoalOptions.DEFEAT_DEMON
    option_hidden_rooms = GoalOptions.HIDDEN_ROOMS
    option_chalice = GoalOptions.CHALICE
    option_both = GoalOptions.BOTH
    
class ProgressionOption(Choice):
    """Lets users choose how they wish to progress
    Vanilla - Plays the game like normal
    (Will only do Vanilla for now)"""
    display_name = "Game Progression Options"
    default = ProgressionOptions.VANILLA
    option_vanilla = ProgressionOptions.VANILLA
    
class IncludeSecretRoomsInChecks(Toggle):
    """Toggle whether to include dan hand secret areas items in checks """
    display_name = "Include Secret Items"
    default = 1
    option_true = 1
    option_false = 0

class IncludeSavingPumpkinSoulsInChecksToggle(Toggle):
    """Include saving all souls in each room in Kew Gardens """
    display_name = "Include Saving Souls in Kew Gardens"
    default = 1
    option_true = 1
    option_false = 0    

class IncludeChalicesInChecksToggle(Toggle):
    """Include Chalices in Checks"""
    display_name = "Include Chalices"
    default = 1
    option_true = 1
    option_false = 0
    
class MonsterSanityToggle(Toggle):
    """Sets whether to do checks for individual monsters (Doesn't work)"""
    display_name = "MonsterSanity"
    default = 0
    option_true = 1
    option_false = 0
    
class KeySanityToggle(Toggle):
    """Sets whether to mix keys into the pool (Doesn't work yet. Will add the items, but not the logic)"""
    display_name = "KeySanity"
    default = 0
    option_true = 1
    option_false = 0
    
class DeathLinkToggle(Toggle):
    """Sets if you want deathlink or not"""
    display_name = "Death Link"
    default = 0
    option_true = 1
    option_false = 0

@dataclass
class MedievilOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    include_secret_rooms_in_checks: IncludeSecretRoomsInChecks
    include_chalices_in_checks: IncludeChalicesInChecksToggle
    deathlink: DeathLinkToggle
    monstersanity: MonsterSanityToggle
    keysanity: KeySanityToggle
    guaranteed_items: GuaranteedItemsOption