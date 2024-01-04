import os
import sys
from models.room import Room
from models.display import Display
from models.inspectable import Inspectable
from models.item import Item
from models.player import Player


title_screen = Display(
    title = "Welcome to our escape game!",
    content = "In this game, you will need to escape the house using clues and items you find in each room.",
    options = {},
    width = 28
)

help_screen = Display(
    title="Help Page", 
    content="Each room you visit will give you a list of inspectable locations within the room that you may click to to search for clues to escape.",
    options={},
    width=28, 
)

inventory_screen = Display(
    title = "",
    content = "",
    options = {},
    width = 28
)

introduction_screen = Display(
    title = "Name select",
    content = "What is your name?",
    width = 28,
)
kitchen_description = """You wake up, dazed and confused to find that you are in a mysterious, unknown kitchen that hasn't been used in a few years. You see a SINK with a pile of dirty dishes, some CABINETS with most of the cabinet doors barely hanging by the hinges, a TRASH CAN that is in bad need of being taken out, and a door with a square-shaped pad-lock that is locked. To escape, you will need to inspect each of these to find the clue that unlocks the door. What would you like to inspect first?"""
kitchen_screen = Display(
    title = "Kitchen",
    content = kitchen_description,
    options = {},
    width = 28,
)

inspect_screen = Display(
    title = "Kitchen",
    content = "What would you like to inspect?",
    options = {},
    width = 28
)
dining_room_description = """You enter the next room which is a run down version of what used to be a nice looking dining room. You see a TABLE with a bunch of clutter on it, some CHAIRS, a busted in CHINA CABINET, and a BAR CART. There is also a door with a lock with a symbol of a circle on it. Find the key for this lock!"""
dining_room_screen = Display(
    title = "Dining Room",
    content = dining_room_description,
    options = {},
    width = 28,
)

dining_room_inspect = Display(
    title = "Dining Room",
    content = "What would you like to inspect?",
    width = 28
)

bedroom_description = """You now enter the bedroom. You notice that there is a broken BED against the far wall, a CLOSET with the doors torn off, a DESK with a mess of papers scattered everywhere and a door with a giant triangle shaped lock. You also notice that the door has been barred off with wooden PLANKS, preventing anyone from accessing the door. This must be the way out!"""
bedroom_screen = Display(
    title = "Bedroom",
    content = bedroom_description,
    options = {},
    width = 28,
)
bedroom_inspect = Display(
    title = "Bedroom",
    content = "What would you like to inspect?",
    width = 28
)

escape_screen = Display(
    title = "END GAME",
    content = "Congratulations! You have escaped the house!",
    options = {},
    width = 28,
)

inspectable_screen = Display(
    title = "",
    content = "",
    options = {},
    width = 28,
)


##### Room seeds ######
Room.drop_table()
Room.create_table()

kitchen = Room("Kitchen", locked = False, description = kitchen_description, screen =  kitchen_screen)
# kitchen.add_to_table()


dining_room = Room("Dining Room", locked = False, description = dining_room_description, screen = dining_room_screen)


bedroom = Room("Bedroom", locked = False, description = bedroom_description , screen = bedroom_screen)
# bedroom.add_to_table()


###### Display seeds + helper functions ######


##### Inspectable seeds ######
Inspectable.drop_table()
Inspectable.create_table()

sink_description = """You look inside the sink and find a key with a square shaped end."""
sink = Inspectable("Sink", kitchen, False, sink_description)

cabinet_description = """You check the cabinets but you don't find any clues or items that will help you unlock the door."""
cabinet = Inspectable("Cabinet", kitchen, False, cabinet_description)

trash_can_description = """You search through the trash can and find a crowbar. Maybe this will help you in your journey."""
trash_can = Inspectable("Trash Can", kitchen, False, trash_can_description)

square_lock_description = """You approch the square shaped lock. Do you want to use your key?"""
square_lock = Inspectable("Square Lock", kitchen, False, square_lock_description)

table_description = """You search the table in the middle of the room but do not find any clues."""
table = Inspectable("Table", dining_room, False, table_description)

chairs_description = """You look on each chair and do not find any clues or items."""
chairs = Inspectable("Chairs", dining_room, False, chairs_description)

china_cabinet_description = """You search through the China cabinet to find nothing more than broken dishes."""
china_cabinet = Inspectable("China Cabinet", dining_room, False, china_cabinet_description)

bar_cart_description = """You search through the bottles and glassware and find a key inside a decanter. Upon opening the decanter and retrieving the key, you notice that it has a circle symbol on it. This must be for the lock on the door!"""
bar_cart = Inspectable("Bar Cart", dining_room, False, bar_cart_description)

circle_lock_description = """You approach the door with the circle symbol. Do you want to use the key that you found?"""
circle_lock = Inspectable("Circle Lock", dining_room, False, circle_lock_description)

bed_description = """You pull the blankets off the bed but do not find any usefull clues."""
bed = Inspectable("Bed", bedroom, False, bed_description)

closet_description = """You make your way to the closet and search through the tattered clothes. You find an old baseball bat that you might could use."""
closet = Inspectable("Closet", bedroom, False, closet_description)

desk_description = """You search through the papers on the desk but don't find anything you can use. You open a drawer and find a key with the triangle symbol! You are almost free!"""
desk = Inspectable("Desk", bedroom, False, desk_description)

planks_description = """You run to the door with with the triangle shaped key in excitment about getting out but you remember you need to get through the planks. What do you use to get through these?"""
planks = Inspectable("Planks", bedroom, False, planks_description)

triangle_lock_description = """You finally get through the planks and are now at the triangle shaped lock! Would you like to use the key?"""
triangle_lock = Inspectable("Triangle Lock", bedroom, False, triangle_lock_description)

###### Item seeds ######
Item.drop_table()
Item.create_table()

square_key_description = """A key with a square shaped end that fits to a specific lock."""
square_key = Item("Square Key", sink, square_key_description)

crowbar_description = """A crowbar used for prying."""
crowbar = Item("Crowbar", trash_can, crowbar_description)

circle_key_description = """A key with a circle shaped end that fits to a specific lock."""
circle_key = Item("Circle Key", bar_cart, circle_key_description)

baseball_bat_description = """A baseball bat used for hitting."""
baseball_bat = Item("Baseball Bat", closet, baseball_bat_description)

triangle_key_description = """A key with a triangle shaped end that fits to a specific lock."""
triangle_key = Item("Triangle Key", desk, triangle_key_description)

###### Player seed ######
player = Player("No name", kitchen)

    
# def get_current_location_screen(desired_location):
#     player.move(desired_location, "You cannot use this door")
#     get_screen(player.current_location.screen)
            

