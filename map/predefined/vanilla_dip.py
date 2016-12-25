from copy import deepcopy

from map.map import Map, SupplyCenterMap, OwnershipMap
from player.unit import Unit
from player.unit import UnitTypes

_VANILLA_DIP_MAP_CACHE = None
def generate_map():
    global _VANILLA_DIP_MAP_CACHE
    if not _VANILLA_DIP_MAP_CACHE:
        territory_descriptors = [
            # Sea Territories
            {'name': 'Adriatic Sea'},
            {'name': 'Aegean Sea'},
            {'name': 'Baltic Sea'},
            {'name': 'Barents Sea'},
            {'name': 'Black Sea'},
            {'name': 'Eastern Mediterranean Sea'},
            {'name': 'English Channel'},
            {'name': 'Gulf of Bothnia'},
            {'name': 'Gulf of Lyon'},
            {'name': 'Helgoland Bight'},
            {'name': 'Ionian Sea'},
            {'name': 'Irish Sea'},
            {'name': 'Mid-Atlantic Ocean'},
            {'name': 'North Atlantic Ocean'},
            {'name': 'North Sea'},
            {'name': 'Norwegian Sea'},
            {'name': 'Skagerrak'},
            {'name': 'Tyrrhenian Sea'},
            {'name': 'Western Mediterranean Sea'},

            # Land Territories
            {'name': 'Albania',        'coasts': ['Albania Coast']},
            {'name': 'Apulia',         'coasts': ['Apulia Coast']},
            {'name': 'Ankara',         'coasts': ['Ankara Coast']},
            {'name': 'Armenia',        'coasts': ['Armenia Coast']},
            {'name': 'Belgium',        'coasts': ['Belgium Coast']},
            {'name': 'Berlin',         'coasts': ['Berlin Coast']},
            {'name': 'Bohemia',        'coasts': []},
            {'name': 'Brest',          'coasts': ['Brest Coast']},
            {'name': 'Budapest',       'coasts': []},
            {'name': 'Bulgaria',       'coasts': ['Bulgaria North Coast', 'Bulgaria South Coast']},
            {'name': 'Burgundy',       'coasts': []},
            {'name': 'Clyde',          'coasts': ['Clyde Coast']},
            {'name': 'Constantinople', 'coasts': ['Constantinople Coast']},
            {'name': 'Denmark',        'coasts': ['Denmark Coast']},
            {'name': 'Edinburgh',      'coasts': ['Edinburgh Coast']},
            {'name': 'Finland',        'coasts': ['Finland Coast']},
            {'name': 'Gascony',        'coasts': ['Gascony Coast']},
            {'name': 'Galicia',        'coasts': []},
            {'name': 'Greece',         'coasts': ['Greece Coast']},
            {'name': 'Holland',        'coasts': ['Holland Coast']},
            {'name': 'Kiel',           'coasts': ['Kiel Coast']},
            {'name': 'London',         'coasts': ['London Coast']},
            {'name': 'Liverpool',      'coasts': ['Liverpool Coast']},
            {'name': 'Livonia',        'coasts': ['Livonia Coast']},
            {'name': 'Marseilles',     'coasts': ['Marseilles Coast']},
            {'name': 'Moscow',         'coasts': []},
            {'name': 'Munich',         'coasts': []},
            {'name': 'Naples',         'coasts': ['Naples Coast']},
            {'name': 'Norway',         'coasts': ['Norway Coast']},
            {'name': 'Paris',          'coasts': []},
            {'name': 'Picardy',        'coasts': ['Picardy Coast']},
            {'name': 'Piedmont',       'coasts': ['Piedmont Coast']},
            {'name': 'Portugal',       'coasts': ['Portugal Coast']},
            {'name': 'Prussia',        'coasts': ['Prussia Coast']},
            {'name': 'Rome',           'coasts': ['Rome Coast']},
            {'name': 'Ruhr',           'coasts': []},
            {'name': 'North Africa',   'coasts': ['North Africa Coast']},
            {'name': 'Rumania',        'coasts': ['Rumania Coast']},
            {'name': 'Serbia',         'coasts': []},
            {'name': 'Silesia',        'coasts': []},
            {'name': 'Sevastopol',     'coasts': ['Sevastopol Coast']},
            {'name': 'Smyrna',         'coasts': ['Smyrna Coast']},
            {'name': 'Spain',          'coasts': ['Spain North Coast', 'Spain South Coast']},
            {'name': 'St. Petersburg', 'coasts': ['St. Petersburg North Coast', 'St. Petersburg South Coast']},
            {'name': 'Sweden',         'coasts': ['Sweden Coast']},
            {'name': 'Syria',          'coasts': ['Syria Coast']},
            {'name': 'Trieste',        'coasts': ['Trieste Coast']},
            {'name': 'Tunis',          'coasts': ['Tunis Coast']},
            {'name': 'Tuscany',        'coasts': ['Tuscany Coast']},
            {'name': 'Tyrolia',        'coasts': []},
            {'name': 'Ukraine',        'coasts': []},
            {'name': 'Venice',         'coasts': ['Venice Coast']},
            {'name': 'Vienna',         'coasts': []},
            {'name': 'Warsaw',         'coasts': []},
            {'name': 'Wales',          'coasts': ['Wales Coast']},
            {'name': 'Yorkshire',      'coasts': ['Yorkshire Coast']},
        ]
        adjacencies = [
            # Sea Adjacencies
            ('North Atlantic Ocean',      'Norwegian Sea'),
            ('North Atlantic Ocean',      'Mid-Atlantic Ocean'),
            ('North Atlantic Ocean',      'Irish Sea'),
            ('North Atlantic Ocean',      'Clyde Coast'),
            ('North Atlantic Ocean',      'Liverpool Coast'),
            ('Norwegian Sea',             'North Sea'),
            ('Norwegian Sea',             'Barents Sea'),
            ('Norwegian Sea',             'Clyde Coast'),
            ('Norwegian Sea',             'Edinburgh Coast'),
            ('Norwegian Sea',             'Norway Coast'),
            ('Barents Sea',               'Norway Coast'),
            ('Barents Sea',               'St. Petersburg North Coast'),
            ('Mid-Atlantic Ocean',        'Irish Sea'),
            ('Mid-Atlantic Ocean',        'English Channel'),
            ('Mid-Atlantic Ocean',        'Western Mediterranean Sea'),
            ('Mid-Atlantic Ocean',        'North Africa Coast'),
            ('Mid-Atlantic Ocean',        'Spain North Coast'),
            ('Mid-Atlantic Ocean',        'Spain South Coast'),
            ('Mid-Atlantic Ocean',        'Portugal Coast'),
            ('Mid-Atlantic Ocean',        'Gascony Coast'),
            ('Mid-Atlantic Ocean',        'Brest Coast'),
            ('Irish Sea',                 'English Channel'),
            ('Irish Sea',                 'Liverpool Coast'),
            ('Irish Sea',                 'Wales Coast'),
            ('English Channel',           'Wales Coast'),
            ('English Channel',           'London Coast'),
            ('English Channel',           'North Sea'),
            ('English Channel',           'Belgium Coast'),
            ('English Channel',           'Picardy Coast'),
            ('English Channel',           'Brest Coast'),
            ('North Sea',                 'Skagerrak'),
            ('North Sea',                 'Helgoland Bight'),
            ('North Sea',                 'Norway Coast'),
            ('North Sea',                 'Holland Coast'),
            ('North Sea',                 'Belgium Coast'),
            ('North Sea',                 'London Coast'),
            ('North Sea',                 'Yorkshire Coast'),
            ('North Sea',                 'Edinburgh Coast'),
            ('North Sea',                 'Denmark Coast'),
            ('Skagerrak',                 'Norway Coast'),
            ('Skagerrak',                 'Sweden Coast'),
            ('Skagerrak',                 'Denmark Coast'),
            ('Helgoland Bight',           'Denmark Coast'),
            ('Helgoland Bight',           'Kiel Coast'),
            ('Helgoland Bight',           'Holland Coast'),
            ('Baltic Sea',                'Sweden Coast'),
            ('Baltic Sea',                'Gulf of Bothnia'),
            ('Baltic Sea',                'Livonia Coast'),
            ('Baltic Sea',                'Prussia Coast'),
            ('Baltic Sea',                'Berlin Coast'),
            ('Baltic Sea',                'Kiel Coast'),
            ('Baltic Sea',                'Denmark Coast'),
            ('Gulf of Bothnia',           'Finland Coast'),
            ('Gulf of Bothnia',           'St. Petersburg South Coast'),
            ('Gulf of Bothnia',           'Livonia Coast'),
            ('Gulf of Bothnia',           'Sweden Coast'),
            ('Western Mediterranean Sea', 'Spain South Coast'),
            ('Western Mediterranean Sea', 'Gulf of Lyon'),
            ('Western Mediterranean Sea', 'Tyrrhenian Sea'),
            ('Western Mediterranean Sea', 'Tunis Coast'),
            ('Western Mediterranean Sea', 'North Africa Coast'),
            ('Gulf of Lyon',              'Marseilles Coast'),
            ('Gulf of Lyon',              'Spain South Coast'),
            ('Gulf of Lyon',              'Piedmont Coast'),
            ('Gulf of Lyon',              'Tuscany Coast'),
            ('Gulf of Lyon',              'Tyrrhenian Sea'),
            ('Tyrrhenian Sea',            'Tuscany Coast'),
            ('Tyrrhenian Sea',            'Rome Coast'),
            ('Tyrrhenian Sea',            'Naples Coast'),
            ('Tyrrhenian Sea',            'Ionian Sea'),
            ('Tyrrhenian Sea',            'Tunis Coast'),
            ('Ionian Sea',                'Tunis Coast'),
            ('Ionian Sea',                'Naples Coast'),
            ('Ionian Sea',                'Apulia Coast'),
            ('Ionian Sea',                'Adriatic Sea'),
            ('Ionian Sea',                'Albania Coast'),
            ('Ionian Sea',                'Greece Coast'),
            ('Ionian Sea',                'Aegean Sea'),
            ('Ionian Sea',                'Eastern Mediterranean Sea'),
            ('Aegean Sea',                'Greece Coast'),
            ('Aegean Sea',                'Bulgaria South Coast'),
            ('Aegean Sea',                'Constantinople Coast'),
            ('Aegean Sea',                'Smyrna Coast'),
            ('Aegean Sea',                'Eastern Mediterranean Sea'),
            ('Eastern Mediterranean Sea', 'Smyrna Coast'),
            ('Eastern Mediterranean Sea', 'Syria Coast'),
            ('Adriatic Sea',              'Apulia Coast'),
            ('Adriatic Sea',              'Venice Coast'),
            ('Adriatic Sea',              'Trieste Coast'),
            ('Adriatic Sea',              'Albania Coast'),
            ('Black Sea',                 'Constantinople Coast'),
            ('Black Sea',                 'Bulgaria North Coast'),
            ('Black Sea',                 'Rumania Coast'),
            ('Black Sea',                 'Sevastopol Coast'),
            ('Black Sea',                 'Armenia Coast'),
            ('Black Sea',                 'Ankara Coast'),

            # Coast Adjacencies
            ('Clyde Coast',          'Edinburgh Coast'),
            ('Clyde Coast',          'Liverpool Coast'),
            ('Edinburgh Coast',      'Yorkshire Coast'),
            ('Liverpool Coast',      'Wales Coast'),
            ('Wales Coast',          'London Coast'),
            ('Yorkshire Coast',      'London Coast'),
            ('Norway Coast',         'Sweden Coast'),
            ('Norway Coast',         'St. Petersburg North Coast'),
            ('Sweden Coast',         'Denmark Coast'),
            ('Sweden Coast',         'Finland Coast'),
            ('Denmark Coast',        'Kiel Coast'),
            ('Finland Coast',        'St. Petersburg South Coast'),
            ('Livonia Coast',        'St. Petersburg South Coast'),
            ('Livonia Coast',        'Prussia Coast'),
            ('Prussia Coast',        'Berlin Coast'),
            ('Berlin Coast',         'Kiel Coast'),
            ('Kiel Coast',           'Holland Coast'),
            ('Holland Coast',        'Belgium Coast'),
            ('Belgium Coast',        'Picardy Coast'),
            ('Picardy Coast',        'Brest Coast'),
            ('Brest Coast',          'Gascony Coast'),
            ('Gascony Coast',        'Spain North Coast'),
            ('Portugal Coast',       'Spain North Coast'),
            ('Portugal Coast',       'Spain South Coast'),
            ('Marseilles Coast',     'Spain South Coast'),
            ('Marseilles Coast',     'Piedmont Coast'),
            ('Piedmont Coast',       'Tuscany Coast'),
            ('Tuscany Coast',        'Rome Coast'),
            ('Rome Coast',           'Naples Coast'),
            ('Naples Coast',         'Apulia Coast'),
            ('Apulia Coast',         'Venice Coast'),
            ('North Africa Coast',   'Tunis Coast'),
            ('Venice Coast',         'Trieste Coast'),
            ('Trieste Coast',        'Albania Coast'),
            ('Albania Coast',        'Greece Coast'),
            ('Greece Coast',         'Bulgaria South Coast'),
            ('Constantinople Coast', 'Bulgaria South Coast'),
            ('Constantinople Coast', 'Bulgaria North Coast'),
            ('Constantinople Coast', 'Ankara Coast'),
            ('Constantinople Coast', 'Smyrna Coast'),
            ('Smyrna Coast',         'Syria Coast'),
            ('Ankara Coast',         'Armenia Coast'),
            ('Armenia Coast',        'Sevastopol Coast'),
            ('Sevastopol Coast',     'Rumania Coast'),
            ('Rumania Coast',        'Bulgaria North Coast'),

            # Land Adjacencies
            ('Apulia', 'Venice'),
            ('Albania', 'Trieste'),
            ('Clyde', 'Edinburgh'),
            ('Clyde', 'Liverpool'),
            ('Liverpool', 'Edinburgh'),
            ('Liverpool', 'Yorkshire'),
            ('Liverpool', 'Wales'),
            ('Edinburgh', 'Yorkshire'),
            ('Wales', 'London'),
            ('Wales', 'Yorkshire'),
            ('Yorkshire', 'London'),
            ('Norway', 'Sweden'),
            ('Norway', 'Finland'),
            ('Norway', 'St. Petersburg'),
            ('Sweden', 'Finland'),
            ('Sweden', 'Denmark'),
            ('Finland', 'St. Petersburg'),
            ('Denmark', 'Kiel'),
            ('St. Petersburg', 'Livonia'),
            ('St. Petersburg', 'Moscow'),
            ('Livonia', 'Moscow'),
            ('Livonia', 'Warsaw'),
            ('Livonia', 'Prussia'),
            ('Moscow', 'Warsaw'),
            ('Moscow', 'Ukraine'),
            ('Moscow', 'Sevastopol'),
            ('Warsaw', 'Prussia'),
            ('Warsaw', 'Silesia'),
            ('Warsaw', 'Galicia'),
            ('Warsaw', 'Ukraine'),
            ('Ukraine', 'Galicia'),
            ('Ukraine', 'Sevastopol'),
            ('Ukraine', 'Rumania'),
            ('Sevastopol', 'Armenia'),
            ('Sevastopol', 'Rumania'),
            ('Armenia', 'Syria'),
            ('Armenia', 'Smyrna'),
            ('Armenia', 'Ankara'),
            ('Ankara', 'Smyrna'),
            ('Ankara', 'Constantinople'),
            ('Smyrna', 'Constantinople'),
            ('Smyrna', 'Syria'),
            ('Constantinople', 'Bulgaria'),
            ('Bulgaria', 'Rumania'),
            ('Bulgaria', 'Greece'),
            ('Bulgaria', 'Serbia'),
            ('Rumania', 'Galicia'),
            ('Rumania', 'Budapest'),
            ('Rumania', 'Serbia'),
            ('Greece', 'Albania'),
            ('Greece', 'Serbia'),
            ('Serbia', 'Albania'),
            ('Serbia', 'Trieste'),
            ('Serbia', 'Budapest'),
            ('Budapest', 'Trieste'),
            ('Budapest', 'Vienna'),
            ('Budapest', 'Galicia'),
            ('Galicia', 'Vienna'),
            ('Galicia', 'Bohemia'),
            ('Galicia', 'Silesia'),
            ('Silesia', 'Bohemia'),
            ('Silesia', 'Munich'),
            ('Silesia', 'Berlin'),
            ('Silesia', 'Prussia'),
            ('Prussia', 'Berlin'),
            ('Berlin', 'Kiel'),
            ('Berlin', 'Munich'),
            ('Munich', 'Kiel'),
            ('Munich', 'Ruhr'),
            ('Munich', 'Burgundy'),
            ('Munich', 'Tyrolia'),
            ('Munich', 'Bohemia'),
            ('Bohemia', 'Tyrolia'),
            ('Bohemia', 'Vienna'),
            ('Vienna', 'Tyrolia'),
            ('Vienna', 'Trieste'),
            ('Trieste', 'Venice'),
            ('Trieste', 'Tyrolia'),
            ('Kiel', 'Ruhr'),
            ('Kiel', 'Holland'),
            ('Ruhr', 'Holland'),
            ('Holland', 'Belgium'),
            ('Belgium', 'Ruhr'),
            ('Belgium', 'Burgundy'),
            ('Belgium', 'Picardy'),
            ('Burgundy', 'Ruhr'),
            ('Burgundy', 'Marseilles'),
            ('Burgundy', 'Gascony'),
            ('Burgundy', 'Paris'),
            ('Burgundy', 'Picardy'),
            ('Picardy', 'Paris'),
            ('Picardy', 'Brest'),
            ('Brest', 'Gascony'),
            ('Brest', 'Paris'),
            ('Gascony', 'Paris'),
            ('Gascony', 'Marseilles'),
            ('Gascony', 'Spain'),
            ('Spain', 'Portugal'),
            ('Spain', 'Marseilles'),
            ('North Africa', 'Tunis'),
            ('Marseilles', 'Piedmont'),
            ('Piedmont', 'Tuscany'),
            ('Piedmont', 'Venice'),
            ('Piedmont', 'Tyrolia'),
            ('Tuscany', 'Venice'),
            ('Tuscany', 'Rome'),
            ('Rome', 'Venice'),
            ('Rome', 'Apulia'),
            ('Rome', 'Naples'),
            ('Naples', 'Apulia'),
            ('Venice', 'Tyrolia'),
        ]

        _VANILLA_DIP_MAP_CACHE = Map(territory_descriptors, adjacencies)
    return deepcopy(_VANILLA_DIP_MAP_CACHE)

