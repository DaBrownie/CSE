import string


def print_inventory():
    for item in inventory:
        print(item.name)


def print_items():
    print("The item in the room are:")
    for item in current_node.items:
        print(item.name)
    for item in current_node.items:
        if item == []:
            print("There are no items here")


def print_wequiped():
    for item in player_stats.eweapon:
        print(item.name)


def print_aequiped():
    for item in player_stats.earmor:
        print(item.name)


def attack(target):
        if fight == target.name:
            dmg = target.defense - player_attack
            if dmg <= 0:
                print('You do no dmg')
            elif dmg > 0:
                hp = target.HP - dmg
                target.HP = hp
                print("%s has taken %s damage and has %s HP left" % (target.name, dmg, target.HP))


def equip_weapon():
    iequip = input("What\n>_")
    for item in inventory:
        if iequip == item.name and item.req == 'wep' and item.classr == player_stats.classx:
            removed_item = player_stats.eweapon.remove
            inventory.append(removed_item)
            inventory.remove(item)
            player_stats.eweapon.append(item)
            print("The armor you have equipped is %s" % print_wequiped())
        else:
            print("You cannot do this")


def print_npcname():
    for item in current_node.characters:
        print(item.name)


def print_killede():
    print("You have killed:")
    for item in killed_enemies:
        print(item.name)
        if item not in killed_enemies:
            print('Nothing')


class Room(object):
    def __init__(self, name, north, south, east, west, southeast, desc, items, characters, visits):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.desc = desc
        self.items = items
        self.characters = characters
        self.visits = visits


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
    def __init__(self, attack, defense, speed, luck, chance, intellect):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.chance = chance
        self.intellect = intellect


class Character(Stats):
    def __init__(self, attack, defense, speed, luck, chance, intellect, HP, mana, name, classx, eweapon, earmor):
        super(Character, self).__init__(attack, defense, speed, luck, chance, intellect)
        self.HP = HP
        self.mana = mana
        self.name = name
        self.classx = classx
        self.eweapon = eweapon
        self.earmor = earmor


class Skill(object):
    def __init__(self, name, effects, dmgc, crit, manause):
        self.name = name
        self.effects = effects
        self.dmgc = dmgc
        self.crit = crit
        self.manause = manause


class Weapon(Item):
    def __init__(self, name, desc, type_, rarity, dmg, weight, range, uses, req, classr):
        super(Weapon, self).__init__(name, desc, type_, rarity)
        self.dmg = dmg
        self.range = weight
        self.range = range
        self.uses = uses
        self.req = req
        self.classr = classr


class Armor(Item):
    def __init__(self, name, desc, type_, rarity, defense, speed, intellect, HP, mana):
        super(Armor, self).__init__(name, desc, type_, rarity)
        self.defense = defense
        self.speed = speed
        self.intellect = intellect
        self.HP = HP
        self.mana = mana


class Magic(Item):
    def __init__(self, name, desc, type_, rarity, mana_use, mana_gain, uses):
        super(Magic, self).__init__(name, desc, type_, rarity)
        self.mana_use = mana_use
        self.mana_gain = mana_gain
        self.uses = uses


class Tool(Item):
    def __init__(self, name, desc, type_, rarity):
        super(Tool, self).__init__(name, desc, type_, rarity)


class Shovel(Tool):
    def __init__(self, name, desc, type_, rarity, dig):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.dig = dig


class Key(Tool):
    def __init__(self, name, desc, type_, rarity, open_):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.open_ = open_



WOOD_SWORD = Weapon("wood sword", "A old wooden sword that might fall apart if you use it at all", 'K', 'common', '5',
                    '3', '0', '30', 'wep', 'K')
WOOD_BOW = Weapon("wood bow", "A old wooden bow that might fall apart if you use it at all", 'A', 'common', '5',
                    '3', '0', '30', 'wep', 'A')
WOOD_SPEAR = Weapon("wood spear", "A old wooden spear that might fall apart if you use it at all", 'L', 'common', '5',
                    '3', '0', '30', 'wep', 'L')
WOOD_STAFF = Weapon("wood staff", "A old wooden staff that might fall apart if you use it at all", 'M', 'common', '5',
                    '3', '0', '30', 'wep', 'M')
#  attack, defense, dexterity, speed, range_, luck, intellect, HP, Mana
#  attack, defense, speed, chance, luck, intellect, HP, mana, name, classx
swordstats = Character(7, 7, 3, 1, 4, 0, 100, 300, "", 'K', [WOOD_BOW], [])

