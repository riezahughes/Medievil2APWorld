from enum import IntEnum
from typing import NamedTuple, List, Optional
import random
from BaseClasses import Item, ItemClassification
from .Options import KeyItemSanityToggle


class Medievil2ItemCategory(IntEnum):
    FILLER = 0
    MELEE_WEAPONS = 1
    RANGED_WEAPONS = 2
    SHIELDS = 3
    LIFE_BOTTLE = 4
    DANS_ARMOUR = 5
    GOLD = 6
    ENERGY = 7
    WEAPON_AMMO = 8
    WEAPON_CHARGE = 9
    DANKENSTEIN_PARTS = 10
    KEYS = 11
    KEY_ITEMS = 12
    TRAP = 13
    SKILLS = 14


class Medievil2ItemData(NamedTuple):
    name: str
    m_code: Optional[int]  # Changed to Optional[int] for flexibility with None
    category: Medievil2ItemCategory
    progression: bool  # Added 'progression' field to the raw data


class Medievil2Item(Item):
    game: str = "Vagrant Story"
    category: Medievil2ItemCategory
    m_code: Optional[int]

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int):
        super().__init__(name, classification, code, player)
        # The 'advancement' attribute is automatically handled by the parent Item class
        # if ItemClassification.progression is passed to its constructor.
        # You can explicitly set it here for clarity if you prefer, but BaseClasses.Item does this.
        # self.advancement = classification == ItemClassification.progression

        # Store game-specific data directly on the item instance
        item_data = item_dictionary.get(name)
        if item_data:
            self.v_code = item_data.m_code
            self.category = item_data.category
        else:
            self.v_code = None
            self.category = Medievil2ItemCategory.FILLER  # Fallback for unknown items

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 9901000
        # Create a dictionary mapping item names to their unique Archipelago IDs.
        return {item_data.name: (base_id + item_data.m_code) for item_data in _all_items if item_data.m_code is not None}


key_item_names = {}