_VANILLA_DIP_SUPPLY_CENTER_MAP_CACHE = None
def generate_supply_center_map():
    global _VANILLA_DIP_SUPPLY_CENTER_MAP_CACHE
    if not _VANILLA_DIP_SUPPLY_CENTER_MAP_CACHE:
        supply_centers = {
            'Edinburgh',
            'London',
            'Liverpool',
            'Norway',
            'Sweden',
            'St. Petersburg',
            'Denmark',
            'Belgium',
            'Holland',
            'Kiel',
            'Berlin',
            'Munich',
            'Brest',
            'Paris',
            'Marseilles',
            'Portugal',
            'Spain',
            'Tunis',
            'Naples',
            'Rome',
            'Venice',
            'Trieste',
            'Vienna',
            'Budapest',
            'Serbia',
            'Greece',
            'Bulgaria',
            'Rumania',
            'Constantinople',
            'Ankara',
            'Smyrna',
            'Sevastopol',
            'Moscow',
            'Warsaw',
        }
        _VANILLA_DIP_SUPPLY_CENTER_MAP_CACHE = SupplyCenterMap(generate_map(), supply_centers)
    return deepcopy(_VANILLA_DIP_SUPPLY_CENTER_MAP_CACHE)

_VANILLA_DIP_HOME_TERRITORY_CACHE = None
def generate_home_territories():
    global _VANILLA_DIP_HOME_TERRITORY_CACHE
    if not _VANILLA_DIP_HOME_TERRITORY_CACHE:
        _VANILLA_DIP_HOME_TERRITORY_CACHE = {
            'England': {
                'Liverpool',
                'London',
                'Edinburgh',
            },
            'France': {
                'Brest',
                'Paris',
                'Marseilles',
            },
            'Germany': {
                'Kiel',
                'Berlin',
                'Munich',
            },
            'Italy': {
                'Venice',
                'Rome',
                'Naples',
            },
            'Russia': {
                'St. Petersburg',
                'Moscow',
                'Warsaw',
                'Sevastopol',
            },
            'Austria': {
                'Vienna',
                'Budapest',
                'Trieste',
            },
            'Turkey': {
                'Constantinople',
                'Ankara',
                'Smyrna',
            },
        }
    return deepcopy(_VANILLA_DIP_HOME_TERRITORY_CACHE)

