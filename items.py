class Item:
    def __init__(self, name, type, rarity, value, weight=None):
        self.name = name
        self.type = type
        self.rarity = rarity
        self.value = value
        self.weight = weight


class Weapon(Item): # add crit dmg multiplier
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, weight)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance

    def itemView(self):
        dps = self.maxDps - self.minDps
        critChance = f'{int(self.critChance * 100)} %'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'DPS': dps, 'Crit Chance': critChance, 'Weight': self.weight,
                 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')

class Longsword(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, weight)


class Greatsword(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, weight)


class Dagger(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, weight)


class SmallAxe(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, weight)


class Greataxe(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, weight)


class Shield(Item): #add block chance
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

    def itemView(self):
        evasion = f'{int(self.evasion * 100)} %'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Armor Value': self.armorValue, 'Evasion': evasion,
                 'Weight': self.weight, 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')

class Greatshield(Shield):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class SmallShield(Shield):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class Armor(Item):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

    def itemView(self):
        evasion = f'{int(self.evasion * 100)} %'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Armor Value': self.armorValue, 'Evasion': evasion,
                 'Weight': self.weight, 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')

class LightArmor(Armor):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class HeavyArmor(Armor):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class Ring(Item):
    def __init__(self, name, type, rarity, value, minDps=None, maxDps=None,
                 armorValue=None, evasion=None, critChance=None,
                 maxHealth=None):
        super().__init__(name, type, rarity, value)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance
        self.armorValue = armorValue
        self.evasion = evasion
        self.maxHealth = maxHealth

    def itemView(self):
        if self.maxDps:
            dps = self.maxDps - self.minDps
        else:
            dps = None
        if self.evasion:
            evasion = f'{int(self.evasion * 100)} %'
        else:
            evasion = None
        if self.critChance:
            critChance = f'{int(self.critChance * 100)} %'
        else:
            critChance = None
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Health': self.maxHealth, 'DPS': dps, 'Armor Value':
                     self.armorValue, 'Evasion': evasion,
                 'Crit Chance': critChance, 'Value': self.value}
        for key, value in attrs.items():
            if not value:
                continue
            else:
                print(f'{key:^15} : {value:^15}')


class Potion(Item):
    def __init__(self, name, type, rarity, value, heal=None):
        super().__init__(name, type, rarity, value, heal)
        self.heal = heal

    def itemView(self):
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Heal': self.heal, 'Value': self.value}
        for key, value in attrs.items():
            if not value:
                continue
            else:
                print(f'{key:^15} : {value:^15}')


class HealthPotion(Potion):
    def __init__(self, name, type, rarity, value, heal):
        super().__init__(name, type, rarity, value, heal)


class Antidote(Potion):
    def __init__(self, name, type, rarity, value):
        super().__init__(name, type, rarity, value)

    def curePoison(self, player):
        player.status.remove('poisoned')


class RegenPotion(Potion):
    def __init__(self, name, type, rarity, value, heal):
        super().__init__(name, type, rarity, value, heal)