bowstats = Character(3, 3, 6, 7, 3, 0, 100, 300, "", 'A', [], [])

staffstats = Character(5, 5, 8, 5, 6, 11, 100, 300, "", 'M', [], [])

spearstats = Character(3, 7, 9, 3, 3, 1, 100, 300, "", 'L', [], [])

player = Character(0, 0, 0, 0, 0, 0, 100, 300, "", None, [], [])

chris = Character(6, 6, 6, 6, 6, 6, 100, 300, 'Chris', 'W', [], [])

# Initialize Rooms  name, north, south, east, west, southeast, desc, items, characters, visits
TIMEANDSPACE = Room("Time and Space", None, None, None, None, None, "You don't know where you are, who you are what you"
                                                                    " are "
                                                                    "or why you are here, but you see A sword, a bow,"
                    "\n a spear and a staff, you reach out to chose one what do you pick", [WOOD_SWORD, WOOD_BOW,
                                                                                            WOOD_SPEAR, WOOD_STAFF],
                    (), 0)
CATHEDRAL = Room("The Cathedral", 'ARMORY', 'GRAVEYARD', 'FIRING', 'LIBRARY', None,
                 "You find yourself in a cathedral with broken glass everywhere and worn out furniture. on the other "
                 "side of the \n middle of the Cathedral %s is approaching you with a 5%% summon chance on (WT) banner "
                 "but no Leif" % chris.name, [], chris, 0)
ARMORY = Room("The Armory", 'HALL', 'CATHEDRAL', 'MAINTROOM', 'FOREST', None, "There is a man guarding a giant box, "
                                                              "and you feel a strong presence from the box", [], (), 0)
HALL = Room("The Long Hallway", 'REPAIR', 'ARMORY', 'FOOD', None, None, "a long hallway filled with old paintings and "
                                                                        "inscribing on the wall", [], (), 0)
REPAIR = Room("The Repair Center", None, 'HALL', 'TUNNEL', None, None, "There is a grinder wheel and cleaning cloths"
                                                                       " neatly laid outs", [], (), 0)
TUNNEL = Room("A Dark Tunnel", None, None, 'GLASS', 'REPAIR', None, "A Dark tunnel, you can't see anything without a "
                                                                    "source of light", [], (), 0)
GLASS = Room("Glass Statue", None, None, None, 'TUNNEL', None, "In the middle of the room there is a glass statue that "
                                               "looks like the goddess Ishtar, at her feet \n there is a: Long "
                                               "stick, wooden sword, plastic ball, tattered book, and old "
                                               "bow and arrows", [], (), 0)
FOOD = Room("Rations Center", None, None, None, 'HALL', None, "a dusty place with dusty cabinets and old kitchenware",
            [], (), 0)
MAINTROOM = Room("Maintenance Room", None, None, 'TELEPORTER', 'ARMORY', None,
                 "A room with cleaning-ware and in the middle "
                 "a container holding a chain of keys that "
                 "requires a code \n to open. The code is a 6 "
                 "2-digit code (in total 12 digits) is equal "
                 "to west, \n and has a pattern in "
                 "odd numbers.", [], (), 0)
TELEPORTER = Room("Teleporter Room", None, None, None, 'MAINTROOM', None,
                                                         "a room with Mario tubes everywhere (not the "
                                                         "teleporter you thought?). Some of the tubes seem to \n be"
                                                         " broken and rusted", [], (), 0)
FOREST = Room("Burnt Forest", 'OLWAF', None, 'ARMORY', None, None, "A forest with burnt down trees, skeletons, "
                                                                   "and bodies everywhere", [], (), 0)
VILLAGE = Room("The Peaceful Village", None, 'OLWAF', None, None, None, "a village with people everywhere...It is quite"
               " a "
               "happy place despite the surrounding war field...\n"
               " The are shops by the factions of the: Blacksmiths,"
               " Alchemists, Clothiers, and Librarians", [], (), 0)
OLWAF = Room("The Old War Field", 'VILLAGE', 'FOREST', None, None, None, "a war field with cannons, corpses, and "
                                                                         "weapons laid everywhere...In the distance "
                                                                         "you see what looks \n  like a village.", [],
             (), 0)
GRAVEYARD = Room("GraveYard", 'CATHEDRAL', None, None, None, None, "a graveyard...with graves...and dead beings of "
                                                                   "multiple races: Elves, dwarfs, humans, demons, "
                                                                   "\n fairies, and sub-terrainians. GraveYards are "
                                                                   "a good research place for necromancers, stay "
                                                                   "aware \n of your surroundings ", [WOOD_SWORD, WOOD_BOW,
                                                                                            WOOD_SPEAR, WOOD_STAFF], (), 0)
