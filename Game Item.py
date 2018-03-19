class Item(object):
    def __init__(self, name, desc, type_, rarity):
        self.name = name
        self.desc = desc
        self.type_ = type_
        self.rarity = rarity


class Weapon(Item):
    def __init__(self, name, desc, type_, rarity, atk_dmg, mag_dmg, weight, spd, uses):
        super(Weapon, self).__init__(name, desc, type_, rarity)
        self.atk_dmg = atk_dmg
        self.mag_dmg = mag_dmg
        self.range = weight
        self.spd = spd
        self.uses = uses



class Armor(Item):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd, uses):
        super(Armor, self).__init__(name, desc, type_, rarity)
        self.def_lvl = def_lvl
        self.mres = mres
        self.spd = spd
        self.uses = uses


class Magic(Item):
    def __init__(self, name, desc, type_, rarity, mana_use, mana_gain, uses):
        super(Magic, self).__init__(name, desc, type_, rarity)
        self.mana_use = mana_use
        self.mana_gain = mana_gain
        self.uses = uses


class Accessories(Item):
    def __init__(self, name, desc, type_, rarity, def_lvl, mres, spd):
        super(Accessories, self).__init__(name, desc, type_, rarity)
        self.def_lvl = def_lvl
        self.mres = mres
        self.spd = spd