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


def has_lost_souls_required(self, count: int, state: CollectionState):
    return state.count("Lost Soul", self.player) >= count


def has_good_lightning(self, state: CollectionState):
    return state.has("Good Lightning", self.player)


def has_valves(self, count: int, state: CollectionState):
    return state.has("Progressive Valve", self.player, count)


def has_number_of_chalices(self, count, state: CollectionState):
    chalice_list = [
        "Chalice: The Museum",
        "Chalice: Kensington",
        "Chalice: The Freakshow",
        "Chalice: Greenwhich Observatory",
        "Chalice: Kew Gardens",
        "Chalice: Dankenstein",
        "Chalice: Wulfrum Hall",
        "Chalice: Whitechapel",
        "Chalice: The Sewers",
        "Chalice: The Ripper",
    ]

    collected_chalices = 0

    for chalice_location in chalice_list:
        if state.can_reach_location(chalice_location, self.player):
            collected_chalices += 1
    return collected_chalices >= count


def has_cleared_levels(self, count, state: CollectionState):
    level_list = [
        "Cleared: The Museum",
        "Cleared: Kensington",
        "Cleared: The Freakshow",
        "Cleared: Greenwich Observatory",
        "Cleared: Kew Gardens",
        "Cleared: Dankenstein",
        "Cleared: Wulfrum Hall",
        "Cleared: Whitechapel",
        "Cleared: The Sewers",
        "Cleared: The Ripper",
    ]

    completed_levels = 0

    for location in level_list:
        if state.can_reach_location(location, self.player):
            completed_levels += 1
    return completed_levels >= count


def set_key_blocks(self, locations: list[str], items: list[str]):
    for location in locations:
        for item in items:
            set_rule(self.get_location(location), lambda state: has_keyitems_required(self, [item], state))


def set_valve_block(self, count: int, locations: list[str]):
    for location in locations:
        add_rule(self.get_location(location), lambda state: has_valves(self, count, state))


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


