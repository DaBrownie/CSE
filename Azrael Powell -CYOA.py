import string


def print_inventory():
    for item in inventory:
        print(item.name)


def print_npcname():
    for item in current_node.characters:
        print(item.name)


class Room(object):
    def __init__(self, name, north, south, east, west, southeast, desc, items, characters, enemy):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.desc = desc
        self.items = items
        self.characters = characters
        self.enemy = enemy

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name, desc, type_, rarity):
        self.name = name
        self.desc = desc
        self.type_ = type_
        self.rarity = rarity


class Stats(object):
    def __init__(self, attack, defense, dexterity, speed, range_, luck, intellect):
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.speed = speed
        self.range_ = range_
        self.luck = luck
        self.intellect = intellect


class Character(Stats):
    def __init__(self, attack, defense, dexterity, speed, range_, luck, intellect, HP, name):
        super(Character, self).__init__(attack, defense, dexterity, speed, range_, luck, intellect)
        self.HP = HP
        self.name = name

    def attack(self, target):
        pass

    def take_damage(self, dmg):
        pass

class Skill(object):
    def __init__(self, name, effects, dmgc, crit):
        self.name = name
        self.effects = effects
        self.dmgc = dmgc
        self.crit = crit

class Weapon(Item):
    def __init__(self, name, desc, type_, rarity, dmg, weight, range, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity)
        self.dmg = dmg
        self.range = weight
        self.range = range
        self.uses = uses


class Armor(Item):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd, dur):
        super(Armor, self).__init__(name, desc, type_, rarity)
        self.def_lvl = def_lvl
        self.mres = mres
        self.spd = spd
        self.dur = dur


class Magic(Item):
    def __init__(self, name, desc, type_, rarity, mana_use, mana_gain, uses):
        super(Magic, self).__init__(name, desc, type_, rarity)
        self.mana_use = mana_use
        self.mana_gain = mana_gain
        self.uses = uses


class Tool(Item):
    def __init__(self, name, desc, type_, rarity, ):
        super(Tool, self).__init__(name, desc, type_, rarity)


class Shovel(Tool):
    def __init__(self, name, desc, type_, rarity, dig):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.dig = dig


class Key(Tool):
    def __init__(self, name, desc, type_, rarity, open_):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.open_ = open_



WOOD_SWORD = Weapon("Wood Sword", "A old wooden sword that might fall apart if you use it at all", 'S', 'common', '5',
                    '3', '0', '30')
WOOD_BOW = Weapon("Wood Bow", "A old wooden bow that might fall apart if you use it at all", 'B', 'common', '5',
                    '3', '0', '30')
WOOD_SPEAR = Weapon("Wood Sword", "A old wooden spear that might fall apart if you use it at all", 'R', 'common', '5',
                    '3', '0', '30')
WOOD_STAFF = Weapon("Wood Sword", "A old wooden staff that might fall apart if you use it at all", 'M', 'common', '5',
                    '3', '0', '30')

#  attack, defense, dexterity, speed, range_, luck, intellect, HP
player = Character(1, 1, 1, 1, 1, 1, 1, 100, "")
chris = Character(1, 1, 1, 1, 1, 1, 1, 100, 'Chris the FEH expert')

# Initialize Rooms
TIMEANDSPACE = Room("Time and Space", None, None, None, None, None, "You don't know where you are, who you are what you"
                                                                    " are "
                                                                    "or why you are here, but you see A sword, a bow,"
                    "\n a spear and a staff, you reach out to chose one what do you pick", [WOOD_SWORD, WOOD_BOW,
                                                                                            WOOD_SPEAR, WOOD_STAFF],
                                                                                           [], [])
CATHEDRAL = Room("The Cathedral", 'ARMORY', 'GRAVEYARD', 'FIRING', 'LIBRARY', None,
                 "You find yourself in a cathedral with broken glass everywhere and worn out furniture. on the other "
                 "side of the \n middle of the Cathedral %s is approaching you without Leif" % chris.name, [],
                 [chris], [])
