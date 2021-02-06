import random


class Creature:
    def __init__(self, name, health, dps, armorValue,
                 evasion, critChance, shield=None):
        self.name = name
        self.health = health
        self.dps = dps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance
        self.shield = shield

    def attack(self, target):
        attack = random.choice(range(self.dps[0], self.dps[1] + 1))
        if random.random() < target.evasion:
            return False
        if random.random() < self.critChance:
            attack = (attack / 100) * 150
        attack = attack / (1 + (target.armorValue / 100))
        if target.shield:
            attack = (attack / 100) * 70
        target.health -= attack

    def itemDrop(self, player, items):
        if self == Boss:
            item = random.choice(items['rare'])
            player.inventory.append(item)
            # global items
            items.remove[item]

        n = random.random()
        if n < 0.1:
            item = random.choice(items['rare'])
        elif n < 0.3:
            item = random.choice(items['uncommon'])
        else:
            item = random.choice(items['common'])
        player.inventory.append(item)
        # global items
        items.remove[item]

    def dropGold(self, player):
        if self == Boss:
            gold = random.randint(50, 100)
        else:
            gold = random.randint(5, 20)
        player.gold += gold


class Player(Creature):
    def __init__(self, name, shield, maxHealth=100, currentHealth=100,
                 dps=[1, 4], armorValue=0, evasion=0.2, critChance=0.01,
                 maxWeight=100,currentWeight=0, weapon=None, armor=None,
                 ring=None, gold=0):
        super().__init__(name, dps, armorValue, shield, evasion, critChance)
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.inventory = []
        self.weapon = weapon
        self.shield = shield
        self.armor = armor
        self.ring = ring
        self.gold = gold

    def showChar(self):
        attrs = vars(Player)
        for key, value in attrs.items():
            print(f'{key} = {value}')

    def showInventory(self):
        print(i for i in self.inventory)

    def equipItem(self, item):
        try:
            if item not in self.inventory:
                raise ValueError
            if item == Weapon:
                if not self.handCheck(item):
                    raise ValueError
                if self.weapon:
                    self.unequipItem(item)
                self.weapon = item
                self.currentWeight += item.weight
                self.dps += item.dps
                self.critChance += item.critChance
            elif item == Shield:
                if not self.handCheck(item):
                    raise ValueError
                if self.shield:
                    self.unequipItem(item)
                self.shield = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
            elif item == Armor:
                if self.armor:
                    self.unequipItem(item)
                self.armor = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.evasion += item.evasion
            elif item == Ring:
                if self.ring:
                    self.unequipItem(item)
                self.ring = item
                self.maxHealth += item.maxHealth
                self.dps += item.dps
                self.armorValue += item.armorValue
                self.evasion += item.evasion
                self.critChance += item.critChance
            self.inventory.remove(item)

        except ValueError:
            print(f'{item} not in the inventory or check hands!')  # change

    def unequipItem(self, item):
        try:
            if item not in self.inventory:
                raise ValueError
            if item == Weapon:
                self.weapon = None
                self.currentWeight -= item.weight
                self.dps -= item.dps
                self.critChance -= item.critChance
            elif item == Shield:
                self.shield = None
                self.currentWeight -= item.weight
                self.armorValue -= item.armorValue
            elif item == Armor:
                self.armor = None
                self.currentWeight -= item.weight
                self.armorValue -= item.armorValue
                self.evasion -= item.evasion
            elif item == Ring:
                self.ring = None
                self.maxHealth -= item.maxHealth
                self.dps -= item.dps
                self.armorValue -= item.armorValue
                self.evasion -= item.evasion
                self.critChance -= item.critChance
            self.inventory.append(item)

        except ValueError:
            print(f'{item} not in the inventory!')

    def drinkPotion(self, potion):
        try:
            if potion not in self.inventory:
                raise ValueError
            self.inventory.remove(potion)
            self.health += potion.health
            if self.health > self.maxHealth:
                self.health = self.maxHealth

        except ValueError:
            print(f'{potion} not in the inventory!')

    def handCheck(self, item):
        if item == Weapon:
            return False if item.hand == 'two hand' and self.shield else True
        if item == Shield:
            return False if self.weapon.hand == 'two hand' else True


class Monster(Creature):
    def __init__(self, name, health, dps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, health, dps, armorValue, evasion,
                         critChance, shield)

    # def specialAbility(self)

class Boss(Creature):
    def __init__(self, name, health, dps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, health, dps, armorValue, evasion,
                         critChance, shield)

    # def specialAbility(self):


class Item:
    def __init__(self, name, type, rarity, value, weight):
        self.type = type
        self.name = name
        self.rarity = rarity
        self.value = value
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, type, rarity, value, weight, hand, dps,
                 critChance):
        super().__init__(name, type, rarity, value, weight)
        self.hand = hand
        self.dps = dps
        self.critChance = critChance


class Shield(Item):
    def __init__(self, name, type, rarity, value, weight, armorValue):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue


class Armor(Item):
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion


class Ring(Item):
    def __init__(self, name, rarity, value, maxHealth=None, dps=None,
                 armorValue=None, evasion=None, critChance=None):
        super().__init__(name, rarity, value)
        self.maxHealth = maxHealth
        self.dps = dps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance


class Potion(Item):
    def __init__(self, name, rarity, value, health):
        super().__init__(name, rarity, value)
        self.health = health

class Shrine:
    def __init__(self):

    def heal(self, player):
        player.currentHealth = player.maxHealth

