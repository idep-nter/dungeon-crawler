class Item:
    def __init__(self, name, type, rarity, value, weight=None):
        self.name = name
        self.type = type
        self.rarity = rarity
        self.value = value
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance

    def itemView(self):
        attrs = vars(self)
        for key, value in attrs.items():
            value = strNone(value)
            print(f'{key:^15} : {value:^15}')


class Longsword(Weapon):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight, minDps, maxDps,
                         critChance)


class Greatsword(Weapon):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight, minDps, maxDps,
                         critChance)


class Dagger(Weapon):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight, minDps, maxDps,
                         critChance)


class SmallAxe(Weapon):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight, minDps, maxDps,
                         critChance)


class Greataxe(Weapon):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight, minDps, maxDps,
                         critChance)


class Shield(Item):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

    def itemView(self):
        attrs = vars(self)
        for key, value in attrs.items():
            value = strNone(value)
            print(f'{key:^15} : {value:^15}')


class Greatshield(Shield):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight, armorValue, evasion)


class SmallShield(Shield):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight, armorValue, evasion)


class Armor(Item):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

    def itemView(self):
        attrs = vars(self)
        for key, value in attrs.items():
            value = strNone(value)
            print(f'{key:^15} : {value:^15}')


class LightArmor(Armor):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight, armorValue, evasion)


class HeavyArmor(Armor):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight, armorValue, evasion)


class Ring(Item):
    def __init__(self, name, type, rarity, value, maxHealth=None,
                 minDps=None, maxDps=None, armorValue=None, evasion=None,
                 critChance=None):
        super().__init__(name, type, rarity, value)
        self.maxHealth = maxHealth
        self.minDps = minDps
        self.maxDps = maxDps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance

    def itemView(self):
        attrs = vars(self)
        for key, value in attrs.items():
            value = strNone(value)
            print(f'{key:^15} : {value:^15}')


class Potion(Item):
    def __init__(self, name, type, rarity, value):
        super().__init__(name, type, rarity, value)

    def itemView(self):
        attrs = vars(self)
        for key, value in attrs.items():
            print(f'{key} : {value}')


class HealthPotion(Potion):
    def __init__(self, name, type, rarity, value, heal):
        super().__init__(name, type, rarity, value)
        self.heal = heal


class Antidote(Potion):
    def __init__(self, name, type, rarity, value):
        super().__init__(name, type, rarity, value)

    def curePoison(self, player):
        player.states.remove('poisoned')

def strNone(value):
    if not value:
        return '-'
    return value