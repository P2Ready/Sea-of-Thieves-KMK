from __future__ import annotations

import functools
from typing import List

import random

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SeaOfThievesArchipelagoOptions:
    sea_of_thieves_include_pvp: SeaOfThievesIncludePVP
    sea_of_thieves_include_fishing: SeaOfThievesIncludeFish
    sea_of_thieves_include_tall_tales: SeaOfThievesIncludeTallTales
    sea_of_thieves_include_emergent_events: SeaOfThievesIncludeEmergentEvents
    sea_of_thieves_include_social: SeaOfThievesIncludeSocial

class SeaOfThievesGame(Game):
    name = "Sea of Thieves"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.PS5
    ]

    is_adult_only_or_unrated = False

    options_cls = SeaOfThievesArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            # Gold Hoarder Standard Voyages
            GameObjectiveTemplate(
                label="Complete a Gold Hoarder GH_VOYAGE voyage",
                data={
                    "GH_VOYAGE": (self.gh_voyages, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Order of Souls Standard Voyages
            GameObjectiveTemplate(
                label="Complete an Order of Souls OOS_VOYAGE voyage",
                data={
                    "OOS_VOYAGE": (self.oos_voyages, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Merchant Alliance Standard Voyages
            GameObjectiveTemplate(
                label="Complete a Merchant Alliance MA_VOYAGE voyage",
                data={
                    "MA_VOYAGE": (self.ma_voyages, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Hunter's Call Standard Voyages
            GameObjectiveTemplate(
                label="Complete a Hunter's Call HC_VOYAGE voyage",
                data={
                    "HC_VOYAGE": (self.hc_voyages, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Athena's Fortune Standard Voyages
            GameObjectiveTemplate(
                label="Complete an Athena's Fortune AF_VOYAGE voyage",
                data={
                    "AF_VOYAGE": (self.af_voyages, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3
            ),
            # Faction Raid voyages
            GameObjectiveTemplate(
                label="Complete a(n) FACTION RAID raid voyage",
                data={
                    "FACTION": (self.pve_factions, 1),
                    "RAID": (self.raids, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Emissary grade 5 objectives
            GameObjectiveTemplate(
                label="Reach Emissary Rank 5 as FACTION",
                data={
                    "FACTION": (self.factions, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            # World Event Objectives
            GameObjectiveTemplate(
                label="Complete INT world events",
                data={
                    "INT": (functools.partial(self.short_int, 2, 5), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Complete a(n) WORLD_EVENT world event",
                data={
                    "WORLD_EVENT": (self.world_events, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Message in a bottle voyage
            GameObjectiveTemplate(
                label="Complete a Message in a Bottle voyage",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Sunken Kingdom
            GameObjectiveTemplate(
                label="Complete the SUNKEN_KINGDOM",
                data={
                    "SUNKEN_KINGDOM": (self.sunken_kingdom, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Sanctuary of the Banished
            GameObjectiveTemplate(
                label="Plunder a Santuary of the Banished in the Devil's Roar",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Big Turn In
            GameObjectiveTemplate(
                label="Earn INT gold from a single turn-in",
                data={
                    "INT": (functools.partial(self.long_int, 100000, 1000000, 100000), 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3
            ),
            # Fort of the Damned
            GameObjectiveTemplate(
                label="Complete and successfully plunder the Fort of the Damned",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=3
            ),
            # Smuggler's Run
            GameObjectiveTemplate(
                label="Successfully complete a Smuggler's Run voyage",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            # Orb of Secrets
            GameObjectiveTemplate(
                label="Retrieve and sell an Orb of Secrets",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
        ]

        # Option-based objectives
        # PVP option
        if self.include_pvp:
            template_list = [
                # Hourglass Matches
                GameObjectiveTemplate(
                    label="Win INT hourglass matches as the HG_FACTION",
                    data={
                        "INT": (functools.partial(self.short_int, 2, 5), 1),
                        "HG_FACTION": (self.hg_factions, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                GameObjectiveTemplate(
                    label="Send INT enemy pirates to the Ferry of the Damned",
                    data={
                        "INT": (functools.partial(self.short_int, 4, 10), 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                # World PVP
                GameObjectiveTemplate(
                    label="Sink INT ships outside of Hourglass matches",
                    data={
                        "INT": (functools.partial(self.short_int, 2, 5), 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                # Reaper Standard Voyages
                GameObjectiveTemplate(
                    label="Complete a Reaper's Bones RB_VOYAGE voyage",
                    data={
                        "RB_VOYAGE": (self.rb_voyages, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                # Siren Skull
                GameObjectiveTemplate(
                    label="Sell a Skull of Siren Song",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                # Reaper's Chest/Bounty
                GameObjectiveTemplate(
                    label="Sell a Reaper's Chest or Reaper's Bounty",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
            ]
            for i in template_list:
                templates.append(i)
        # Fishing option
        if self.include_fishing:
            template_list = [
                GameObjectiveTemplate(
                    label="Catch and sell a FISH",
                    data={
                        "FISH": (self.fish, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                GameObjectiveTemplate(
                    label="Make INT gold selling fish",
                    data={
                        "INT": (functools.partial(self.long_int, 5000, 50000, 5000), 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                )
            ]
            for i in template_list:
                templates.append(i)

        # Tall Tale option
        if self.include_tall_tales:
            templates.append(
                GameObjectiveTemplate(
                    label="Complete the TALL_TALE Tall Tale",
                    data={
                        "TALL_TALE": (self.tall_tales, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                )
            )

        # Emergent Event option
        if self.include_emergent_events:
            templates.append(
                GameObjectiveTemplate(
                    label="Defeat a EMERGENT_EVENT",
                    data={
                        "EMERGENT_EVENT": (self.emergent_events, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                )
            )

        # Social option
        if self.include_social:
            template_list = [
                GameObjectiveTemplate(
                    label="Make a new friend",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                GameObjectiveTemplate(
                    label="Ride on another crew's ship for INT minutes",
                    data={
                        "INT": (functools.partial(self.short_int, 5, 15), 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                ),
                GameObjectiveTemplate(
                    label="Form an alliance with INT other ships",
                    data={
                        "INT": (functools.partial(self.short_int, 1, 3), 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3
                )
            ]
            for i in template_list:
                templates.append(i)

        return templates

    @property
    def include_pvp(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_pvp.value)
    
    @property
    def include_fishing(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_fishing.value)
    
    @property
    def include_tall_tales(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_tall_tales.value)
    
    @property
    def include_emergent_events(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_emergent_events.value)
    
    @property
    def include_social(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_social.value)

    #@functools.cached_property
    @staticmethod
    def gh_voyages() -> List[str]:
        return [
            "Treasure Map",
            "Riddle Quest",
            "Treasure Vault"
        ]
    
    @staticmethod
    def oos_voyages() -> List[str]:
        return [
            "Skeleton Bounty",
            "Ghost Armada"
        ]
    
    @staticmethod
    def ma_voyages() -> List[str]:
        return [
            "Lost Shipment",
            "Cargo Run",
            "Merchant Contract"
        ]
    
    @staticmethod
    def hc_voyages() -> List[str]:
        return [
            "Fishing",
            "Hunting"
        ]
    
    @staticmethod
    def rb_voyages() -> List[str]:
        return [
            "Ritual",
            "Search"
        ]
    
    @staticmethod
    def af_voyages() -> List[str]:
        return [
            "Voyage of Legends",
            "Legend of the Veil",
            "Legendary Search"
        ]
    
    @staticmethod
    def short_int(a,b) -> List[str]:
        return [
            str(random.randint(a,b))
        ]
    
    @staticmethod
    def long_int(a,b,c) -> List[str]:
        return[
            str(random.randrange(a,b+1,c))
        ]
    
    @staticmethod
    def world_events() -> List[str]:
        return[
            "Skeleton Fort",
            "Skeleteon Fleet",
            "Reaper Fortress",
            "Fort of Fortune",
            "Ghost Fleet",
            "Ashen Winds"
        ]
    
    @staticmethod
    def sunken_kingdom() -> List[str]:
        return[
            "Shrine of the Coral Tomb",
            "Shrine of Ocean's Fortune",
            "Shrine of Ancient Tears",
            "Shrine of Tribute",
            "Shrine of Hungering",
            "Shrine of Flooded Embrace",
            "Treasury of Sunken Shores",
            "Treasury of the Lost Ancients",
            "Treasury of the Secret Wilds"
        ]
    
    @functools.cached_property
    def base_factions(self) -> List[str]:
        return [
            "Gold Hoarders",
            "Order of Souls",
            "Merchant Alliance",
            "Hunter's Call",
            "Athena's Fortune"
        ]
    
    @functools.cached_property
    def pvp_factions(self) -> List[str]:
        return[
            "Reaper's Bones"
        ]
    
    def pve_factions(self) -> List[str]:
        pve_factions: List[str] = self.base_factions[:]

        return pve_factions

    def factions(self) -> List[str]:
        factions: List[str] = self.base_factions[:]

        if self.include_pvp:
            factions.extend(self.pvp_factions)

        return factions

    @staticmethod
    def raids() -> List[str]:
        return [
            "Sea Fort",
            "Skeleton Camp",
            "Ashen Lord",
            "Skeleton Armada",
            "Ghost Fleet",
            "Skeleton Fort"
        ]
    
    @staticmethod
    def hg_factions() -> List[str]:
        return [
            "Guardians of Fortune",
            "Servants of the Flame"
        ]
    
    @staticmethod
    def fish() -> List[str]:
        return[
            "Ruby Splashtail",
            "Sunny Splashtail",
            "Indigo Splashtail",
            "Umber Splashtail",
            "Seafoam Splashtail",
            "Charcoal Pondie",
            "Orchid Pondie",
            "Bronze Pondie",
            "Bright Pondie",
            "Moonsky Pondie",
            "Stone Islehopper",
            "Moss Islehopper",
            "Honey Islehopper",
            "Raven Islehopper",
            "Amethyst Islehopper",
            "Almond Ancientscale",
            "Sapphire Ancientscale",
            "Smoke Ancientscale",
            "Bone Ancientscale",
            "Starshine Ancientscale",
            "Olive Plentifin",
            "Amber Plentifin",
            "Cloudy Plentifin",
            "Bonedust Plentifin",
            "Watery Plentifin",
            "Russet Wildsplash",
            "Sandy Wildsplash",
            "Ocean Wildsplash",
            "Muddy Wildsplash",
            "Coral Wildsplash",
            "Ashen Devilfish",
            "Seashell Devilfish",
            "Lava Devilfish",
            "Forsaken Devilfish",
            "Firelight Devilfish",
            "Jade Battlegill",
            "Sky Battlegill",
            "Rum Battlegill",
            "Sand Battlegill",
            "Bittersweet Battlegill",
            "Rose Wrecker",
            "Sun Wrecker",
            "Blackcloud Wrecker",
            "Snow Wrecker",
            "Moon Wrecker",
            "Ancient Stormfish",
            "Shores Stormfish",
            "Wild Stormfish",
            "Shadow Stormfish",
            "Twilight Stormfish"
        ]
    
    @staticmethod
    def tall_tales() -> List[str]:
        return [
            "The Shroudbreaker",
            "The Cursed Rogue",
            "The Legendary Storyteller",
            "Stars of a Thief",
            "Wild Rose",
            "The Art of the Trickster",
            "The Fate of the Morningstar",
            "Revenge of the Morningstar",
            "Shores of Gold",
            "The Seabound Soul",
            "Heart of Fire",
            "A Pirate's Life",
            "The Sunken Pearl",
            "Captains of the Damned",
            "Dark Brethren",
            "Lords of the Sea",
            "Journey to Melee Island",
            "The Quest for Guybrush",
            "The Lair of LeChuck"
        ]
    
    @staticmethod
    def emergent_events() -> List[str]:
        return [
            "Kraken",
            "Megalodon",
            "Skeleton Sloop",
            "Skeleton Galleon"
        ]
    
# Archipelago Options
class SeaOfThievesIncludePVP(Toggle):
    """
    Indicates if PVP based objectives (hourglass, world pvp) should be generated
    """

    display_name = "Sea of Thieves PVP Objectives"

class SeaOfThievesIncludeFish(Toggle):
    """
    Indicates if non-voyage fishing checks should be included (catch specific fish, earn X gold off of fish)
    """

    display_name = "Sea of Thieves Fishing Objectives"

class SeaOfThievesIncludeTallTales(Toggle):
    """
    Indicates if Tall Tale objectives should be included (recommended to have access to all beforehand!)
    """

    display_name = "Sea of Thieves Tall Tale Objectives"

class SeaOfThievesIncludeEmergentEvents(Toggle):
    """
    Indicates whether emergent events (krakens, megalodons, skeleton ships) should be included. These objectives can be hard to purposefully check, and require a bit of RARE luck.
    """

    display_name = "Sea of Thieves Emergent Event Objectives"

class SeaOfThievesIncludeSocial(Toggle):
    """
    Indicates whether more 'social' checks should be included. Sea of Thieves is a social game, and incentivizing this can be a lot of fun! These objectives may be fairly subjective.
    """

    display_name = "Sea of Thieves Social Objectives"