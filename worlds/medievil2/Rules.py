import dataclasses
from typing import TYPE_CHECKING

from typing_extensions import override

from BaseClasses import CollectionState, Entrance, Location
from rule_builder.rules import CanReachLocation, Has, HasAll, Rule
from .Options import IncludeChalicesInChecksToggle

if TYPE_CHECKING:
    from . import Medievil2World


def cleared(level: str) -> Rule:
    return CanReachLocation(f"Cleared: {level}")


def key_items(*names: str) -> Rule:
    return HasAll(*names)


DAN_HAND = Has("Dan Hand")
GOOD_LIGHTNING = Has("Good Lightning")

# The fixed list of "Cleared: X" locations tracked by HasNumberOfClearedLevels. Only these
# 10 specific levels count -- Tyrannosaurus Wrecks, The Tomb, Naval Academy, Iron Slugger,
# Cathedral Spires (and its Descent), and The Demon are NOT tracked.
TRACKED_LEVELS: tuple[str, ...] = (
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
)


@dataclasses.dataclass()
class HasNumberOfClearedLevels(Rule["Medievil2World"], game="Medievil 2"):
    """Checks that at least `count` of the 10 tracked "Cleared: X" LOCATIONS are reachable."""

    count: int

    @override
    def _instantiate(self, world: "Medievil2World") -> Rule.Resolved:
        return self.Resolved(
            TRACKED_LEVELS,
            self.count,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    @override
    def __str__(self) -> str:
        return f"HasNumberOfClearedLevels({self.count})"

    class Resolved(Rule.Resolved):
        tracked_levels: tuple[str, ...]
        count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            completed_levels = 0
            for location_name in self.tracked_levels:
                if state.can_reach_location(location_name, self.player):
                    completed_levels += 1
            return completed_levels >= self.count

        @override
        def location_dependencies(self) -> dict[str, set[int]]:
            return {name: {id(self)} for name in self.tracked_levels}

        @override
        def __str__(self) -> str:
            return f"Has {self.count} cleared levels"


def layer_rule(world: "Medievil2World", spot: "Location | Entrance", rule: Rule) -> None:
    existing = spot.access_rule
    if existing is Location.access_rule or existing is Entrance.access_rule:
        world.set_rule(spot, rule)
        return
    resolved = rule.resolve(world)
    world.register_rule_dependencies(resolved)
    spot.access_rule = lambda state, e=existing, n=resolved: e(state) and n(state)


def set_key_blocks(self: "Medievil2World", locations: list[str], items: list[str]) -> None:
    for location in locations:
        self.set_rule(self.get_location(location), key_items(*items))


def set_valve_block(self: "Medievil2World", count: int, locations: list[str]) -> None:
    for location in locations:
        layer_rule(self, self.get_location(location), Has("Progressive Valve", count))


def set_vanilla_level_progression(self: "Medievil2World") -> None:
    self.set_rule(self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), cleared("The Museum"))
    self.set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), cleared("Tyrannosaurus Wrecks"))
    self.set_rule(self.get_entrance("Hub -> Tyrannosaurus Wrecks"), cleared("The Museum"))
    self.set_rule(self.get_entrance("Hub -> Kensington"), cleared("Tyrannosaurus Wrecks"))
    self.set_rule(self.get_entrance("Kensington -> The Tomb"), cleared("Kensington"))
    self.set_rule(self.get_entrance("Hub -> The Freakshow"), cleared("The Tomb"))
    self.set_rule(self.get_entrance("Hub -> Greenwich Observatory"), cleared("The Freakshow") & DAN_HAND)
    self.set_rule(self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), cleared("Greenwich Observatory"))
    self.set_rule(self.get_entrance("Hub -> Kew Gardens"), cleared("Naval Academy"))
    self.set_rule(self.get_entrance("Hub -> Dankenstein"), cleared("Kew Gardens"))
    self.set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), cleared("Dankenstein"))
    self.set_rule(self.get_entrance("Hub -> Iron Slugger"), cleared("Dankenstein"))
    self.set_rule(self.get_entrance("Hub -> Wulfrum Hall"), cleared("Iron Slugger"))
    self.set_rule(self.get_entrance("Wulfrum Hall -> The Count"), cleared("Wulfrum Hall"))
    self.set_rule(self.get_entrance("Hub -> The Count"), cleared("Wulfrum Hall"))
    self.set_rule(self.get_entrance("Hub -> Whitechapel"), cleared("The Count"))
    self.set_rule(self.get_entrance("Hub -> The Sewers"), cleared("Whitechapel"))
    self.set_rule(self.get_entrance("Hub -> The Time Machine"), cleared("The Sewers"))
    self.set_rule(self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), cleared("The Time Machine"))
    self.set_rule(self.get_entrance("The Time Machine, The Sewers -> The Ripper"), cleared("The Time Machine, The Sewers"))
    self.set_rule(self.get_entrance("Hub -> Cathedral Spires"), cleared("The Ripper"))
    self.set_rule(self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"), cleared("Cathedral Spires"))
    self.set_rule(self.get_entrance("Hub -> The Demon"), cleared("Cathedral Spires, The Descent"))


def set_open_world_progression(self: "Medievil2World") -> None:
    self.set_rule(self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), cleared("The Museum"))
    self.set_rule(self.get_entrance("Tyrannosaurus Wrecks -> Hub"), cleared("Tyrannosaurus Wrecks"))
    self.set_rule(self.get_entrance("Kensington -> The Tomb"), cleared("Kensington"))
    self.set_rule(self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), cleared("Greenwich Observatory"))
    self.set_rule(self.get_entrance("Dankenstein -> Iron Slugger"), cleared("Dankenstein"))
    self.set_rule(self.get_entrance("Wulfrum Hall -> The Count"), cleared("Wulfrum Hall"))
    self.set_rule(self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), cleared("The Time Machine"))
    self.set_rule(self.get_entrance("The Time Machine, The Sewers -> The Ripper"), cleared("The Time Machine, The Sewers"))
    self.set_rule(self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"), cleared("Cathedral Spires"))


def set_keyitemsanity_progression(self: "Medievil2World") -> None:
    layer_rule(self, self.get_entrance("The Museum -> Tyrannosaurus Wrecks"), key_items("Museum Key", "Dinosaur Key", "Cannon Ball", "Torch"))
    layer_rule(self, self.get_entrance("Hub -> Tyrannosaurus Wrecks"), key_items("Museum Key", "Dinosaur Key", "Cannon Ball", "Torch"))
    layer_rule(self, self.get_entrance("Kensington -> The Tomb"), key_items("Depot Key", "Town House Key", "Pocket Watch"))
    layer_rule(
        self,
        self.get_entrance("The Tomb -> Hub"),
        cleared("Kensington") & key_items("Staff of Anubis", "Scroll of Sekhmet", "Tablet of Horus"),
    )
    layer_rule(self, self.get_entrance("Hub -> The Freakshow"), key_items("Elephant Key 1", "Elephant Key 2"))
    layer_rule(self, self.get_entrance("Hub -> Greenwich Observatory"), DAN_HAND)
    layer_rule(self, self.get_entrance("Greenwich Observatory -> Greenwich, Naval Academy"), key_items("Bellows"))
    layer_rule(self, self.get_entrance("Hub -> Kew Gardens"), Has("Progressive Valve", 3) & key_items("Potting Shed Key"))
    layer_rule(self, self.get_entrance("Hub -> Wulfrum Hall"), key_items("Front Door Key"))
    layer_rule(
        self,
        self.get_entrance("Hub -> Whitechapel"),
        key_items("Library Key", "Club Membership Card", "Beard", "Unicorn Shield", "Griffin Shield"),
    )
    layer_rule(self, self.get_entrance("Hub -> The Sewers"), key_items("Poster"))
    layer_rule(
        self,
        self.get_entrance("Hub -> The Time Machine"),
        key_items("Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"),
    )
    layer_rule(self, self.get_entrance("The Time Machine -> The Time Machine, The Sewers"), key_items("King Mullock's Key"))
    layer_rule(
        self,
        self.get_entrance("The Time Machine, The Sewers -> The Ripper"),
        GOOD_LIGHTNING & key_items("Time Stone"),
    )
    layer_rule(
        self,
        self.get_entrance("Cathedral Spires -> Cathedral Spires, The Descent"),
        Has("Lost Soul", 5),
    )
    layer_rule(
        self,
        self.get_entrance("Cathedral Spires, The Descent -> The Demon"),
        cleared("Cathedral Spires, The Descent") & Has("Lost Soul", 12),
    )
    layer_rule(self, self.get_entrance("Hub -> The Demon"), Has("Lost Soul", 12))


def set_chalice_vanilla_rules(self: "Medievil2World") -> None:
    for i, name in enumerate(
        (
            "Cane Stick",
            "Hammer",
            "Crossbow",
            "Axe",
            "Bombs",
            "Broadsword",
            "Lightning",
            "Blunderbuss",
            "Magic Sword",
            "Gatling Gun",
        ),
        start=1,
    ):
        self.set_rule(self.get_location(f"Chalice Reward: {name}"), HasNumberOfClearedLevels(i))


def set_item_rules(self: "Medievil2World") -> None:
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

    if self.options.include_chalices_in_checks == IncludeChalicesInChecksToggle.option_true:
        set_key_blocks(self, ["Chalice: Greenwich Observatory"], ["Dan Hand"])

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
        ["Potting Shed Key", "Dan Hand"],
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

    # time machine - nothing

    set_key_blocks(
        self,
        ["Cleared: The Time Machine"],
        ["Time Machine Piece (Contact Room)", "Time Machine Piece (Earth Room)", "Time Machine Piece (Space Room)"],
    )

    # time machine - sewers

    set_key_blocks(self, ["Equipment: Good Lightning - Changing Room - TTMTS", "Cleared: The Time Machine, The Sewers"], ["King Mullock's Key"])

    # nothing in the ripper

    # nothing blocked in cathedral spires

    # The Descent

    # need two of these.
    self.set_rule(self.get_location("Key Item: Golden Cog in Hand Area - CSTD"), Has("Progressive Golden Cog", 1))
    self.set_rule(self.get_location("Cleared: Cathedral Spires, The Descent"), Has("Progressive Golden Cog", 2))
