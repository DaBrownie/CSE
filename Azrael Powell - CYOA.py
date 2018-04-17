class Room(object):
    def __init__(self, name, north, south, east, west, southeast, desc, items):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.desc = desc
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name, desc, type_, rarity):
        self.name = name
        self.desc = desc
        self.type_ = type_
        self.rarity = rarity


class DoP(object):
    def __init__(self, equip, use, unequip, drop):
        self.equip = equip
        self.use = use
        self.unequip = unequip
        self.drop = drop


class Classx(object):
    def __init__(self, name, stats, weapon, classig):
        self.name = name
        self.stats = stats
        self.weapon = weapon
        self.classig = classig


class Skill(object):
    def __init__(self, name, effects, dmgc, crit):
        self.name = name
        self.effects = effects


class Weapon(Item):
    def __init__(self, name, desc, type_, rarity, dmg, weight, length, range, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity)
        self.dmg = dmg
        self.range = weight
        self.length = length
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
                    '3', '4', '0', '30')
WOOD_BOW = Weapon("Wood Bow", "A old wooden bow that might fall apart if you use it at all", 'B', 'common', '5',
                    '3', '4', '0', '30')
WOOD_SPEAR = Weapon("Wood Sword", "A old wooden spear that might fall apart if you use it at all", 'R', 'common', '5',
                    '3', '4', '0', '30')
WOOD_STAFF = Weapon("Wood Sword", "A old wooden staff that might fall apart if you use it at all", 'M', 'common', '5',
                    '3', '4', '0', '30')
# Initialize Rooms
TIMEANDSPACE = Room("Time and Space", None, None, None, None, None, "You don't know where you are, who you are what you are "
                                                              "or why you are here, but you see A sword, a bow,"
                    "\n a spear and a staff, you reach out to chose one what do you pick", ['WOOD_SWORD', 'WOOD_BOW',
                                                                                            'WOOD_SPEAR', 'WOOD_STAFF'])
CATHEDRAL = Room("The Cathedral", 'ARMORY', 'GRAVEYARD', 'FIRING', 'LIBRARY', None,
                 "You find yourself in a cathedral with broken glass everywhere and worn out furniture. on the other "
                 "side of the \n middle of the Cathedral there is a mad warrior slowly approaching you with a blood "
                 "stained sword.", None)
ARMORY = Room("The Armory", 'HALL', 'CATHEDRAL', 'MAINTROOM', 'FOREST', None, "There is a man guarding a giant box, "
                                                              "and you feel a strong presence from the box", None)
HALL = Room("The Long Hallway", 'REPAIR', 'ARMORY', 'FOOD', None, None, "a long hallway filled with old paintings and "
                                                                        "inscribing on the wall", None)
REPAIR = Room("The Repair Center", None, 'HALL', 'TUNNEL', None, None, "There is a grinder wheel and cleaning cloths"
                                                                       " neatly laid outs", None)
TUNNEL = Room("A Dark Tunnel", None, None, 'GLASS', 'REPAIR', None, "A Dark tunnel, you can't see anything without a "
                                                                    "source of light", None)
GLASS = Room("Glass Statue", None, None, None, 'TUNNEL', None, "In the middle of the room there is a glass statue that "
                                               "looks like the goddess Ishtar, at her feet \n there is a: Long "
                                               "stick, wooden sword, plastic ball, tattered book, and old "
                                               "bow and arrows", None)
FOOD = Room("Rations Center", None, None, None, 'HALL', None, "a dusty place with dusty cabinets and old kitchenware",
            None)
MAINTROOM = Room("Maintenance Room", None, None, 'TELEPOOPER', 'ARMORY', None,
                 "A room with cleaning-ware and in the middle "
                 "a container holding a chain of keys that "
                 "requires a code \n to open. The code is a 6 "
                 "2-digit code (in total 12 digits) is equal "
                 "to west in degrees, \n and has a pattern in "
                 "prime numbers.", None)
TELEPORTER = Room("Teleporter Room", None, None, None, 'MAINTROOM', None,
                                                         "a room with Mario tubes everywhere (not the "
                                                         "teleporter you thought?). Some of the tubes seem to \n be"
                                                         " broken and rusted", None)
FOREST = Room("Burnt Forest", 'OLWAF', None, 'ARMORY', None, None, "A forest with burnt down trees, skeletons, "
                                                                   "and bodies everywhere", None)
