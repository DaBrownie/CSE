class Room(object):
    def __init__(self, name, north, south, east, west, desc):
        self.name = name
        self.desc = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
CATHEDRAL = Room("The Cathedral", 'ARMORY', 'GRAVEYARD', 'FIRING', 'LIBRARY',
                 "You find yourself in a cathedral with broken glass everywhere and worn out furniture." )
