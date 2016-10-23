import pytest

from map.predefined.vanilla_dip import generate_map
from player.command.command import SupportCommand
from player.player import Player
from player.unit import UnitTypes

def test_support_destination_not_adjacent():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Trieste', 'unit_type': UnitTypes.TROOP},
        {'territory_name': 'Budapest', 'unit_type': UnitTypes.TROOP},
    ]
    player = Player("Austria", map, starting_configuration)

    with pytest.raises(AssertionError):
        SupportCommand(player, player.units[0], player.units[1], 'Galicia')

def test_support_landlocked_destination_with_fleet():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Rumania Coast', 'unit_type': UnitTypes.FLEET},
        {'territory_name': 'Serbia', 'unit_type': UnitTypes.TROOP},
    ]
    player = Player("Turkey", map, starting_configuration)

    with pytest.raises(AssertionError):
        SupportCommand(player, player.units[0], player.units[1], 'Budapest')

def test_support_supported_unit_not_adjacent():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Paris', 'unit_type': UnitTypes.TROOP},
        {'territory_name': 'Ruhr', 'unit_type': UnitTypes.TROOP},
    ]
    player = Player("France", map, starting_configuration)

    command = SupportCommand(player, player.units[0], player.units[1], 'Burgundy')

    assert command.unit.position == 'Paris'
    assert command.supported_unit.position == 'Ruhr'
    assert command.destination == 'Burgundy'

def test_support_supported_unit_adjacent():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Tuscany', 'unit_type': UnitTypes.TROOP},
        {'territory_name': 'Rome', 'unit_type': UnitTypes.TROOP},
    ]
    player = Player("Italy", map, starting_configuration)

    command = SupportCommand(player, player.units[0], player.units[1], 'Venice')

    assert command.unit.position == 'Tuscany'
    assert command.supported_unit.position == 'Rome'
    assert command.destination == 'Venice'

def test_support_troop_to_parent_of_coast_with_fleet():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Gulf of Lyon', 'unit_type': UnitTypes.FLEET},
        {'territory_name': 'Tuscany', 'unit_type': UnitTypes.TROOP},
    ]
    player = Player("France", map, starting_configuration)

    command = SupportCommand(player, player.units[0], player.units[1], 'Piedmont')

    assert command.unit.position == 'Gulf of Lyon'
    assert command.supported_unit.position == 'Tuscany'
    assert command.destination == 'Piedmont'

def test_support_fleet_to_coast_with_troop():
    map = generate_map()
    starting_configuration = [
        {'territory_name': 'Finland', 'unit_type': UnitTypes.TROOP},
        {'territory_name': 'Baltic Sea', 'unit_type': UnitTypes.FLEET},
    ]
    player = Player("France", map, starting_configuration)

    command = SupportCommand(player, player.units[0], player.units[1], 'Sweden Coast')

    assert command.unit.position == 'Finland'
    assert command.supported_unit.position == 'Baltic Sea'
    assert command.destination == 'Sweden Coast'