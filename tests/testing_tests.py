#!/usr/bin/python

from nose.tools import *
from testing.game import Room

def test_room():
    desc = """This room has gold in it you can grab.
           There's a door to the north."""
    gold = Room("GoldRoom", desc)
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    assert_equal(gold.description, desc)

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south")

    center.add_path({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def  test_map():
    start = Room("Start", "You can go west and down a hole")
    west = Room("Trees", "There are trees here, you can go east")
    down = Room("Dungeon", "It's dark down here, you can go up")

    start.add_path({'west': west, 'down': down})
    west.add_path({'east': start})
    down.add_path({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
