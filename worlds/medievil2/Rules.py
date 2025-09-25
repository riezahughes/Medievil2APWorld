from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState, Iterable
from .Options import IncludeChalicesInChecksToggle


def is_level_cleared(self, location: str, state: CollectionState):
    return state.can_reach_location("Cleared: " + location, self.player)


def has_dan_hand_skill(self, state: CollectionState):
    return state.has("Dan Hand", self.player)


def is_boss_defeated(self, boss: str, state: CollectionState):  # can used later
    return state.has("Boss: " + boss, self.player, 1)


def has_keyitems_required(self, items: list[str], state: CollectionState):
    passed_check = True
    for item in items:
        if state.has(item, self.player, 1) is False:
            passed_check = False
    return passed_check


def set_key_blocks(self, locations: list[str], items: list[str]):
    for location in locations:
        for item in items:
            set_rule(self.get_location(location), lambda state: has_keyitems_required(self, [item], state))


def set_vanilla_level_progression(self):
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Menu", state))
    set_rule(self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), lambda state: is_level_cleared(self, "The Museum", state))
    set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Hub", state))
    set_rule(self.get_entrance("Hub -> Tyrannosaurus Wrecks"), lambda state: is_level_cleared(self, "The Museum", state))
    set_rule(self.get_entrance("Hub -> Kensington"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(self.get_entrance("Kensington -> The Tomb"), lambda state: is_level_cleared(self, "Kensington", state))
    set_rule(self.get_entrance("Hub -> The Freakshow"), lambda state: is_level_cleared(self, "The Tomb", state))
    set_rule(
        self.get_entrance("Hub -> Greenwich Observatory"),
        lambda state: is_level_cleared(self, "The Freakshow", state) and has_dan_hand_skill(self, state),
    )
    set_rule(
        self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), lambda state: is_level_cleared(self, "Greenwich Observatory", state)
    )
    set_rule(self.get_entrance("Hub -> Kew Gardens"), lambda state: is_level_cleared(self, "Naval Academy", state))
    set_rule(self.get_entrance("Hub -> Dankenstein"), lambda state: is_level_cleared(self, "Kew Gardens", state))
    set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Hub -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Hub -> Wulfrum Hall"), lambda state: is_level_cleared(self, "Iron Slugger", state))
    set_rule(self.get_entrance("Wulfrum Hall -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("Hub -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("Hub -> Whitechapel"), lambda state: is_level_cleared(self, "The Count", state))
    set_rule(self.get_entrance("Hub -> The Sewers"), lambda state: is_level_cleared(self, "Whitechapel", state))
    set_rule(self.get_entrance("Hub -> The Time Machine"), lambda state: is_level_cleared(self, "The Sewers", state))
    set_rule(self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), lambda state: is_level_cleared(self, "The Time Machine", state))
    set_rule(
        self.get_entrance("The Time Machine, The Sewers -> The Ripper"), lambda state: is_level_cleared(self, "The Time Machine, The Sewers", state)
    )
    set_rule(self.get_entrance("Hub -> Cathedral Spires"), lambda state: is_level_cleared(self, "The Ripper", state))
    set_rule(self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"), lambda state: is_level_cleared(self, "Cathedral Spires", state))
    set_rule(self.get_entrance("Hub -> The Demon"), lambda state: is_level_cleared(self, "Cathedral Spires, The Descent", state))


def set_item_rules(self):
    # Hub

    # The Museum

    set_key_blocks(
        self,
        [
            "Key Item: Torch - TM",
            "Key Item: Cannonball - TM",
            "Gold Coins: Buddah Statue Staircase - TM",
            "Winston: Climbing Wall - TM",
            "Winston: Staircase After Buddah - TM",
            "Winston: Chalice - TM",
        ],
        ["Museum Key"],
    )

    set_key_blocks(
        self,
        [
            "Equipment: Copper Shield Zarok Room - TM",
            "Gold Coins: Display Room Balcony Right - TM",
            "Gold Coins: Display Room Balcony Left - TM",
            "Gold Coins: Zarok Room Rafters Back - TM",
            "Gold Coins: Zarok Room Rafters Left - TM",
            "Gold Coins: Zarok Room Rafters Right - TM",
            "Book: The Kraken - TM",
            "Book: Zarok - TM",
            "Chalice: The Museum",
        ],
        ["Torch", "Cannon Ball"],
    )

    set_key_blocks(self, ["Gold Coins: Tomb Room Left - TM", "Gold Coins: Tomb Room Right - TM"], ["Dinosaur Key"])

    set_key_blocks(
        self,
        [
            "Gold Coins: First Hand Room - Chest 1 - TM",
            "Gold Coins: First Hand Room - Chest 2 - TM",
            "Gold Coins: First Hand Room - Chest 3 - TM",
            "Gold Coins: Second Hand Room - Chest Right of Vial - TM",
            "Gold Coins: Second Hand Room - Chest Left of Vial - TM",
            "Gold Coins: Second Hand Room - Chest Between Boxes - TM",
            "Gold Coins: Second Hand Room - Chest Hidden on Pipes - TM",
            "Gold Coins: Second Hand Room - Chest on Boxes - TM",
            "Energy Vial: Second Hand Room - TM",
        ],
        ["Dan Hand"],
    )

    # Tyrannosaurus Wrecks - No Blocks

    # Kensington

    set_key_blocks(self, ["Key Item: Town House Key - KT"], ["Depot Key"])

    set_key_blocks(self, ["Key Item: Pocketwatch - KT", "Winston: Where the Spell was Cast - KT", "Chalice: Kensington - KT"], ["Town House Key"])

    set_key_blocks(self, ["Winston: Museum Roof - KT"], ["Pocket Watch"])

    set_key_blocks(self, [], ["Dan Hand"])

    # The Tomb

    set_key_blocks(self, ["Gold Coins: Hand Area Chest Ground Floor - TT", "Gold Coins: Hand Area Chest Upper Floor - TT"], ["Dan Hand"])

    # The Freakshow

    set_key_blocks(self, ["Equipment: Copper Shield in Elephant Boss Arena - TF"], ["Elephant Key 1", "Elephant Key 2"])

    # Greenwich Observatory

    set_key_blocks(
        self, ["Gold Coins: Hand Area Chest 1 - GO", "Gold Coins: Hand Area Chest 2 - GO", "Gold Coins: Hand Area Chest 3 - GO"], ["Dan Hand"]
    )

    # Naval Academy - bellows are end of level

    # Kew Gardens

    # potting shed key for water tank valve
    # water tank valve give you the pond room valve
    # hothouse valve gives you the pond room

    set_key_blocks(self, ["Key Item: Water Tank Valve - KG"], ["Potting Shed Key"])

    set_key_blocks(self, ["Key Item: Pond Room Valve - KG"], ["Water Tank Valve"])

    set_key_blocks(self, ["Key Item: Hothouse Valve - KG"], ["Pond Room Valve"])

    set_key_blocks(
        self,
        ["Equipment: Silver Shield in Gauntlet Room - KG", "Gold Coins: Bag in Third Human Room - KG", "Chalice: Kew Gardens"],
        ["Hothouse Valve"],
    )

    set_key_blocks(
        self,
        [
            "Gold Coins: Hand Maze Chest - KG",
            "Gold Coins: Hand Maze Chest Reward 1 - KG",
            "Gold Coins: Hand Maze Chest Reward 2- KG",
            "Gold Coins: Hand Maze Chest Reward 3 - KG",
        ],
        ["Dan Hand", "Pond Room Valve"],
    )

    # dankenstein - no blocks

    # iron slugger - no blocks

    # Wulfrum Hall

    set_key_blocks(
        self,
        [
            "Life Bottle: Wulfrum Hall",
            "Equipment: Silver Shield Close To Vampire Room 2 - WH",
            "Energy Vial: Near Kitchen Stairs - WH",
            "Energy Vial: Left Room Of Entrance - WH",
            "Energy Vial: In Front Of Hall's Staircase - WH",
            "Gold Coins: Chest Close To Vampire Room 1 - WH",
            "Gold Coins: Chest in Vampire Room 3 - WH",
            "Gold Coins: Bag in Vampire Room 5 - WH",
            "Winston: Vampires - WH",
            "Chalice: Wulfrum Hall",
        ],
        ["Front Door Key"],
    )

    # Whitechapel

    set_key_blocks(self, ["Equipment: Silver Shield in Library - WC", "Chalice: Whitechapel - WC"], ["Library Key"])

    set_key_blocks(self, [], ["Beard", "Club Membership Card"])

    set_key_blocks(self, ["Key Item: Beard - WC"], ["Griffin Shield", "Unicorn Shield"])

    # Sewers - nothing

    # time machine - nothing

    # time machine - sewers

    set_key_blocks(self, ["Equipment: Good Lightning - Changing Room - TTMTS"], ["King Mullock's Key"])

    # nothing in the ripper

    # nothing blocked in cathedral spires

    # The Descent

    # need two of these.
    set_key_blocks(self, ["Key Item: Golden Cog in Hand Area - CSTD"], ["Golden Cog 1"])

    set_key_blocks(self, [], ["Golden Cog 2"])
