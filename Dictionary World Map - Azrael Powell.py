game_map = {
    'CATHEDRAL': {
        'NAME': "The Cathedral",
        'DESC': "You find yourself in a cathedral with broken glass everywhere and worn out furniture.",
        'PATHS': {
            'N': "ARMORY",
            'S': 'GRAVEYARD',
            'E': 'FIRING',
            'W': 'LIBRARY',
        }
    },
    'ARMORY': {
        'NAME': "The Armory",
        'DESC': "There is a man guarding a giant box, and you feel a strong presence from the box",
        'PATHS': {
            'N': 'HALL',
            'S': 'CATHEDRAL',
            'E': 'MAINTROOM',
            'W': 'FOREST',
        }
    },
    'HALL': {
        'NAME': "The Long Hallway",
        'DESC': "a long hallway filled with old paintings and inscribing on the wall",
        'PATHS': {
            'N': 'REPAIR',
            'S': 'ARMORY',
            'E': 'FOOD',
        }
    },
    'REPAIR': {
        'NAME': "The Repair Center",
        'DESC': "There is a grinder wheel and cleaning cloths neatly laid out",
        'PATHS': {
            'S': 'HALL',
            'E': 'TUNNEL',
        }
    },
    'TUNNEL': {
        'NAME': "A Dark Tunnel",
        'DESC': "A Dark tunnel, you can't see anything without a source of light",
        'PATHS': {
            'E': 'GLASS',
            'W': 'REPAIR',
        }
    },
    'GLASS': {
        'NAME': "Glass Statue",
        'DESC': "In the middle of the room there is a glass statue that looks like the goddess Ishtar, at her feet "
                "\n there is a: Long stick, wooden sword, plastic ball, tattered book, and old bow and arrows",
        'PATHS': {
            'W': 'TUNNEL',
        }
    },
    'FOOD': {
        'NAME': "Rations Center",
        'DESC': "a dusty place with dusty cabinets and old kitchenware",
        'PATHS': {
            'W': 'HALL',
        }
    },
    'MAINTROOM': {
        'NAME': "Maintenance Room",
        'DESC': "A room with cleaning-ware and in the middle a container holding a chain of keys that requires a code "
                "\n to open. The code is a 6 2-digit code (in total 12 digits) is equal to west in degrees, "
                "\n and has a pattern in prime numbers.",
        'PATHS': {
            'E': 'TELEPOOPER',
            'W': 'ARMORY',
        }
    },
    'TELEPOOPER': {
        'NAME': "Broken Teleporter",
        'DESC': "a room with magic circles everywhere (not the teleporter you thought?). Some of the circles seem to "
                "\n be partially erased",
        'PATHS': {
            'W': 'MAINTROOM',
        }
    },
    'FOREST': {
        'NAME': "Burnt Forest",
        'DESC': "A forest with burnt down trees, skeletons, and bodies everywhere",
        'PATHS': {
            'N': 'OLWAF',
            'E': 'ARMORY',
        }
    },
    'VILLAGE': {
        'NAME': "The Peaceful Village",
        'DESC': "a village with people everywhere...It is quite a happy place despite the surrounding war field... "
                "\n The are shops by the factions of the: Blacksmiths, Alchemists, Clothiers, and Librarians",
        'PATHS': {
            'S': 'OLWAF',
        }
    },
    'OLWAF': {
        'NAME': "The Old War Field",
        'DESC': "a war field with cannons, corpses, and weapons laid everywhere...In the distance you see what looks "
                "\n  like a village.",
        'PATHS': {
            'N': 'VILLAGE',
            'S': 'FOREST',
        }
    },
    'GRAVEYARD': {
        'NAME': "GraveYard",
        'DESC': "a graveyard...with graves...and dead beings of multiple races: Elves, dwarfs, humans, demons, "
                "\n fairies, and sub-terrainians. GraveYards are a good research place for necromancers, stay aware \n "
                "of your surroundings ",
        'PATHS': {
            'N': 'CATHEDRAL',
        }
    },
    'LIBRARY': {
        'NAME': "The Library",
        'DESC': "a library with no books. You should explore it",
        'EXPLO': "you find a magic circle in a corner of the room in a hole...You feel tempted to touch it",
        'PATHS': {
            'T': 'MAGICIANT',
            'SE': 'NLR',
            'W': 'CATHEDRAL',
        }
    },
    'MAGICIANT': {
        'NAME': "Magician's Test",
        'DESC': "You are teleported to a room with a man in a great robe with a staff and orb in his hands. He "
                "\n looks at you gesturing you to talk.",
        'PATHS': {
            'S': 'MAGICIANJ',
            'N': 'LIBRARY',
        }
    },
    'FORBLIBR': {
        'NAME': "Forbidden Library",
        'DESC': " a massive library with magical tomes, scrolls and books and you have gained an affinity for magic.",
        'PATHS': {
            'N': 'LIBRARY',
        }
    },
    'MAGICIANJ': {
        'NAME': "Magician's Judgement",
        'DESC': "He brings you a corner of the room and gives you a knife to cut your finger with",
        'PATHS': {
            'N': 'LIBRARY',
        }
    },
    'NLR': {
        'NAME': "No Life's Room",
        'DESC': "You find a room with that's dark but you can still see things pretty clearly and  a human from "
                "\n another  world with a object that looks like a book but sideways and there's a clicking sound "
                "\n every time he interacts with it, it also has pictures in light emitting from the top of the device."
                "\n The person's constantly yelling at the device about the pay-to-win and skilless-spammers, whatever"
                "\n those are.",
        'PATHS': {
            'NW': 'LIBRARY',
        }
    },

}

current_node = game_map['CATHEDRAL']
directions = ['N', 'S', 'E', 'W']
long_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESC'])
    command = input('>_').upper()
    if command == 'QUIT':
        quit(0)
    if command in long_directions:
        index = long_directions.index(command)
        command = directions[index]
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = game_map[name_of_node]
        except KeyError:
            print('You cannot go this way')
        print(current_node)
    else:
        print('Command not recognized')
