import random
class Character(object):
    def __init__(self, name, move, talk, interact, inventory, abilities, stats, health, status_effects, physique,
                 description, dialogue, attack, take_damage, level):
        self.name = name
        self.move = move
        self.talk = talk
        self.interact = interact
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = health
        self.status_effects = status_effects
        self.physique = physique
        self.description = description
        self.dialogue = dialogue
        self.attack = attack
        self.take_damage = take_damage
        self.level = level


   # def move(self, direction):
   #     global current_node
   #     current_node = globals()[getattr(self, direction)]

    def talk(self):
        print("you talk to them")

    def interact(self):
        if self is 'immovable':
            print('Nothing happens')
        elif self is 'cursed':
            print('You cannot hold this object')
        elif self is 'not there':
            print('What are you trying to accomplish')
        elif self is 'magic circle':
            print('You have been teleported')
        elif self is 'item':
            print('You pick up the item')
            self.inventory.append('item')


Stats = ['strength', 'dexterity', 'defense', 'intellegence', 'vitality', 'luck', 'talent', 'trickery']
stat_lvl = [10, 10, 10, 10, 100, 5, 0, 2]
ability_list = ['fire', 'water', 'thunder', 'earth', 'divine', 'cursed', 'forbidden', 'inscription']
while True:
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
