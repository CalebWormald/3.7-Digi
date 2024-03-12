import sys
import time
#######################################################
####  Straded in Time -- Caleb Wormald -- 6/3/2024 ####
#######################################################

## To play Straded in Time simply run the pyton file and then enjoy ##

WIDTH = 4
inventory = []
pos = 6
        
map = []
loc_list = [
            {"pos":"0", "direction":"ES", "desc":""}, {"pos":"1", "direction":"EW", "desc":""}, {"pos":"2", "direction":"WS", "desc":""}, {"pos":"3", "direction":"", "desc":""},
            {"pos":"4", "direction":"NS", "desc":""}, {"pos":"5", "direction":"", "desc":""}, {"pos":"6", "direction":"NE", "desc":"You have arived at you Time Machine."}, {"pos":"7", "direction":"WS", "desc":""},
            {"pos":"8", "direction":"NE", "desc":""}, {"pos":"9", "direction":"WS", "desc":""}, {"pos":"10", "direction":"", "desc":""}, {"pos":"11", "direction":"NS", "desc":""},
            {"pos":"12", "direction":"", "desc":""}, {"pos":"13", "direction":"NE", "desc":""}, {"pos":"14", "direction":"EW", "desc":""}, {"pos":"15", "direction":"NW", "desc":""}
            ]
        
#adding the writing effect to the Question and other text 
def text_effects(string):
    """adds a text effect by writing out string one character at a time"""
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
        

class Location:
    def __init__(self, pos, desc, direction, item=None):
        self.pos = pos
        self.desc = desc
        self.direction = direction
        self.item = item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        next_room = getattr(self.current_room, direction, None)
        if next_room:
            self.current_room = next_room
            print("You are now in the {self.current_room.desc}.")
            print(self.current_room.desc)
        else:
            print("You can't go that way!")


for loc_info in loc_list:
    location = Location(loc_info["pos"], loc_info["desc"], loc_info["direction"], loc_info.get("item"))
    map.append(location)
