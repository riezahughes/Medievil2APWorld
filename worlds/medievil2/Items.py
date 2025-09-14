from enum import IntEnum
from typing import NamedTuple, List, Optional
import random
from BaseClasses import Item, ItemClassification


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
    KEY_ITEMS = 10
    TRAP = 11


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
    Medievil2ItemData("Ammo: Fire Crossbow (30)", 10, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Fire Crossbow (50)", 11, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gatling Gun (50)", 12, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gatling Gun (100)", 13, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Blunderbuss (30)", 14, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Blunderbuss (50)", 15, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Bombs (15)", 16, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Bombs (30)", 17, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Chicken Drumsticks (10)", 18, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Chicken Drumsticks (20)", 19, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Copper Shield (50)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Copper Shield (100)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Silver Shield (100)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Silver Shield (200)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gold Shield (100)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    Medievil2ItemData("Ammo: Gold Shield (300)", None, Medievil2ItemCategory.WEAPON_AMMO, False),
    # Charge
    Medievil2ItemData("Charge: Lightning", 20, Medievil2ItemCategory.WEAPON_CHARGE, False),
    Medievil2ItemData("Charge: Broadsword", 21, Medievil2ItemCategory.WEAPON_CHARGE, False),
    # Melee Weapons
    Medievil2ItemData("Small Sword", 22, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Broad Sword", 23, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Magic Sword", 24, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Cane Stick", 25, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Hammer", 26, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Axe", 27, Medievil2ItemCategory.MELEE_WEAPONS, True),
    Medievil2ItemData("Torch", 28, Medievil2ItemCategory.MELEE_WEAPONS, True),
    # Ranged Weapons
    Medievil2ItemData("Pistol", 29, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Crossbow", 30, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Fire Crossbow", 31, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Gatling Gun", 32, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Good Lightning", 33, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Lightning", 34, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Blunderbuss", 35, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Bombs", 36, Medievil2ItemCategory.RANGED_WEAPONS, True),
    Medievil2ItemData("Chicken Drumsticks", 37, Medievil2ItemCategory.RANGED_WEAPONS, True),
    # Shields
    Medievil2ItemData("Bronze Shield", 38, Medievil2ItemCategory.SHIELDS, True),
    Medievil2ItemData("Silver Shield", 39, Medievil2ItemCategory.SHIELDS, True),
    Medievil2ItemData("Gold Shield", 40, Medievil2ItemCategory.SHIELDS, True),
    # Life Bottles
    Medievil2ItemData("Life Bottle", 41, Medievil2ItemCategory.LIFE_BOTTLE, True),
    # Dans Armour
    Medievil2ItemData("Gold Armour", 42, Medievil2ItemCategory.DANS_ARMOUR, True),
    # Key Items
    Medievil2ItemData("Poster", 43, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Head", 44, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Chalice of Souls", 45, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Left Leg", 46, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Right Leg", 47, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Left Arm", 48, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Right Arm", 49, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Bum", 50, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Torso", 51, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Bellows", 52, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Lost Soul", 53, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Golden Cog", 54, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Spell Page", 55, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Griffin Shield", 56, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Unicorn Shield", 57, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Beard", 58, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Library Key", 59, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Club Membership Card", 60, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Elephant Key 1", 61, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Elephant Key 2", 62, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Contact Room)", 63, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Earth Room)", 64, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Machine Piece (Space Room)", 65, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("King Mullock's Key", 66, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Staff of Anubis", 67, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Scroll of Sekhmet", 68, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Tablet of Horus", 69, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Pocket Watch", 70, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Town House Key", 71, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Time Stone", 72, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Antidote", 73, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Pond Room Valve", 74, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Hothouse Valve", 75, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Water Tank Valve", 76, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Cannon Ball", 77, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Front Door Key", 78, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Potting Shed Key", 79, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("The Depot Key", 80, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Museum Key", 81, Medievil2ItemCategory.KEY_ITEMS, True),
    Medievil2ItemData("Dinosaur Key", 82, Medievil2ItemCategory.KEY_ITEMS, True),
    # Traps
    Medievil2ItemData("Trap: Heavy Dan", 83, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Light Dan", 84, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Darkness", 85, Medievil2ItemCategory.TRAP, False),
    Medievil2ItemData("Trap: Hudless", 86, Medievil2ItemCategory.TRAP, False),
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

    # this needs adjusted for VS
    progression_items = [item_data.name for item_data in _all_items if item_data.progression]

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

    print(filler_item_names)

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
