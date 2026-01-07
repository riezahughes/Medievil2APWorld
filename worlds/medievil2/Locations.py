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
    WINSTON = 7
    ENERGY = 8
    LIFE_BOTTLE = 9
    WEAPON = 10
    LEVEL_END = 11
    EVENT = 12


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
            "Greenwich Observatory",
            "Greenwich, Naval Academy",
            "Kew Gardens",
            "Dankenstein",
            "Iron Slugger",
            "Wulfrum Hall",
            "The Count",
            "Whitechapel",
            "The Sewers",
            "The Time Machine",
            "The Time Machine, The Sewers",
            "The Ripper",
            "Cathedral Spires",
            "Cathedral Spires, The Descent",
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
    "Hub": [  # some of these come from winston. Need to see which do which.
        Medievil2LocationData("Book: Lifestyles of the Pharaohs", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: Professor's Diary", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Chalice Reward: Cane Stick", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Hammer", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Crossbow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Axe", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Bombs", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Broadsword", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Lightning", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Blunderbuss", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Magic Sword", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
        Medievil2LocationData("Chalice Reward: Gatling Gun", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_REWARD),
    ],
    "The Museum": [
        Medievil2LocationData("Key Item: Museum Key - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Cannonball - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Torch - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Dinosaur Key - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Equipment: Short Sword at Start - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Pistol in Case - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Copper Shield 2nd Floor Chest - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Copper Shield Zarok Room - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Energy Vial: Pistol Room - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Mausoleum Room 2nd Floor - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Second Hand Room - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Hidden Behind Purple Structure - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 1 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 2 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Mausoleum Room 2nd Floor 3 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Buddah Statue Staircase - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Display Room Balcony Right - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Display Room Balcony Left - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Zarok Room Rafters Back - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Zarok Room Rafters Left - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Zarok Room Rafters Right - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Tomb Room Left - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Tomb Room Right - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: First Hand Room - Chest 1 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: First Hand Room - Chest 2 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: First Hand Room - Chest 3 - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Second Hand Room - Chest Right of Vial - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Second Hand Room - Chest Left of Vial - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Second Hand Room - Chest Between Boxes - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Second Hand Room - Chest Hidden on Pipes - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Second Hand Room - Chest on Boxes - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Book: Sir Dan - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: The Kraken - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: Zarok - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Winston: Dans Room - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Pistol Room - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Chest on Mausoleum Room 2nd Floor - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Gold Coins on Mausoleum Room 2nd Floor - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Climbing Wall - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Staircase After Buddah - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Chalice - TM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: The Museum", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: The Museum", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "Tyrannosaurus Wrecks": [
        Medievil2LocationData("Life Bottle: Tyrannosaurus Wrecks", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Copper Chest in Stairway - TW", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Gold Coins: Bag Behind Lion Statue - TW", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Near Spiv on Stairway - TW", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Book: Dinosaur Display - TW", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Winston: Entrance - TW", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: Tyrannosaurus Wrecks", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Kensington": [
        Medievil2LocationData("Key Item: The Depot Key - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Town House Key - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Pocketwatch - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Equipment: Copper Shield on Railway - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Gold Coins: Bag Near Water in Quayside Mill - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Pushing and Pulling - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Where the Spell was Cast - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Museum Roof - KT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Kensington", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Kensington", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Tomb": [
        Medievil2LocationData("Key Item: Scroll of Sekhmet - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Tablet of Horus - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Staff of Anubis - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Gold Coins: Tomb Entrance Top Right - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Tomb Entrance Top Left - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest Ground Floor - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest Upper Floor - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Entrance - TT", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: The Tomb", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Freakshow": [
        Medievil2LocationData("Key Item: Elephant key 1 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Elephant key 2 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: The Freakshow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Copper Shield in Chalice Room - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Copper Shield in Elephant Boss Arena - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Gold Coins: Bag at Start Left - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Ladies Bag Trap 1 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Ladies Bag Trap 2 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Ladies Bag Trap 3 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Ladies Bag Trap 4 - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag in Tunnel - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Outside Tunnel - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest at Water Jump - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Below Giant Clown - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Hidden at Trampolines - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Hidden Chest Left - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Hidden Chest Right - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Entrance - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Trampoline - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Elephant Army - TF", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: The Freakshow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: The Freakshow", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Greenwich Observatory": [
        Medievil2LocationData("Life Bottle: Greenwich Observatory", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Copper Shield near Bomb Chest", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Gold Coins: Fountain Bag 1 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Fountain Bag 2 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Below Spiv - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Below Chalice 1 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Below Chalice 2 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Near Exit - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest 1 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest 2 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest 3 - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Lost your head? - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Close To Ladder - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Lever Puzzle - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Once Through This Door - GO", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Greenwich Observatory", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Greenwich Observatory", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Greenwich, Naval Academy": [
        Medievil2LocationData("Key Item: Bellows - GONA", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Energy Vial: Near Trees - GONA", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Bag Near Trees - GONA", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Entrance - GONA", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Balloon - GONA", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: Naval Academy", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Kew Gardens": [
        Medievil2LocationData("Key Item: Potting Shed Key - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Water Tank Valve - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Pond Room Valve - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Hothouse Valve - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Kew Gardens", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Life Bottle: Kew Gardens 2", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Silver Shield in Gauntlet Room - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Energy Vial: Behind Fence Vial 1 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Behind Fence Vial 2 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Behind Fence Chest 1 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Behind Fence Chest 2 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Near Shed - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest at Top of Tree in First Human Room - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bridge Room Vine Chest 1 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bridge Room Vine Chest 2 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag Up Tree in Second Human Room - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag on Roof 1 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag on Roof 2 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag in Third Human Room - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Maze Chest - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Maze Chest Reward 1 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Maze Chest Reward 2- KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Maze Chest Reward 3 - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Level Start - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Infection - KG", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Kew Gardens", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Kew Gardens", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Dankenstein": [
        Medievil2LocationData("Key Item: Bum - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Left Arm - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Left Leg - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Right Arm - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Right Leg - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Torso - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Dankenstein - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Silver shield - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Gold Coins: Chest Above Projector - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest 1 - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Hand Area Chest 2 - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Book: Reanimation - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Winston: Save Point - DK", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Dankenstein", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Dankenstein", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "Iron Slugger": [
        Medievil2LocationData("Book: Dankenstein Manual - IS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Cleared: Iron Slugger", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Wulfrum Hall": [
        Medievil2LocationData("Key Item: Front Door Key - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Wulfrum Hall", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Silver Shield Close To Vampire Room 2 - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Energy Vial: Near Kitchen Stairs - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Left Room Of Entrance - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: In Front Of Hall's Staircase - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Bag Left Side Of Entrance Stairs - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Close To Vampire Room 1 - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest in Vampire Room 3 - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag in Vampire Room 5 - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Level Start - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Vampires - WH", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Wulfrum Hall", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Wulfrum Hall", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Count": [
        Medievil2LocationData("Winston: Level Start - TC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Gold Coins: Gold Chest - TC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Cleared: The Count", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Whitechapel": [
        Medievil2LocationData("Key Item: Library Key in House Basement - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Griffin Shield - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Membership Card - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Elegant Suit - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Unicorn Shield - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Beard - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Whitechapel", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Silver Shield in Library - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData(
            "Equipment: Flaming Crossbow Inside House Near Unicorn Shield - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON
        ),
        Medievil2LocationData("Gold Coins: Bag 1 in House Basement - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 2 in House Basement - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 1 Tailor Shop Basement -WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 2 Tailor Shop Basement - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 3 Tailor Shop Basement - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Inside Club - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Book: Isibod Brunel - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Winston: Kiya Last Seen - WC", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: Whitechapel", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: Whitechapel", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Sewers": [
        Medievil2LocationData("Key Item: Poster - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Gold Shield in Hub Area - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Event: Girls Freed - 1 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.EVENT),
        Medievil2LocationData("Event: Girls Freed - 2 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.EVENT),
        Medievil2LocationData("Event: Girls Freed - 3 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.EVENT),
        Medievil2LocationData("Event: Girls Freed - 4 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.EVENT),
        Medievil2LocationData("Event: Girls Freed - 5 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.EVENT),
        Medievil2LocationData("Energy Vial: Vial 1 End Pipes Area - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Vial 2 End Pipes Area - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Energy Vial: Vial 3 End Pipes Area - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Bag at Pipes Area Start - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 1 in Pipes Puzzle Room - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag 2 in Pipes Puzzle Room - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Reward Chest 1 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Reward Chest 2 - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Save Point - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Something Really Interesting - TS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: The Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.CHALICE_PICKUP),
        Medievil2LocationData("Cleared: The Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Time Machine": [
        Medievil2LocationData("Key Item: Time Machine Piece - Planetarium - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Time Machine Piece - Grammar Horn - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Time Machine Piece - Moon Exhibit - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Gold Coins: Chest Behind Right Lion Statue - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Book: Space Beacon - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: Grammar Horn - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: Moon Exhibit - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Book: The Time Machine", "Ammo: Gold Shield (100)", Medievil2LocationCategory.BOOK),
        Medievil2LocationData("Winston: Entrance - TTM", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: The Time Machine", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "The Time Machine, The Sewers": [
        Medievil2LocationData("Key Item: Time Stone - Hut Trap - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: King Mullocks Key - Downing King - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Equipment: Good Lightning - Changing Room - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Winston: Entrance - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Kings Hat - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Winston: Stealing Time Stone - TTMTS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: The Time Machine, The Sewers", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Ripper": [
        Medievil2LocationData("Winston: Entrance - TR", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Chalice: The Ripper", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
        Medievil2LocationData("Cleared: The Ripper", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Cathedral Spires": [
        Medievil2LocationData("Key Item: Lost Soul - Bottom left of Cathedral - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Top of Cathedral - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Left Chapel on the Roo - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Right Chapel on the Roo - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Next to Life Bottle - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Cathedral Spires", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Equipment: Gold Shield in Chest at Start - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Equipment: Silver Shield Chest near Gold Coins - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WEAPON),
        Medievil2LocationData("Energy Vial: Next to Spiv - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.ENERGY),
        Medievil2LocationData("Gold Coins: Bottom Right Near Spiv - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest After First Lost Soul - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest After First Flame Gargoyles - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Chest Near Silver Shield Chest - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Bag at top of Spire - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Entrance - CS", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: Cathedral Spires", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    "Cathedral Spires, The Descent": [
        Medievil2LocationData("Key Item: Lost Soul - Left Jump at Chandelere - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Right Jump at Chandelere - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Demon Statue Mausoleum - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Entrance Room - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Top of Pully Front - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Top of Pully Back - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Lost Soul - Pully Room Right - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Golden Cog in Room - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Golden Cog in Hand Area - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Key Item: Spell Page - Demon Death - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.KEY_ITEM),
        Medievil2LocationData("Life Bottle: Cathedral Spires, The Decent", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LIFE_BOTTLE),
        Medievil2LocationData("Gold Coins: Golden Cog Room Entrance - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Gold Coins: Golden Cog Room Bottom - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.GOLD),
        Medievil2LocationData("Winston: Entrance - CSTD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: Cathedral Spires, The Descent", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
    # Boss Fight
    "The Demon": [
        Medievil2LocationData("Winston: Entrance - TD", "Ammo: Gold Shield (100)", Medievil2LocationCategory.WINSTON),
        Medievil2LocationData("Cleared: The Demon", "Ammo: Gold Shield (100)", Medievil2LocationCategory.LEVEL_END),
    ],
}

location_dictionary: Dict[str, Medievil2LocationData] = {}  #
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