_VANILLA_DIP_STARTING_OWNERSHIP_MAP_CACHE = None
def generate_starting_ownership_map():
    global _VANILLA_DIP_STARTING_OWNERSHIP_MAP_CACHE
    if not _VANILLA_DIP_STARTING_OWNERSHIP_MAP_CACHE:
        # Vanilla Diplomacy uses the home territories as starting ownership
        _VANILLA_DIP_STARTING_OWNERSHIP_MAP_CACHE = OwnershipMap(
            generate_supply_center_map(),
            generate_home_territories(),
            generate_home_territories(),
        )
    return _VANILLA_DIP_STARTING_OWNERSHIP_MAP_CACHE

_VANILLA_DIP_STARTING_PLAYER_UNITS_CACHE = None
def generate_starting_player_units():
    global _VANILLA_DIP_STARTING_PLAYER_UNITS_CACHE
    if not _VANILLA_DIP_STARTING_PLAYER_UNITS_CACHE:
        # Vanilla Diplomacy uses the home territories as starting ownership
        _VANILLA_DIP_STARTING_PLAYER_UNITS_CACHE = {
            'England': {
                Unit(UnitTypes.TROOP, 'Liverpool'),
                Unit(UnitTypes.FLEET, 'London Coast'),
                Unit(UnitTypes.FLEET, 'Edinburgh Coast'),
            },
            'France': {
                Unit(UnitTypes.FLEET, 'Brest Coast'),
                Unit(UnitTypes.TROOP, 'Paris'),
                Unit(UnitTypes.TROOP, 'Marseilles'),
            },
            'Germany': {
                Unit(UnitTypes.FLEET, 'Kiel Coast'),
                Unit(UnitTypes.TROOP, 'Berlin'),
                Unit(UnitTypes.TROOP, 'Munich'),
            },
            'Italy': {
                Unit(UnitTypes.TROOP, 'Venice'),
                Unit(UnitTypes.TROOP, 'Rome'),
                Unit(UnitTypes.FLEET, 'Naples Coast'),
            },
            'Russia': {
                Unit(UnitTypes.FLEET, 'St. Petersburg South Coast'),
                Unit(UnitTypes.TROOP, 'Moscow'),
                Unit(UnitTypes.TROOP, 'Warsaw'),
                Unit(UnitTypes.FLEET, 'Sevastopol Coast'),
            },
            'Austria': {
                Unit(UnitTypes.TROOP, 'Vienna'),
                Unit(UnitTypes.TROOP, 'Budapest'),
                Unit(UnitTypes.FLEET, 'Trieste Coast'),
            },
            'Turkey': {
                Unit(UnitTypes.TROOP, 'Constantinople'),
                Unit(UnitTypes.FLEET, 'Ankara Coast'),
                Unit(UnitTypes.TROOP, 'Smyrna'),
            },
        }
    return deepcopy(_VANILLA_DIP_STARTING_PLAYER_UNITS_CACHE)