LIBRARY = Room("The Library", None, None, 'CATHEDRAL', None, 'NLR', "a library with no books. You should explore it",
               [], (), 0)
MAGICIANT = Room("Magician's Test", 'MAGICIANJ', 'LIBRARY', None, None, None, "You are teleported to a room with a man"
                                                                              " in a great robe with a staff and orb "
                                                                              "in his hands. He \n looks at you "
                                                                              "gesturing you to talk.", [], (), 0)
MAGICIANJ = Room("Magician's Judgement", 'LIBRARY', None, None, None, None, "He brings you a corner of the room and "
                                                                            "gives you a knife to cut your finger with",
                 [], (), 0)
NLR = Room("No Life's Room", None, None, None, None, 'LIBRARY',
           "You find a room with that's dark but you can still see things pretty clearly and  a human from "
           "\n another  world with a object that looks like a book but sideways and there's a clicking sound "
           "\n every time he interacts with it, it also has pictures in light emitting from the top of the device."
           "\n The person's constantly yelling at the device about the pay-to-win and skilless-spammers, whatever"
           "\n those are.", [], (), 0)

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
weapon = None
head_wear = None
top_piece = None
bottom_piece = None
gloves = None
shoes = None
current_equip = (weapon, head_wear, top_piece, bottom_piece, gloves, shoes)
player_attack = player_stats.attack + player_stats.eweapon.attck
killed_enemies = []
max_exp = 100
CExp = 0
Level = 1
inventory = [map1]
choice = 0
TAS = 0
turn = 0
inventory = []

while True:
    if TAS == 0:
        name = input('What is your name?\n>_') + ','
        TAS += 1
        if name in ['Chris,', 'chris']:
            name = 'Not Leif,'
    if turn == 0:
        print(current_node.name)
        turn += 1
    if current_node.visits == 0:
        print(name, current_node.desc)
        print_items()
        current_node.visits += 1
    command = input('>_').lower()


    if command in ['i like zero two', 'i like 02', '02 is better than ichigo', 'zero two is better than ichigo']:
        print('You should die')
    else:
        turn += 1

    if current_node == TIMEANDSPACE:
        if 'sword' in command:
            player_stats = swordstats
            current_node.items.remove(WOOD_SWORD)
            inventory.append(WOOD_SWORD)
            current_node = CATHEDRAL
        if 'bow' in command:
            player_stats = bowstats
            current_node.items.remove(WOOD_BOW)
            inventory.append(WOOD_BOW)
            current_node = CATHEDRAL
        if 'spear' in command:
            player_stats = spearstats
            current_node.items.remove(WOOD_SPEAR)
            inventory.append(WOOD_SPEAR)
            current_node = CATHEDRAL
        if 'staff' in command:
            player_stats = staffstats
            current_node.items.remove(WOOD_STAFF)
            inventory.append(WOOD_STAFF)
            current_node = CATHEDRAL



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

    equiped = None
    if command == 'stats':
        print()
    if command in ['i', 'inv', 'inventory']:
        print_inventory()
    if command in ['killed enemies', 'player kills', 'enemies killed', 'ke', 'kills']:
        print_killede()
    if command in ['d', 'des', 'description', 'desc']:
        print(current_node.desc)
    if command in ['objects', 'object', 'items', 'stuff', 'things']:
        print_items()
    if command in ['equip', 'eq', 'put on']:
        print_inventory()
        equip_weapon()



    if command in ['attack', 'hit', 'fight', 'kill']:
        fight = input('What\n>_')
        attack(fight)


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
        for item in current_node.items:
            if take == item.name:
                print("You took the %s" % take)
                current_node.items.remove(item)
                inventory.append(item)
                print_inventory()

    if command in ['jump', 'fly', 'float', 'soar']:
        print('Congratulations do you feel accomplished?')
    if command in ['suicide', 'die']:
        print('Maybe later')
    if command in ['gay', 'homosexual', 'gae', 'gei', 'homo sexual', 'homo',
                   'your mom gay', 'ur mom gay', 'ur mum gay']:
        print('no u')
    if command in ['bitch', 'fuck', 'damn', 'shit']:
        print('Watch your language!')
    if command == '':
        print('Nothing?\nLess work for me')


    if command == '^^vv<><>ba' and choice == 0:
        print('you have Light Brand')
        inventory.append()
        choice += 1
    if command == '^cvc<c>ca' and choice == 0:
        choice += 1
    if command == 'idspispopd' and choice == 0:
        choice += 1