ARMORY = Room("The Armory", 'HALL', 'CATHEDRAL', 'MAINTROOM', 'FOREST', None, "There is a man guarding a giant box, "
                                                              "and you feel a strong presence from the box", [], [], [])
HALL = Room("The Long Hallway", 'REPAIR', 'ARMORY', 'FOOD', None, None, "a long hallway filled with old paintings and "
                                                                        "inscribing on the wall", [], [], [])
REPAIR = Room("The Repair Center", None, 'HALL', 'TUNNEL', None, None, "There is a grinder wheel and cleaning cloths"
                                                                       " neatly laid outs", [], [], [])
TUNNEL = Room("A Dark Tunnel", None, None, 'GLASS', 'REPAIR', None, "A Dark tunnel, you can't see anything without a "
                                                                    "source of light", [], [], [])
GLASS = Room("Glass Statue", None, None, None, 'TUNNEL', None, "In the middle of the room there is a glass statue that "
                                               "looks like the goddess Ishtar, at her feet \n there is a: Long "
                                               "stick, wooden sword, plastic ball, tattered book, and old "
                                               "bow and arrows", [], [], [])
FOOD = Room("Rations Center", None, None, None, 'HALL', None, "a dusty place with dusty cabinets and old kitchenware",
            [], [], [])
MAINTROOM = Room("Maintenance Room", None, None, 'TELEPOOPER', 'ARMORY', None,
                 "A room with cleaning-ware and in the middle "
                 "a container holding a chain of keys that "
                 "requires a code \n to open. The code is a 6 "
                 "2-digit code (in total 12 digits) is equal "
                 "to west in degrees, \n and has a pattern in "
                 "prime numbers.", [], [], [])
TELEPORTER = Room("Teleporter Room", None, None, None, 'MAINTROOM', None,
                                                         "a room with Mario tubes everywhere (not the "
                                                         "teleporter you thought?). Some of the tubes seem to \n be"
                                                         " broken and rusted", [], [], [])
FOREST = Room("Burnt Forest", 'OLWAF', None, 'ARMORY', None, None, "A forest with burnt down trees, skeletons, "
                                                                   "and bodies everywhere", [], [], [])
VILLAGE = Room("The Peaceful Village", None, 'OLWAF', None, None, None, "a village with people everywhere...It is quite"
               " a "
               "happy place despite the surrounding war field...\n"
               " The are shops by the factions of the: Blacksmiths,"
               " Alchemists, Clothiers, and Librarians", [], [], [])
OLWAF = Room("The Old War Field", 'VILLAGE', 'FOREST', None, None, None, "a war field with cannons, corpses, and "
                                                                         "weapons laid everywhere...In the distance "
                                                                         "you see what looks \n  like a village.", [],
             [], [])
GRAVEYARD = Room("GraveYard", 'CATHEDRAL', None, None, None, None, "a graveyard...with graves...and dead beings of "
                                                                   "multiple races: Elves, dwarfs, humans, demons, "
                                                                   "\n fairies, and sub-terrainians. GraveYards are "
                                                                   "a good research place for necromancers, stay "
                                                                   "aware \n of your surroundings ", [], [], [])
LIBRARY = Room("The Library", None, None, 'CATHEDRAL', None, 'NLR', "a library with no books. You should explore it",
               [], [], [])
MAGICIANT = Room("Magician's Test", 'MAGICIANJ', 'LIBRARY', None, None, None, "You are teleported to a room with a man"
                                                                              " in a great robe with a staff and orb "
                                                                              "in his hands. He \n looks at you "
                                                                              "gesturing you to talk.", [], [], [])
MAGICIANJ = Room("Magician's Judgement", 'LIBRARY', None, None, None, None, "He brings you a corner of the room and "
                                                                            "gives you a knife to cut your finger with",
                 [], [], [])