VILLAGE = Room("The Peaceful Village", None, 'OLWAF', None, None, None, "a village with people everywhere...It is quite"
               " a "
               "happy place despite the surrounding war field...\n"
               " The are shops by the factions of the: Blacksmiths,"
               " Alchemists, Clothiers, and Librarians", None)
OLWAF = Room("The Old War Field", 'VILLAGE', 'FOREST', None, None, None, "a war field with cannons, corpses, and "
                                                                         "weapons laid everywhere...In the distance "
                                                                         "you see what looks \n  like a village.", None)
GRAVEYARD = Room("GraveYard", 'CATHEDRAL', None, None, None, None, "a graveyard...with graves...and dead beings of "
                                                                   "multiple races: Elves, dwarfs, humans, demons, "
                                                                   "\n fairies, and sub-terrainians. GraveYards are "
                                                                   "a good research place for necromancers, stay "
                                                                   "aware \n of your surroundings ", None)
LIBRARY = Room("The Library", None, None, 'CATHEDRAL', None, 'NLR', "a library with no books. You should explore it",
                None)
MAGICIANT = Room("Magician's Test", 'MAGICIANJ', 'LIBRARY', None, None, None, "You are teleported to a room with a man"
                                                                              " in a great robe with a staff and orb "
                                                                              "in his hands. He \n looks at you "
                                                                              "gesturing you to talk.", None)
MAGICIANJ = Room("Magician's Judgement", 'LIBRARY', None, None, None, None, "He brings you a corner of the room and "
                                                                            "gives you a knife to cut your finger with",
                 None)
NLR = Room("No Life's Room", None, None, None, None, 'LIBRARY',
           "You find a room with that's dark but you can still see things pretty clearly and  a human from "
           "\n another  world with a object that looks like a book but sideways and there's a clicking sound "
           "\n every time he interacts with it, it also has pictures in light emitting from the top of the device."
           "\n The person's constantly yelling at the device about the pay-to-win and skilless-spammers, whatever"
           "\n those are.", None)

current_node = TIMEANDSPACE
short_directions = ['n', 's', 'e', 'w', 'se']
directions = ['north', 'south', 'east', 'west', 'southeast']
inventory = ['map']
attack = 0
defense = 5
dexterity = 5
speed = 5
range_ = 0
luck = 1
intellect = 0
stats = (attack, defense, dexterity, speed, range_, luck, intellect)
staffstats = (5, 5, 8, 8, 5, 6, 11)
weapon = None
head_wear = None
top_piece = None
bottom_piece = None
gloves = None
shoes = None
current_equip = (weapon, head_wear, top_piece, bottom_piece, gloves, shoes)
view_a_items = [stats, current_equip]
max_exp = 100
CExp = 0
while True:
    print(current_node.name)
    print(current_node.desc)
    command = input('>_').lower()
    if current_node == TIMEANDSPACE:
        if 'sword' in command:
            attack += 7
            defense += 2
            dexterity += 4
            speed -= 2
            range_ += 1
            luck += 3
            intellect += 0
            command.remove(current_node.items[WOOD_SWORD])
            command.append(inventory)
            current_node = CATHEDRAL
        if 'bow' in command:
            attack += 3
            defense -= 2
            dexterity += 2
            speed += 1
            range_ += 7
            luck += 2
            intellect += 0
            command.remove(current_node.items)
            command.append(inventory)
            current_node = CATHEDRAL
        if 'spear' in command:
            attack += 3
            defense += 2
            dexterity += 10
            speed += 9
            range_ += 3
            luck += 2
            intellect += 1
            command.remove(current_node.items)
            command.append(inventory)
            current_node = CATHEDRAL
        if 'staff' in command:
            stats = staffstats
            command.remove(current_node.items)
            command.append(inventory)
            current_node = CATHEDRAL
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
    if command == 'stats':
        print("%s" % stats)
    if 'inv' in command:
        print(inventory)
    if command == 'take':
        print('what?')
        if command in current_node:
            command.remove(current_node.items)
            command.append(inventory)
    if command == 'drop':
        drop1 = input('What?'
                      '>_').lower()
        if drop1 in inventory:
            print('You have dropped %s' % drop1)
            drop1.remove(inventory)
            drop1.append(current_node.items)
    else:
        print('Command not recognized')