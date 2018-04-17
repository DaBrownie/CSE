class Item(object):
    def __init__(self, name, desc, type_, rarity):
        self.name = name
        self.desc = desc
        self.type_ = type_
        self.rarity = rarity


class Inventory(object):
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
    def __init__(self, name, effects, dmgc, crit, classx):
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


class Staff(Weapon):
    def __init__(self, name, desc, type_, rarity, dmg, weight, length, range, uses, classx):
        super(Weapon, self).__init__(name, desc, type_, rarity, dmg, weight, length, range, uses)
        self.length = False
        classx = 'MAGE'


class Shovel(Tool):
    def __init__(self, name, desc, type_, rarity, dig):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.dig = dig


class Key(Tool):
    def __init__(self, name, desc, type_, rarity, open_):
        super(Tool, self).__init__(name, desc, type_, rarity)
        self.open_ = open_


class Sword(Weapon):
    def __init__(self, name, desc, type_, rarity, dmg, weight, length, range, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity, dmg, weight, length, range, uses)
        self.range = False


class Book(Weapon):
    def __init__(self, name, desc, type_, rarity, dmg, weight, length, range, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity, dmg, weight, length, range, uses)
        self.length = False


class Spear(Weapon):
    def __init__(self, name, desc, type_, rarity, dmg, weight, length, range, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity, dmg, weight, length, range, uses)
        self.range = False


class Robes(Armor):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd, dur, mdmgplus):
        super(Robes, self).__init__(name, desc, type_, rarity, def_lvl, mres, spd, dur)
        self.mdmgplus = mdmgplus


class Light_cloth(Armor):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd, dur, spdplus):
        super(Light_cloth, self).__init__(name, desc, type_, rarity, def_lvl, mres, spd, dur)
        self.spdplus = spdplus


class Metal(Armor):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd, dur, defplus):
        super(Metal, self).__init__(name, desc, type_, rarity, def_lvl, mres, spd, dur)
        self.defplus = defplus