class Chest:
    def __init__(self, items):
        self.items = items

    def open(self, player, items):
        self.itemFind(player, items)
        self.trap(player)

    def itemFind(self, player, items):
        n = random.random()
        if n < 0.3:
            item = random.choice(items['rare'])
        elif n < 0.5:
            item = random.choice(items['uncommon'])
        else:
            item = random.choice(items['common'])
        player.inventory.append(item)
        # global items
        items.remove[item]

    def trap(self, player):
        if random.random() < 0.1:
            player.currentHealth -= random.randint(10, 30)


dagger = Weapon('Dagger', 'dagger', 'common', 3, 2, 'one hand', [3, 7], 0.2)
axe = Weapon('Axe', 'axe', 'common', 5, 5, 'one hand', [5, 10], 0.1)
longSword = Weapon('Long Sword', 'long sword', 'common', 5, 4, 'one hand',
                   [7, 9], 0.05)
twoHandedSword = Weapon('Two Handed Sword', 'two handed sword', 'common', 8, 8,
                        'two hand', [11, 15], 0.1)
twoHandedAxe = Weapon('Two Handed Axe', 'two handed axe', 'common', 9, 10,
                      'two hand', [10, 17], 0.1)
shadowStrike = Weapon('Shadow Strike', 'dagger', 'uncommon', 23, 2, 'one hand',
                      [12, 16], 0.2)
peaceMaker = Weapon('Peace Maker', 'axe', 'uncommon', 28, 6, 'one hand',
                    [12, 20], 0.1)
oathKeeper = Weapon('Oath Keeper', 'long sword', 'uncommon', 26, 4, 'one hand',
                    [15, 18], 0.05)
soulReaper = Weapon('Soul Reaper', 'two handed sword', 'uncommon', 35, 10,
                    'two hand', [35, 40], 0.1)
rapture = Weapon('Rapture', 'two handed axe', 'uncommon', 37, 11,
                 'two hand', [31, 44], 0.1)
sinisterCarver = Weapon('Sinister Carver', 'dagger', 'rare', 50, 2, 'one hand',
                        [42, 50], 0.2)
harbinger = Weapon('Harbinger', 'axe', 'rare', 56, 6, 'one hand', [45, 60], 0.1)
blindJustice = Weapon('Blind Justice', 'long sword', 'rare', 58, 4, 'one hand',
                      [51, 55], 0.05)
stormbringer = Weapon('Two Handed Sword', 'two handed sword', 'rare', 72, 12,
                      'two hand', [72, 79], 0.1)
eclipse = Weapon('Eclipse', 'two handed axe', 'rare', 78, 12, 'two hand',
                 [68, 85], 0.1)

# add more difference between shield types
smallShield = Shield('Small Shield', 'small shield', 'common', 4, 5, 5)
greatShield = Shield('Great Shield', 'great shield', 'common', 6, 10, 11)
dawnGuard = Shield('Dawn Guard', 'small shield', 'uncommon', 13, 6, 13)
heroWarden = Shield('Hero Warden', 'great shield', 'uncommon', 17, 12, 19)
tranquility = Shield('Tranquility', 'small shield', 'rare', 28, 5, 22)
theSentry = Shield('The Sentry', 'small shield', 'rare', 36, 13, 32)

leatherArmor = Armor('Leather Armor', 'light armor', 'common', 8, 10, 16, -0.05)
plateArmor = Armor('Plate Armor', 'heavy armor', 'common', 13, 32, 35, -0.2)
soulOfTheEast = Armor('Soul of the East', 'light armor', 'uncommon', 29, 11, 28,
                      -0.05)
twillightIronArmor = Armor('Twillight Iron Armor', 'heavy armor', 'uncommon',
                           34, 36, 62, -0.2)
favorOfPhantoms = Armor('Favor of Phantoms', 'light armor', 'rare', 62, 10, 42,
                        -0.05)
cryOfTheBerserker = Armor('Cry of the Berserker', 'heavy armor', 'rare', 68, 36,
                          88, -0.2)

items = {'common': {'weapon': [dagger, axe, longSword, twoHandedSword,
                               twoHandedAxe],
                    'armor': [leatherArmor, plateArmor],
                    'shield': [smallShield, greatShield]},
         'uncommon': {'weapon': [shadowStrike, peaceMaker, oathKeeper,
                                 soulReaper],
                      'armor': [soulOfTheEast, twillightIronArmor],
                      'shield': [dawnGuard, heroWarden]},
         'rare': {'weapon': [sinisterCarver, harbinger, blindJustice,
                             stormbringer, eclipse],
                  'armor': [favorOfPhantoms, cryOfTheBerserker],
                  'shield': [tranquility, theSentry]}
         }

rat = Monster('Rat', 20, [1, 3], 0, 0.1, 0.2)
vileBat = Monster('Vile Bat', 15, [2, 3], 0, 0.3, 0.2)
zombie = Monster('Zombie', 30, [3, 5], 5, 0, 0.05)
skeletonWarrior = Monster('Skeleton Warrior', 25, [3, 7], 20, 0.1, 0.1)
lesserShade = Monster('Lesser Shade', 10, [2, 6], 0, 0.5, 0.1)
giantSpider = Monster('Giant Spider', 25, [3, 8], 10, 0.1, 0.1)

darkKnight = Boss('Dark Knight', 80, [10, 15], 50, 0.05, 0.1, shield=True)

shrine = Shrine()

chest = Chest(items)

l1Map = {'s1' : Player, 's2' : vileBat, 's3' : lesserShade, 's4' : chest,
         's5' : rat, 's6' : chest, 's7' : zombie, 's8' : vileBat,
         's9' : chest, 's10' : skeletonWarrior, 's11' : shrine, 's12' : chest,
         's13' : rat, 's14' : giantSpider, 's15' : lesserShade,
         's16' : darkKnight}
