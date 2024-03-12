import sys
import time
#######################################################
####  Straded in Time -- Caleb Wormald -- 6/3/2024 ####
#######################################################

## To play Straded in Time simply run the pyton file and then enjoy ##

WIDTH = 10
inventory = []
        
map = []
loc_list = [
            {"pos":"", "direction":"NE", "desc":""}, {"pos":"", "direction":"EW", "desc":""}, {"pos":"", "direction":"WS", "desc":""}, {"pos":"", "direction":"", "desc":""},
            {"pos":"", "direction":"NS", "desc":""}, {"pos":"", "direction":"", "desc":""}, {"pos":"", "direction":"NE", "desc":"You have arived at you Time Machine."}, {"pos":"", "direction":"WS", "desc":""},
            {"pos":"", "direction":"NE", "desc":""}, {"pos":"", "direction":"WS", "desc":"", "item":"Resipercating_Dingle_Arm"}, {"pos":"", "direction":"", "desc":""}, {"pos":"", "direction":"NS", "desc":""},
            {"pos":"", "direction":"", "desc":""}, {"pos":"", "direction":"NE", "desc":""}, {"pos":"", "direction":"EW", "desc":""}, {"pos":"", "direction":"N", "desc":""}
            ]

#adding the writing effect to the starting blurb
def text_effect(string):
    """adds a text effect by writing out string one character at a time"""
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
        
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


for loc_info in loc_list:
    location = Location(loc_info["pos"], loc_info["desc"], loc_info["direction"], loc_info.get("item"))
    map.append(location)
