import sys
import time
#######################################################
####  Straded in Time -- Caleb Wormald -- 6/3/2024 ####
#######################################################

## To play Straded in Time simply run the pyton file and then enjoy ##

WIDTH = 4
inventory = []
pos = 6
        
loc_list = [
            {"pos":"0", "direction":"ES", "desc":""}, {"pos":"1", "direction":"EW", "desc":""}, {"pos":"2", "direction":"WS", "desc":""}, {"pos":"3", "direction":"", "desc":""},
            {"pos":"4", "direction":"NS", "desc":""}, {"pos":"5", "direction":"", "desc":""}, {"pos":"6", "direction":"NE", "desc":"You have arived at you Time Machine."}, {"pos":"7", "direction":"WS", "desc":""},
            {"pos":"8", "direction":"NE", "desc":""}, {"pos":"9", "direction":"WS", "desc":""}, {"pos":"10", "direction":"", "desc":""}, {"pos":"11", "direction":"NS", "desc":""},
            {"pos":"12", "direction":"", "desc":""}, {"pos":"13", "direction":"NE", "desc":""}, {"pos":"14", "direction":"EW", "desc":""}, {"pos":"15", "direction":"NW", "desc":""}
            ]
        
#adding the writing effect to the Question and other text 
def text_effect(string):
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
        def can_move(pos, direction):
            """Checks to see which direction you can go using pos and then compares that direction you have chosen.
            If you have chosen a direction that is listed it allows you to go in that direction, otherwise you
            don't move and are told to choose a new direction."""
            if direction in loc_list[pos]["direction"]:
                return True
            else:
                return False

class Player:
    def __init__(self, pos, current_room):
        self.pos = pos
        self.direction = direction
        self.inventory = []

    # movement function
    def move(pos, direction):
        """takes pos and direction then works out new pos"""
        if direction == "N":
            pos = pos - WIDTH
            text_effects(" You have moved North\n")
        elif direction == "E":
            pos = pos + 1
            text_effects(" You have moved East\n")
        elif direction == "W":
            pos = pos - 1
            text_effects(" You have moved West\n")
        elif direction == "S":
            pos = pos + WIDTH
            text_effects(" You have moved South\n")
        else:
            text_effects(" Please enter a direction")
        return pos


##for loc_info in loc_list:
##    location = Location(loc_info["pos"], loc_info["desc"], loc_info["direction"], loc_info.get("item"))

#game starts here
def start():
    """runs and calls other functions to run the game"""
    #starting blurb
    print("""    Welcome to Stranded in Time. 
    You were testing a time machine in the year 2040 the test succeeded 
    and you have been sent back in time to the age of the dinosaurs.
    Your only way to escape and back to 2040, your time machine was blowup 
    Now you must find all of the parts without being eaten by the many dinosaurs that roam the canyon.
    So let the game begin.""")
    game = True
    pos = 6
    #reapeating quesiton and moving
    while game:
       direction = input("You can go {}. \nWhich direction would you like to go? ".format(loc_list[pos]["direction"])).upper()
       if loc_list[pos]["direction"] != "":
           if player.can_move(direction):
               player.move(direction)
           else:
               print("Choose a different direction.")
       else:
           print("No valid direction in this location.")


    while game:
        direction = input("    You can go {}. \n Which direction would you like to go? ".format(loc_list[pos]["direction"])).upper()
        #call can_move method
        if can_move(pos, direction) == True:
            pos = move(pos, direction)
        else:
            print("    Choose a different direction.")


   
