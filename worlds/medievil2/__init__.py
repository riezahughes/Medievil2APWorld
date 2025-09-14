# world/dc2/__init__.py
from typing import Dict, Set, List

from BaseClasses import MultiWorld, Region, Item, Entrance, Tutorial, ItemClassification, CollectionState
from Options import Toggle

from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule, add_rule, add_item_rule

from .Items import Medievil2Item, Medievil2ItemCategory, item_dictionary, item_descriptions, BuildItemPool
from .Locations import Medievil2Location, Medievil2LocationCategory, location_tables, location_dictionary
from .Options import Medievil2Options, GoalOptions


class Medievil2Web(WebWorld):
    bug_report_page = ""
    theme = "stone"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Vagrant Story randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["RiezaHughes"],
    )

    tutorials = [setup_en]


class Medievil2World(World):
    """
    Medievil 2 is all about dan learning to be a ladies man and not lose his head.
    """

    game: str = "Medievil 2"
    explicit_indirect_conditions = False
    options_dataclass = Medievil2Options
    options: Medievil2Options
    topology_present: bool = True
    web = Medievil2Web()
    data_version = 0
    base_id = 1230000
    enabled_location_categories: Set[Medievil2LocationCategory]
    required_client_version = (0, 5, 0)
    item_name_to_id = Medievil2Item.get_name_to_id()
    location_name_to_id = Medievil2Location.get_name_to_id()
    item_name_groups = {}
    item_descriptions = item_descriptions

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.locked_items = []
        self.locked_locations = []
        self.main_path_locations = []
        self.enabled_location_categories = set()

    def generate_early(self):
        self.enabled_location_categories.add(Medievil2LocationCategory.KEY_ITEM)
        self.enabled_location_categories.add(Medievil2LocationCategory.CHEST)
        self.enabled_location_categories.add(Medievil2LocationCategory.BOSS)
        self.enabled_location_categories.add(Medievil2LocationCategory.CHALICE_PICKUP)
        self.enabled_location_categories.add(Medievil2LocationCategory.CHALICE_REWARD)
        self.enabled_location_categories.add(Medievil2LocationCategory.BOOK)
        self.enabled_location_categories.add(Medievil2LocationCategory.GOLD)
        self.enabled_location_categories.add(Medievil2LocationCategory.ENERGY)
        self.enabled_location_categories.add(Medievil2LocationCategory.LIFE_BOTTLE)
        self.enabled_location_categories.add(Medievil2LocationCategory.WEAPON)
        self.enabled_location_categories.add(Medievil2LocationCategory.LEVEL_END)

    def create_regions(self):
        # Create Regions
        regions: Dict[str, Region] = {}

        regions["Menu"] = self.create_region("Menu", [])

        list_of_regions = [
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

        # ALTER IF CHANGED BASED ON OPTIONS LIKE SO
        # if(self.options.include_ant_hill_in_checks.value == IncludeAntHillInChecksToggle.option_true):
        #     list_of_regions.insert(8, "Ant Hill")
        # else:
        #     location_tables.pop("Ant Hill")

        regions.update({region_name: self.create_region(region_name, location_tables[region_name]) for region_name in list_of_regions})

        def create_connection(from_region: str, to_region: str):
            connection = Entrance(self.player, f"{from_region} -> {to_region}", regions[from_region])
            regions[from_region].exits.append(connection)
            connection.connect(regions[to_region])

        # Vanilla Connections

        # Start of the Game
        create_connection("Menu", "The Museum")
        create_connection("The Museum", "Tyrannosaurus Wrecks")
        create_connection("The Museum", "Hub")

        # Professors Lab
        create_connection("Hub", "The Museum")
        create_connection("Hub", "Tyrannosaurus Wrecks")
        create_connection("Hub", "Kensington")
        create_connection("Hub", "The Tomb")
        create_connection("Hub", "The Freakshow")
        create_connection("Hub", "Greenwich Observatory ")
        create_connection("Hub", "Greenwich, Naval Academy")
        create_connection("Hub", "Kew Gardens")
        create_connection("Hub", "Dankenstein")
        create_connection("Hub", "Iron Slugger")
        create_connection("Hub", "Wulfrum Hall")
        create_connection("Hub", "The Count")
        create_connection("Hub", "Whitechapel")
        create_connection("Hub", "The Sewers")
        create_connection("Hub", "The Time Machine")
        create_connection("Hub", "The Time Machine, Sewers")
        create_connection("Hub", "The Ripper")
        create_connection("Hub", "Cathedral Spires")
        create_connection("Hub", "Cathedral Spires: The Descent")
        create_connection("Hub", "The Demon")

        # Probably more intricate level progression as you can go from one level to the next on some parts.

    # For each region, add the associated locations retrieved from the corresponding location_table
    def create_region(self, region_name, location_table) -> Region:
        new_region = Region(region_name, self.player, self.multiworld)

        for location in location_table:
            # CAN ALTER INDIVIDUAL LOCATIONS TO REMOVE THEM FROM THE POOL HERE
            # if self.options.include_ant_hill_in_checks.value == IncludeAntHillInChecksToggle.option_false and location.name == "Energy Vial: Megwynne Stormbinder - HH":
            #     continue
            # if self.options.include_chalices_in_checks.value == IncludeChalicesInChecksToggle.option_false and location.category == MedievilLocationCategory.CHALICE:
            #     continue
            if location.category in self.enabled_location_categories:
                new_location = Medievil2Location(
                    self.player,
                    location.name,
                    location.category,
                    location.default_item,
                    self.location_name_to_id[location.name],
                    new_region,
                )
            else:
                event_item = self.create_item(location.default_item)
                new_location = Medievil2Location(self.player, location.name, location.category, location.default_item, None, new_region)
                event_item.code = None
                # Cast the item to the correct type
                if isinstance(event_item, Medievil2Item):
                    new_location.place_locked_item(event_item)
            # Uncomment to print all locations
            # print(f"{self.location_name_to_id[location.name]}: {location.name}")
            new_region.locations.append(new_location)

        self.multiworld.regions.append(new_region)
        return new_region

    def create_items(self):
        randomized_location_count = 0
        for location in self.multiworld.get_locations(self.player):
            if not location.locked and location.address is not None:
                randomized_location_count += 1

        print(f"Requesting itempool size for randomized locations: {randomized_location_count}")

        # Call BuildItemPool to get a list of item NAMES (strings)
        item_names_to_add = BuildItemPool(randomized_location_count, self.options)

        generated_items: List[Item] = []
        for item_name in item_names_to_add:
            new_item = self.create_item(item_name)
            generated_items.append(new_item)

        print(f"Created item pool size: {len(generated_items)}")

        # Add the generated Medievil2Item objects to the multiworld's item pool
        self.multiworld.itempool.extend(generated_items)

    def create_item(self, name: str) -> Item:
        item_data = item_dictionary.get(name)

        if not item_data:
            # Fallback for unknown items. This indicates a data inconsistency.
            print(f"Warning: Attempted to create unknown item: {name}. Falling back to filler.")
            return Medievil2Item(name, ItemClassification.filler, None, self.player)

        # Determine the Archipelago ItemClassification based on Medievil2ItemData.
        item_classification: ItemClassification

        if item_data.progression or item_data.category == Medievil2ItemCategory.KEY_ITEMS:
            item_classification = ItemClassification.progression
        elif (
            item_data.category == Medievil2ItemCategory.MELEE_WEAPONS
            or item_data.category == Medievil2ItemCategory.RANGED_WEAPONS
            or item_data.category == Medievil2ItemCategory.SHIELDS
        ):
            item_classification = ItemClassification.useful
        else:  # Default for FILLER or other categories not explicitly useful/progression
            item_classification = ItemClassification.filler

        return Medievil2Item(name, item_classification, Medievil2Item.get_name_to_id()[name], self.player)

    def get_filler_item_name(self) -> str:
        return "Gold: (50)"  # this clearly needs looked into

    def set_rules(self) -> None:
        def is_level_cleared(self, location: str, state: CollectionState):
            return state.can_reach_location("Cleared: " + location, self.player)

        def is_boss_defeated(self, boss: str, state: CollectionState):  # can used later
            return state.has("Boss: " + boss, self.player, 1)

        def has_keyitems_required(self, items: list[str], state: CollectionState):
            passed_check = True
            for item in items:
                if state.has("Key Item: " + item, self.player, 1) is False:
                    passed_check = False
            return passed_check

        for region in self.multiworld.get_regions(self.player):
            for location in region.locations:
                set_rule(location, lambda state: True)

        if self.options.goal.value == GoalOptions.DEFEAT_DEMON:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Cleared: The Demon", self.player)
        # Map rules

        # ITEM SPECIFIC RULES

        # for location in self.multiworld.get_locations(self.player):
        #     if location.parent_region.name in ["Dan's Crypt", "Locked Items DC"]:
        #         add_item_rule(location, lambda item: item.name != "Equipment: Hammer")

        # options rule setup

        # set_rule(self.get_entrance("Enchanted Earth -> Ant Hill"))

        # Get a birds eye view of everything

        # from Utils import visualize_regions
        # state = self.multiworld.get_all_state(False)
        # state.update_reachable_regions(self.player)
        # visualize_regions(self.get_region("Menu"), "medievil_layout.puml", show_entrance_names=True,
        #                 regions_to_highlight=state.reachable_regions[self.player])

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        name_to_medievil_code = {item.name: item.m_code for item in item_dictionary.values()}
        # Create the mandatory lists to generate the player's output file
        items_id = []
        items_address = []
        locations_id = []
        locations_address = []
        locations_target = []
        for location in self.multiworld.get_filled_locations():
            if location.item is not None:
                if location.item.player == self.player:
                    # we are the receiver of the item
                    items_id.append(location.item.code)
                    items_address.append(name_to_medievil_code[location.item.name])

            if location.player == self.player:
                # we are the sender of the location check
                locations_address.append(item_dictionary[location_dictionary[location.name].default_item].m_code)
                locations_id.append(location.address)
                if location.item is not None:
                    if location.item.player == self.player:
                        locations_target.append(name_to_medievil_code[location.item.name])
                    else:
                        locations_target.append(0)

        slot_data = {
            "options": {
                "guaranteed_items": self.options.guaranteed_items.value,
                "goal": self.options.goal.value,
                "deathlink": self.options.deathlink.value,
                "progression_option": self.options.progression_option.value,
            },
            "seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "slot": self.multiworld.player_name[self.player],  # to connect to server
            "base_id": self.base_id,  # to merge location and items lists
            "locationsId": locations_id,
            "locationsAddress": locations_address,
            "locationsTarget": locations_target,
            "itemsId": items_id,
            "itemsAddress": items_address,
        }

        return slot_data