_all_items: List[Medievil2ItemData] = [
    # Gold
    Medievil2ItemData("Gold: (50)", 0, Medievil2ItemCategory.GOLD, False),
    Medievil2ItemData("Gold: (100)", 1, Medievil2ItemCategory.GOLD, False),
    Medievil2ItemData("Gold: (200)", 2, Medievil2ItemCategory.GOLD, False),
    # Energy
    Medievil2ItemData("Energy: (50)", 3, Medievil2ItemCategory.ENERGY, False),
    Medievil2ItemData("Energy: (100)", 4, Medievil2ItemCategory.ENERGY, False),
    Medievil2ItemData("Energy: (300)", 5, Medievil2ItemCategory.ENERGY, False),
    # Ammo
    Medievil2ItemData("Ammo: Pistol (30)", 6, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Pistol (50)", 7, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Crossbow (30)", 8, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Crossbow (50)", 9, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Flaming Crossbow (30)", 10, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Flaming Crossbow (50)", 11, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gatling Gun (50)", 12, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gatling Gun (100)", 13, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Blunderbuss (30)", 14, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Blunderbuss (50)", 15, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Bombs (15)", 16, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Bombs (30)", 17, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Chicken Drumsticks (10)", 18, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Chicken Drumsticks (20)", 19, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Copper Shield (50)", 20, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Copper Shield (100)", 21, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Silver Shield (100)", 22, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Silver Shield (200)", 23, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gold Shield (100)", 24, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gold Shield (300)", 25, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Dan's Armour (50)", 24, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Dan's Armour (100)", 25, Medievil2ItemCategory.WEAPON_AMMO, False),
    # Charge
    Medievil2ItemData("Charge: Lightning (30)", 26, Medievil2ItemCategory.WEAPON_CHARGE, False),
    Medievil2ItemData("Charge: Lightning (50)", 26, Medievil2ItemCategory.WEAPON_CHARGE, False),
    Medievil2ItemData("Charge: Broadsword (30)", 27, Medievil2ItemCategory.WEAPON_CHARGE, False),
    Medievil2ItemData("Charge: Broadsword (50)", 27, Medievil2ItemCategory.WEAPON_CHARGE, False),
    # Melee Weapons
    Medievil2ItemData("Small Sword", 28, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Broad Sword", 29, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Magic Sword", 30, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Cane Stick", 31, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Hammer", 32, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Axe", 33, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Torch", 34, Medievil2ItemCategory.MELEE_WEAPONS, True),
    # Ranged Weapons
    Medievil2ItemData("Pistol", 35, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Crossbow", 36, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Flaming Crossbow", 37, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Gatling Gun", 38, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Good Lightning", 39, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Lightning", 40, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Blunderbuss", 41, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Bombs", 42, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Chicken Drumsticks", 43, Medievil2ItemCategory.RANGED_WEAPONS, True),
    # Shields
    Medievil2ItemData("Bronze Shield", 44, Medievil2ItemCategory.SHIELDS, True),
    Medievil2ItemData("Silver Shield", 45, Medievil2ItemCategory.SHIELDS, True),
    Medievil2ItemData("Gold Shield", 46, Medievil2ItemCategory.SHIELDS, True),
    # Life Bottles
    Medievil2ItemData("Life Bottle", 47, Medievil2ItemCategory.LIFE_BOTTLE, True),
    # Dans Armour
    Medievil2ItemData("Gold Armour", 48, Medievil2ItemCategory.DANS_ARMOUR, True),
    # Skills
    Medievil2ItemData("Dan Hand", 50, Medievil2ItemCategory.SKILLS, True),
    # Key Items
    Medievil2ItemData("Poster", 51, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Left Leg", 52, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Right Leg", 53, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Left Arm", 54, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Right Arm", 55, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Bum", 56, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Torso", 57, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Bellows", 58, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Lost Soul", 59, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Golden Cog 1", 60, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Golden Cog 2", 60, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Spell Page", 61, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Griffin Shield", 62, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Unicorn Shield", 63, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Beard", 64, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Library Key", 65, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Club Membership Card", 66, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Elephant Key 1", 67, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Elephant Key 2", 68, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Contact Room)", 69, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Earth Room)", 70, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Space Room)", 71, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("King Mullock's Key", 72, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Staff of Anubis", 73, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Scroll of Sekhmet", 74, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Tablet of Horus", 75, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Pocket Watch", 76, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Town House Key", 77, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Stone", 78, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Antidote", 79, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Pond Room Valve", 80, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Hothouse Valve", 81, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Water Tank Valve", 82, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Cannon Ball", 83, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Front Door Key", 84, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Potting Shed Key", 85, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Depot Key", 86, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Museum Key", 87, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Dinosaur Key", 88, Medievil2ItemCategory.KEY_ITEMS, True),
    # Traps
    Medievil2ItemData("Trap: Heavy Dan", 89, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Light Dan", 90, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Darkness", 91, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Hudless", 92, Medievil2ItemCategory.TRAP, False),
]
# Convert raw list of tuples into MedievilItemData NamedTuple instances
# _all_items = [Medievil2ItemData(row[0], row[1], row[2], row[3]) for row in _all_items]


item_descriptions = {
    # Optional: Add detailed descriptions for items here
    # "Gold (50)": "A small pouch of gold coins."
}

# Create a dictionary for quick lookup of item data by name
item_dictionary: dict[str, Medievil2ItemData] = {item_data.name: item_data for item_data in _all_items}


def BuildItemPool(count: int, options) -> List[str]:
    """
    Generates a list of item names to be used for the item pool.
    This function does NOT create Archipelago Item objects; it only provides their names.
    The actual Item objects are created in Medievil2World.create_items.

    Args:
        count (int): The total number of item names to generate.
        options: The options object from the Archipelago multiworld, used for guaranteed items.

    Returns:
        List[str]: A shuffled list of item names.
    """
    item_pool_names: List[str] = []

    # Add any guaranteed items specified in the options first
    if hasattr(options, "guaranteed_items") and options.guaranteed_items.value:
        for item_name in options.guaranteed_items.value:
            if item_name in item_dictionary:
                item_pool_names.append(item_name)
            else:
                print(f"Warning: Guaranteed item '{item_name}' not found in item_dictionary. Skipping.")

    progression_items = [
        item_data.name
        for item_data in _all_items
        if (
            hasattr(options, "keyitemsanity")
            and options.keyitemsanity.value == KeyItemSanityToggle.option_true
            and item_data.category == Medievil2ItemCategory.KEY_ITEMS
        )
        or item_data.category == Medievil2ItemCategory.MELEE_WEAPONS
        or item_data.category == Medievil2ItemCategory.SHIELDS
        or item_data.category == Medievil2ItemCategory.RANGED_WEAPONS
        or item_data.category == Medievil2ItemCategory.SKILLS
    ]

    for item_name in progression_items:
        if item_name not in item_pool_names and len(item_pool_names) < count:
            item_pool_names.append(item_name)

    # Populate the rest of the pool with random filler items
    filler_item_names = [
        item_data.name
        for item_data in _all_items
        if item_data.category == Medievil2ItemCategory.WEAPON_CHARGE
        or item_data.category == Medievil2ItemCategory.WEAPON_AMMO
        or item_data.category == Medievil2ItemCategory.ENERGY
        or item_data.category == Medievil2ItemCategory.GOLD
        or item_data.category == Medievil2ItemCategory.TRAP
    ]

    for _ in range(count - len(item_pool_names)):
        if filler_item_names:
            item_name_to_add = random.choice(filler_item_names)
            item_pool_names.append(item_name_to_add)
        else:
            print("Warning: Ran out of filler items for Vagrant Story. Duplicating from all available items.")
            # Fallback: if no specific filler items left, pick from any available item
            item_pool_names.append(random.choice(list(item_dictionary.keys())))

    random.shuffle(item_pool_names)  # Shuffle the final list of item names
    return item_pool_names
