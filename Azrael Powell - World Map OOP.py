class Room(object):
    def __init__(self, name, north, south, east, west, southeast, desc):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.desc = desc

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
CATHEDRAL = Room("The Cathedral", 'ARMORY', 'GRAVEYARD', 'FIRING', 'LIBRARY', None,
                 "You find yourself in a cathedral with broken glass everywhere and worn out furniture.")

ARMORY = Room("The Armory", 'HALL', 'CATHEDRAL', 'MAINTROOM', 'FOREST', None, "There is a man guarding a giant box, "
                                                              "and you feel a strong presence from the box")

HALL = Room("The Long Hallway", 'REPAIR', 'ARMORY', 'FOOD', None, None, "a long hallway filled with old paintings and "
                                                                        "inscribing on the wall")

REPAIR = Room("The Repair Center", None, 'HALL', 'TUNNEL', None, None, "There is a grinder wheel and cleaning cloths"
                                                                       " neatly laid out")

TUNNEL = Room("A Dark Tunnel", None, None, 'GLASS', 'REPAIR', None, "A Dark tunnel, you can't see anything without a "
                                                                    "source of light")

GLASS = Room("Glass Statue", None, None, None, 'TUNNEL', None, "In the middle of the room there is a glass statue that "
                                               "looks like the goddess Ishtar, at her feet \n there is a: Long "
                                               "stick, wooden sword, plastic ball, tattered book, and old "
                                               "bow and arrows")

FOOD = Room("Rations Center", None, None, None, 'HALL', None, "a dusty place with dusty cabinets and old kitchenware")

MAINTROOM = Room("Maintenance Room", None, None, 'TELEPOOPER', 'ARMORY', None,
                 "A room with cleaning-ware and in the middle "
                 "a container holding a chain of keys that "
                 "requires a code \n to open. The code is a 6 "
                 "2-digit code (in total 12 digits) is equal "
                 "to west in degrees, \n and has a pattern in "
                 "prime numbers.")

TELEPOOPER = Room("Broken Teleporter", None, None, None, 'MAINTROOM', None,
                                                         "a room with magic circles everywhere (not the "
                                                         "teleporter you thought?). Some of the circles seem to \n be"
                                                         " partially erased")

FOREST = Room("Burnt Forest", 'OLWAF', None, 'ARMORY', None, None, "A forest with burnt down trees, skeletons, "
                                                                   "and bodies everywhere")

VILLAGE = Room("The Peaceful Village", None, 'OLWAF', None, None, None, "a village with people everywhere...It is quite"
               " a "
               "happy place despite the surrounding war field...\n"
               " The are shops by the factions of the: Blacksmiths,"
               " Alchemists, Clothiers, and Librarians")

OLWAF = Room("The Old War Field", 'VILLAGE', 'FOREST', None, None, None, "a war field with cannons, corpses, and "
                                                                         "weapons laid everywhere...In the distance "
                                                                         "you see what looks \n  like a village.")

GRAVEYARD = Room("GraveYard", 'CATHEDRAL', None, None, None, None, "a graveyard...with graves...and dead beings of "
                                                                   "multiple races: Elves, dwarfs, humans, demons, "
                                                                   "\n fairies, and sub-terrainians. GraveYards are "
                                                                   "a good research place for necromancers, stay "
                                                                   "aware \n of your surroundings ")

LIBRARY = Room("The Library", None, None, 'CATHEDRAL', None, 'NLR', "a library with no books. You should explore it")

MAGICIANT = Room("Magician's Test", 'MAGICIANJ', 'LIBRARY', None, None, None, "You are teleported to a room with a man"
                                                                              " in a great robe with a staff and orb "
                                                                              "in his hands. He \n looks at you "
                                                                              "gesturing you to talk.")

MAGICIANJ = Room("Magician's Judgement", 'LIBRARY', None, None, None, None, "He brings you a corner of the room and "
                                                                            "gives you a knife to cut your finger with")

NLR = Room("No Life's Room", None, None, None, None, 'LIBRARY',
           "You find a room with that's dark but you can still see things pretty clearly and  a human from "
           "\n another  world with a object that looks like a book but sideways and there's a clicking sound "
           "\n every time he interacts with it, it also has pictures in light emitting from the top of the device."
           "\n The person's constantly yelling at the device about the pay-to-win and skilless-spammers, whatever"
           "\n those are.",)
current_node = CATHEDRAL
short_directions = ['n', 's', 'e', 'w', 'se']
directions = ['north', 'south', 'east', 'west', 'southeast']
inventory = []
target = ()
prob = ['Goblin', 'Thief', 'Barbarian', 'Wizard', 'Dragon']


while True:
    print(current_node.name)
    print(current_node.desc)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        index = short_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You cannot go this wae')
    else:
        print('Command not recognized')