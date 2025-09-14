from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import Medievil2Item


class Medievil2LocationCategory(IntEnum):
    KEY_ITEM = 0
    CHEST = 1
    BOSS = 2
    CHALICE_PICKUP = 3
    CHALICE_REWARD = 4
    BOOK = 5
    GOLD = 6
    ENERGY = 7
    LIFE_BOTTLE = 8
    WEAPON = 9
    LEVEL_END = 10


class Medievil2LocationData(NamedTuple):
    name: str
    default_item: str
    category: Medievil2LocationCategory


class Medievil2Location(Location):
    game: str = "Medievil 2"
    category: Medievil2LocationCategory
    default_item_name: str

    def __init__(
        self,
        player: int,
        name: str,
        category: Medievil2LocationCategory,
        default_item_name: str,
        address: Optional[int] = None,
        parent: Optional[Region] = None,
    ):
        super().__init__(player, name, address, parent)
        self.default_item_name = default_item_name
        self.category = category
        self.name = name

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 99250000
        region_offset = 1000
        table_order = [
            "Hub",
            "The Museum",
            "Tyrannosaurus Wrecks",
            "Kensington",
            "The Tomb",
            "The Freakshow",
            "Greenwich Observatory ",
            "Greenwich, Naval Academy",
            "Kew Gardens",
            "Dankenstein",
            "Iron Slugger",
            "Wulfrum Hall",
            "The Count",
            "Whitechapel",
            "The Sewers",
            "The Time Machine",
            "The Time Machine, Sewers",
            "The Ripper",
            "Cathedral Spires",
            "Cathedral Spires: The Descent",
            "The Demon",
        ]

        output = {}
        for i, region_name in enumerate(table_order):
            current_region_base_id = base_id + (i * region_offset)
            # Ensure the region exists in location_tables
            if region_name in location_tables:
                # Enumerate the items within the current region, starting from current_region_base_id
                for j, location_data in enumerate(location_tables[region_name]):
                    # Assign an ID to each location within the region
                    # The ID for each location in a region will be current_region_base_id + j
                    # print(f"{current_region_base_id + j}: {location_data.name}")
                    output[location_data.name] = current_region_base_id + j

        return output

        # return {location_data.name: (base_id + location_data.m_code) for location_data in location_tables["MainWorld"]}

    def place_locked_item(self, item: Medievil2Item):
        self.item = item
        self.locked = True
        item.location = self


location_tables = {
    "Hub": [
        Medievil2LocationData("Chalice Reward: Cane Stick", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Hammer", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Crossbow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Axe", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Bombs", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Broad Sword", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Lightning", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Blunderbuss", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Magic Sword", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Gatling Gun", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
    ],
    "The Museum": [
        Medievil2LocationData("Key Item: Museum Key", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Dinosaur Key", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Cannonball", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Torch", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Equipment: Short Sword", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Pistol", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Energy Vial - Pistol Room", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial - Mausoleum Room 2nd Floor", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 1", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 2", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 3", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Buddah Statue Staircase", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Zarok Room Rafters 1", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Zarok Room Rafters 2", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Chalice: The Museum", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: The Museum", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "Tyrannosaurus Wrecks": [
        Medievil2LocationData("Cleared: Tyrannosaurus Wrecks", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Kensington": [
        Medievil2LocationData("Cleared: Kensington", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Tomb": [
        Medievil2LocationData("Cleared: The Tomb", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Freakshow": [
        Medievil2LocationData("Cleared: The Freakshow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Greenwich Observatory ": [
        Medievil2LocationData("Cleared: Greenwich - Observatory", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Greenwich, Naval Academy": [
        Medievil2LocationData("Cleared: Greenwich - Naval Academy", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Kew Gardens": [
        Medievil2LocationData("Cleared: Kew Gardens", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Dankenstein": [
        Medievil2LocationData("Cleared: Dankenstein", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "Iron Slugger": [
        Medievil2LocationData("Cleared: Iron Slugger", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Wulfrum Hall": [
        Medievil2LocationData("Cleared: Wulfrum Hall", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Count": [
        Medievil2LocationData("Cleared: The Count", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Whitechapel": [
        Medievil2LocationData("Cleared: Whitechapel", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Sewers": [
        Medievil2LocationData("Cleared: The Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Time Machine": [
        Medievil2LocationData("Cleared: The Time Machine", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Time Machine, Sewers": [
        Medievil2LocationData("Cleared: The Time Machine - Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Ripper": [
        Medievil2LocationData("Cleared: The Ripper", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Cathedral Spires": [
        Medievil2LocationData("Cleared: Cathedral Spires", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Cathedral Spires: The Descent": [
        Medievil2LocationData("Cleared: Cathedral Spires - The Descent", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Demon": [
        Medievil2LocationData("Cleared: The Demon", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
}

location_dictionary: Dict[str, Medievil2LocationData] = {}  #
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