def set_open_world_progression(self):
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Menu", state))
    set_rule(self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), lambda state: is_level_cleared(self, "The Museum", state))
    set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(self.get_entrance("Kensington -> The Tomb"), lambda state: is_level_cleared(self, "Kensington", state))
    set_rule(
        self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), lambda state: is_level_cleared(self, "Greenwich Observatory", state)
    )
    set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Wulfrum Hall -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), lambda state: is_level_cleared(self, "The Time Machine", state))
    set_rule(
        self.get_entrance("The Time Machine, The Sewers -> The Ripper"), lambda state: is_level_cleared(self, "The Time Machine, The Sewers", state)
    )
    set_rule(self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"), lambda state: is_level_cleared(self, "Cathedral Spires", state))


def set_keyitemsanity_progression(self):
    set_rule(self.get_entrance("Hub -> The Museum"), lambda state: is_level_cleared(self, "Menu", state))
    set_rule(
        self.get_entrance("The Museum -> Tyrannosaurus Wrecks"),
        lambda state: (
            has_keyitems_required(self, ["Museum Key", "Dinosaur Key", "Cannon Ball", "Torch"], state) and is_level_cleared(self, "The Museum", state)
        ),
    )
    set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(
        self.get_entrance("Hub -> The Museum"),
        lambda state: (
            is_level_cleared(self, "The Museum", state) and has_keyitems_required(self, ["Museum Key", "Dinosaur Key", "Cannon Ball", "Torch"], state)
        ),
    )
    set_rule(
        self.get_entrance("Hub -> Tyrannosaurus Wrecks"),
        lambda state: (
            is_level_cleared(self, "The Museum", state) and has_keyitems_required(self, ["Museum Key", "Dinosaur Key", "Cannon Ball", "Torch"], state)
        ),
    )
    set_rule(self.get_entrance("Hub -> Kensington"), lambda state: is_level_cleared(self, "Tyrannosaurus Wrecks", state))
    set_rule(
        self.get_entrance("Kensington -> The Tomb"),
        lambda state: (
            is_level_cleared(self, "Kensington", state) and has_keyitems_required(self, ["Depot Key", "Town House Key", "Pocket Watch"], state)
        ),
    )
    set_rule(
        self.get_entrance("The Tomb -> Hub"),
        lambda state: (
            is_level_cleared(self, "Kensington", state)
            and has_keyitems_required(self, ["Staff of Anubis", "Scroll of Sekhmet", "Tablet of Horus"], state)
        ),
    )
    set_rule(
        self.get_entrance("Hub -> The Freakshow"),
        lambda state: is_level_cleared(self, "The Tomb", state) and has_keyitems_required(self, ["Elephant Key 1", "Elephant Key 2"], state),
    )
    set_rule(
        self.get_entrance("Hub -> Greenwich Observatory"),
        lambda state: is_level_cleared(self, "The Freakshow", state) and has_dan_hand_skill(self, state),
    )
    set_rule(
        self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"),
        lambda state: is_level_cleared(self, "Greenwich Observatory", state) and has_keyitems_required(self, ["Bellows"], state),
    )
    set_rule(
        self.get_entrance("Hub -> Kew Gardens"),
        lambda state: (
            is_level_cleared(self, "Naval Academy", state) and has_valves(self, 3, state) and has_keyitems_required(self, ["Potting Shed Key"], state)
        ),
    )
    set_rule(self.get_entrance("Hub -> Dankenstein"), lambda state: is_level_cleared(self, "Kew Gardens", state))
    set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(self.get_entrance("Hub -> Iron Slugger"), lambda state: is_level_cleared(self, "Dankenstein", state))
    set_rule(
        self.get_entrance("Hub -> Wulfrum Hall"),
        lambda state: is_level_cleared(self, "Iron Slugger", state) and has_keyitems_required(self, ["Front Door Key"], state),
    )
    set_rule(self.get_entrance("Wulfrum Hall -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(self.get_entrance("Hub -> The Count"), lambda state: is_level_cleared(self, "Wulfrum Hall", state))
    set_rule(
        self.get_entrance("Hub -> Whitechapel"),
        lambda state: (
            is_level_cleared(self, "The Count", state)
            and has_keyitems_required(self, ["Library Key", "Club Membership Card", "Beard", "Unicorn Shield", "Griffin Shield"], state)
        ),
    )
    set_rule(
        self.get_entrance("Hub -> The Sewers"),
        lambda state: is_level_cleared(self, "Whitechapel", state) and has_keyitems_required(self, ["Poster"], state),
    )
    set_rule(
        self.get_entrance("Hub -> The Time Machine"),
        lambda state: (
            is_level_cleared(self, "The Sewers", state)
            and has_keyitems_required(
                self, ["Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"], state
            )
        ),
    )
    set_rule(
        self.get_entrance("The Time Machine -> The Time Machine, The Sewers"),
        lambda state: is_level_cleared(self, "The Time Machine", state) and has_keyitems_required(self, ["King Mullock's Key"], state),
    )
    set_rule(
        self.get_entrance("The Time Machine, The Sewers -> The Ripper"),
        lambda state: (
            is_level_cleared(self, "The Time Machine, The Sewers", state)
            and has_good_lightning(self, state)
            and has_keyitems_required(self, ["Time Stone"], state)
        ),
    )
    set_rule(
        self.get_entrance("Hub -> Cathedral Spires"),
        lambda state: is_level_cleared(self, "The Ripper", state) and has_lost_souls_required(self, 5, state),
    )
    set_rule(
        self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"),
        lambda state: (
            is_level_cleared(self, "Cathedral Spires", state)
            and has_lost_souls_required(self, 12, state)
            and has_keyitems_required(self, ["Golden Cog 1", "Golden Cog 2"], state)
        ),
    )
    set_rule(
        self.get_entrance("Cathedral Spires, The Descent -> The Demon"),
        lambda state: is_level_cleared(self, "Cathedral Spires, The Descent", state),
    )
    set_rule(self.get_entrance("Hub -> The Demon"), lambda state: is_level_cleared(self, "Cathedral Spires, The Descent", state))


def set_chalice_vanilla_rules(self):
    set_rule(self.get_location("Chalice Reward: Cane Stick"), lambda state: has_cleared_levels(self, 1, state))
    set_rule(self.get_location("Chalice Reward: Hammer"), lambda state: has_cleared_levels(self, 2, state))
    set_rule(self.get_location("Chalice Reward: Crossbow"), lambda state: has_cleared_levels(self, 3, state))
    set_rule(self.get_location("Chalice Reward: Axe"), lambda state: has_cleared_levels(self, 4, state))
    set_rule(self.get_location("Chalice Reward: Bombs"), lambda state: has_cleared_levels(self, 5, state))
    set_rule(self.get_location("Chalice Reward: Broadsword"), lambda state: has_cleared_levels(self, 6, state))
    set_rule(self.get_location("Chalice Reward: Lightning"), lambda state: has_cleared_levels(self, 7, state))
    set_rule(self.get_location("Chalice Reward: Blunderbuss"), lambda state: has_cleared_levels(self, 8, state))
    set_rule(self.get_location("Chalice Reward: Magic Sword"), lambda state: has_cleared_levels(self, 9, state))
    set_rule(self.get_location("Chalice Reward: Gatling Gun"), lambda state: has_cleared_levels(self, 10, state))


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
        ]
        + (["Chalice: The Museum"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Torch", "Cannon Ball", "Museum Key"],
    )

    set_key_blocks(
        self,
        ["Gold Coins: Tomb Room Left - TM", "Gold Coins: Tomb Room Right - TM", "Cleared: The Museum"],
        ["Torch", "Cannon Ball", "Museum Key", "Dinosaur Key"],
    )

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

    set_key_blocks(
        self,
        [
            "Key Item: Pocketwatch - KT",
            "Winston: Where the Spell was Cast - KT",
        ]
        + (["Chalice: Kensington"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Depot Key", "Town House Key"],
    )

    set_key_blocks(self, ["Winston: Museum Roof - KT", "Cleared: Kensington"], ["Depot Key", "Town House Key", "Pocket Watch"])

    set_key_blocks(self, [], ["Dan Hand"])

    # The Tomb

    set_key_blocks(self, ["Gold Coins: Hand Area Chest Ground Floor - TT", "Gold Coins: Hand Area Chest Upper Floor - TT"], ["Dan Hand"])
    set_key_blocks(self, ["Cleared: The Tomb"], ["Staff of Anubis", "Scroll of Sekhmet", "Tablet of Horus"])

    # The Freakshow

    set_key_blocks(
        self,
        ["Equipment: Copper Shield in Elephant Boss Arena - TF", "Cleared: The Freakshow"]
        + (["Chalice: The Freakshow"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Elephant Key 1", "Elephant Key 2"],
    )

    set_key_blocks(
        self,
        ["Gold Coins: Hand Area Chest - TF", "Gold Coins: Hand Area Hidden Chest Left - TF", "Gold Coins: Hand Area Hidden Chest Right - TF"],
        ["Dan Hand"],
    )

    # Greenwich Observatory

    set_key_blocks(
        self,
        [] + (["Chalice: Greenwich Observatory"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Dan Hand"],
    )

    set_key_blocks(
        self, ["Gold Coins: Hand Area Chest 1 - GO", "Gold Coins: Hand Area Chest 2 - GO", "Gold Coins: Hand Area Chest 3 - GO"], ["Dan Hand"]
    )

    # Naval Academy - bellows are end of level

    set_key_blocks(self, ["Cleared: Naval Academy"], ["Bellows"])

    # Kew Gardens

    # potting shed key for water tank valve
    # water tank valve give you the pond room valve
    # hothouse valve gives you the pond room

    set_key_blocks(self, ["Key Item: Water Tank Valve - KG"], ["Potting Shed Key"])

    set_key_blocks(
        self,
        ["Key Item: Pond Room Valve - KG"],
        [
            "Potting Shed Key",
        ],
    )
    set_key_blocks(self, ["Key Item: Hothouse Valve - KG", "Cleared: Kew Gardens"], ["Potting Shed Key"])
    set_valve_block(self, 1, ["Key Item: Pond Room Valve - KG"])
    set_valve_block(self, 3, ["Cleared: Kew Gardens"])
    set_valve_block(self, 2, ["Key Item: Hothouse Valve - KG", "Cleared: Kew Gardens"])

    set_key_blocks(
        self,
        ["Equipment: Silver Shield in Gauntlet Room - KG", "Gold Coins: Bag in Third Human Room - KG"]
        + (["Chalice: Kew Gardens"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Potting Shed Key"],
    )
    set_valve_block(self, 3, ["Equipment: Silver Shield in Gauntlet Room - KG", "Gold Coins: Bag in Third Human Room - KG"])

    set_key_blocks(
        self,
        [
            "Gold Coins: Hand Maze Chest - KG",
            "Gold Coins: Hand Maze Chest Reward 1 - KG",
            "Gold Coins: Hand Maze Chest Reward 2- KG",
            "Gold Coins: Hand Maze Chest Reward 3 - KG",
        ],
        ["Potting Shed Key", "Water Tank Valve", "Pond Room Valve", "Dan Hand"],
    )

    set_valve_block(
        self,
        2,
        [
            "Gold Coins: Hand Maze Chest - KG",
            "Gold Coins: Hand Maze Chest Reward 1 - KG",
            "Gold Coins: Hand Maze Chest Reward 2- KG",
            "Gold Coins: Hand Maze Chest Reward 3 - KG",
        ],
    )
    # dankenstein - no blocks
    set_key_blocks(
        self, [] + (["Chalice: Dankenstein"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []), []
    )
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
            "Cleared: Wulfrum Hall",
        ]
        + (["Chalice: Wulfrum Hall"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Front Door Key"],
    )

    # Whitechapel

    set_key_blocks(self, ["Equipment: Silver Shield in Library - WC"], ["Library Key"])

    set_key_blocks(self, ["Key Item: Beard - WC"], ["Griffin Shield", "Unicorn Shield"])

    set_key_blocks(
        self,
        ["Cleared: Whitechapel"]
        + (["Chalice: Whitechapel"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []),
        ["Beard", "Club Membership Card", "Griffin Shield", "Unicorn Shield"],
    )

    # Sewers - nothing

    set_key_blocks(
        self, [] + (["Chalice: The Sewers"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []), []
    )

    # time machine - nothing

    set_key_blocks(
        self,
        ["Cleared: The Time Machine"],
        ["Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"],
    )

    # time machine - sewers

    set_key_blocks(self, ["Equipment: Good Lightning - Changing Room - TTMTS", "Cleared: The Time Machine, The Sewers"], ["King Mullock's Key"])

    # nothing in the ripper

    set_key_blocks(
        self, [] + (["Chalice: The Ripper"] if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true else []), []
    )

    # nothing blocked in cathedral spires

    # The Descent

    # need two of these.
    set_key_blocks(self, ["Key Item: Golden Cog in Hand Area - CSTD"], ["Golden Cog 1"])
    set_key_blocks(self, ["Cleared: Cathedral Spires, The Descent"], ["Golden Cog 1", "Golden Cog 2"])