NLR = Room("No Life's Room", None, None, None, None, 'LIBRARY',
           "You find a room with that's dark but you can still see things pretty clearly and  a human from "
           "\n another  world with a object that looks like a book but sideways and there's a clicking sound "
           "\n every time he interacts with it, it also has pictures in light emitting from the top of the device."
           "\n The person's constantly yelling at the device about the pay-to-win and skilless-spammers, whatever"
           "\n those are.", [], [], [])

current_node = TIMEANDSPACE
short_directions = ['n', 's', 'e', 'w', 'se']
directions = ['north', 'south', 'east', 'west', 'southeast']
A_Z = list(string.ascii_lowercase)
HP = 100
map1 = Item("Map", """
     ____________________________________________________
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |                                                  |
     |__________________________________________________|
""", "item", "common")
current_stats = Stats(0, 0, 0, 0, 0, 0, 0)
swordstats = Stats(7, 7, 9, 3, 1, 4, 0)
bowstats = Stats(3, 3, 7, 6, 7, 3, 0)
staffstats = Stats(5, 5, 8, 8, 5, 6, 11)
spearstats = Stats(3, 7, 15, 9, 3, 3, 1)
weapon = None
head_wear = None
top_piece = None
bottom_piece = None
gloves = None
shoes = None
current_equip = (weapon, head_wear, top_piece, bottom_piece, gloves, shoes)
view_a_items = [current_stats, current_equip]
max_exp = 100
CExp = 0
inventory = [map1, WOOD_SWORD]
turn = 0


while True:
    if turn == 0:
        print(current_node.name)
        print(current_node.desc)
    command = input('>_').lower()
    if command == 'i ate the cheese in the fridgerator last night':
        print('You should die')
    else:
        turn += 1
    if current_node == TIMEANDSPACE:
        if 'sword' in command:
            current_stats = swordstats
            current_node.items.remove(WOOD_SWORD)
            inventory.append(WOOD_SWORD)
            current_node = CATHEDRAL
            print(current_node.name)
            print(current_node.desc)
        if 'bow' in command:
            current_stats = bowstats
            current_node.items.remove(WOOD_BOW)
            inventory.append(WOOD_BOW)
            current_node = CATHEDRAL
            print(current_node.name)
            print(current_node.desc)
        if 'spear' in command:
            current_stats = spearstats
            current_node.items.remove(WOOD_SPEAR)
            inventory.append(WOOD_SPEAR)
            current_node = CATHEDRAL
            print(current_node.name)
            print(current_node.desc)
        if 'staff' in command:
            current_stats = staffstats
            current_node.items.remove(WOOD_STAFF)
            inventory.append(WOOD_STAFF)
            current_node = CATHEDRAL
            print(current_node.name)
            print(current_node.desc)
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        index = short_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            current_node.move(command)
            turn = 0
        except KeyError:
            print('You cannot go this way')
            turn += 1
    if command == 'stats':
        print("%s" % current_stats)
    if command == 'drop':
        drop1 = input('What?\n>_').lower()
        if drop1 in inventory:
            print('You have dropped %s' % drop1)
            inventory.remove(drop1)
            current_node.items.append(drop1)
        if drop1 not in inventory:
            print('You do not have that')
    if command == KeyError:
        print('Command not recognized')
    if command == 'take':
        take = input('What?\n>_').lower()
        if take in current_node.items:
            print("You took the %s" % take)
            current_node.items.remove(take)
            inventory.append(take)
            print_inventory()
        elif take not in current_node.items:
            print('That is not here')
    if command in ['i', 'inv', 'inventory']:
        print_inventory()
    if command in ['des', 'description', 'desc']:
        print(current_node.desc)
    if command in ['jump', 'fly', 'float', 'soar']:
        print('Congratulations do you feel accomplished?')
    if command in ['suicide', 'die']:
        print('Maybe later')
    if command == '':
        print('Nothing?\n Less work for me')
    chris.defense -= current_stats.attack
    if command in ['attack', 'hit', 'fight', 'kill']:
        fighter = input("what\n>_")
        if fighter is True:
            print("cannot do that 'YET'")
