import random
import time
import re


class Creature:
    def __init__(self, name, currentHealth, dps, armorValue,
                 evasion, critChance, shield=None):
        self.name = name
        self.currentHealth = currentHealth
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
        if target.shield:
            attack = (attack / 100) * 70
        attack = attack / (1 + (target.armorValue / 100))
        print(f'{target.name} was hit by {attack}!')
        target.currentHealth -= attack

    def death(self):
         return True if self.currentHealth < 0 else False

    def itemDrop(self, player, items):
        if self == Boss:
            item = random.choice(items['rare'])
            print(f'You have found {item}!')
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
        print(f'You have found {item}!')
        player.inventory.append(item)
        # global items
        items.remove[item]

    def dropGold(self, player):
        if self == Boss:
            gold = random.randint(50, 100)
        else:
            gold = random.randint(5, 20)
        print(f'You have found {gold} gold!')
        player.gold += gold

    # def specialAbility(self):


class Player(Creature):
    def __init__(self, name, maxHealth=100, currentHealth=100,
                 dps=[1, 4], armorValue=0, evasion=0.2, critChance=0.1,
                 maxWeight=100, currentWeight=0, gold=0, weapon=None,
                 armor=None, ring=None, shield=None):
        super().__init__(name, dps, armorValue, shield, evasion, critChance)
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.gold = gold
        self.inventory = []
        self.weapon = weapon
        self.armor = armor
        self.ring = ring
        self.shield = shield

    def showChar(self):
        attrs = vars(Player)
        for key, value in attrs.items():
            print(f'{key} = {value}')

    def showInventory(self):
        print(i for i in self.inventory)

    def equipItem(self, item):
        while True:
            if item not in self.inventory:
                print(f'{item} not in the inventory!')
                break
            if not self.weightCheck(item):
                print('You weight too much!')
                break
            if item == Weapon:
                if not self.handCheck(item):
                    print(f'Cannot equip!')
                    break
                if self.weapon:
                    self.unequipItem(item)
                self.weapon = item
                self.currentWeight += item.weight
                self.dps += item.dps
                self.critChance += item.critChance
                self.inventory.remove(item)
                break
            elif item == Shield:
                if not self.handCheck(item):
                    print(f'Cannot equip!')
                    break
                if self.shield:
                    self.unequipItem(item)
                self.shield = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.inventory.remove(item)
                break
            elif item == Armor:
                if self.armor:
                    self.unequipItem(item)
                self.armor = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.evasion += item.evasion
                self.inventory.remove(item)
                break
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
                break

    def unequipItem(self, item):
        try:
            if item
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
            self.currentHealth += potion.heal
            if self.currentHealth > self.maxHealth:
                self.currentHealth = self.maxHealth

        except ValueError:
            print(f'{potion} not in the inventory!')

    def handCheck(self, item):
        if item == Weapon:
            return False if item.hand == 'two hand' and self.shield else True
        if item == Shield:
            return False if self.weapon.hand == 'two hand' else True

    def weightCheck(self, item):
        return False if self.currentWeight + item.weight > self.maxWeight else \
            True


class Monster(Creature):
    def __init__(self, name, currentHealth, dps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, currentHealth, dps, armorValue, evasion,
                         critChance, shield)


class Boss(Creature):
    def __init__(self, name, currentHealth, dps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, currentHealth, dps, armorValue, evasion,
                         critChance, shield)


class Item:
    def __init__(self, name, type, rarity, value, weight=None):
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
    def __init__(self, name, type, rarity, value, weight, armorValue, evasion):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion


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
    def __init__(self, name, rarity, value, heal):
        super().__init__(name, rarity, value)
        self.heal = heal

class Shrine:
    def __init__(self):
        pass

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

class Level(list):

    def __str__(self):
        return "\n".join(' '.join(row) for row in self)


class Game(): # add show map!
    markerX = 'X'
    markerO = 'O'
    ctrls = ['left', None, 'right', 'up', None, 'down']
    exit = 'quit'
    start = [0, 3]
    default = [['?'] * 4 for i in range(4)]

    # guessing - need to somehow access this
    global map
    global items


    def __init__(self):
        self.flag = True
        self.level = Level(Game.default)
        self.oLevel = Level(Game.map)
        self.prevPos = Game.start[:]
        self.currPos = Game.start[:]
        self.movePlayer()

    def movePlayer(self):
        px, py = self.prevPos
        cx, cy = self.currPos
        if (-1 < cx < 4) and (-1 < cy < 4):
            self.level[py][px] = Game.markerO
            self.level[cy][cx] = Game.markerX
        else:
            print('Please enter a proper direction.')
            self.currPos = self.prevPos[:]
            self.movePlayer()

    def action(self, player, items):
        cx, cy = self.currPos
        object = self.oLevel[cy][cx]
        if object == Shrine:
            print('You see some kind of shrine before you and suddenly feel '
                  'strength coming back to your body.')
            object.heal(player)
        elif object == Chest:
            print('You see a wooden chest before you. What treasures does it '
                  'hold? You shiver with excitement as you opening it...')
            object.open(player, items)
        elif object == Monster:
            move = input(f'There is a {object.name}! Are you ready to fight? ')
            if move.lower() == 'yes':
                while True:
                    command(player)
                    time.sleep(1)
                    player.attack(object)
                    if object.death():
                        object.itemDrop(player, items)
                        object.dropGold(player)
                        break
                    else:
                        time.sleep(1)
                        object.attack(player)
                        if player.death():
                            print('YOU DIED')
                            self.flag = False
                        time.sleep(1)
        elif object == Boss:
            print(f'Damn, you see a {object.name}! He looks tough!)
                while True:
                    command(player)
                    time.sleep(1)
                    player.attack(object)
                    if object.death():
                        object.itemDrop(player, items)
                        object.dropGold(player)
                        print('LEVEL CLEARED')
                        self.flag = False
                    else:
                        time.sleep(1)
                        object.attack(player)
                        if player.death():
                            print('YOU DIED')
                            self.flag = False
                        time.sleep(1)

    def command(self, player):
        reg = re.compile(r'(un)?equip (\w)+')
        while True:
            try:
                a = input('What\'s your action?')
                if a == 'attack':
                    break
                if a == 'help':
                    help()
                elif a == 'char':
                    player.showChar()
                elif a == 'inv':
                    player.showInventory()
                elif a == reg
                    mo = reg.search(a)
                    item = mo.group(2)
                    player.equipItem(item)
                elif a == reg
                    mo = reg.search(a)
                    item = mo.group(2)
                    player.unequipItem(item)
                elif a == 'drink':
                    player.drinkPotion()
                elif a == 'quit':
                    self.flag = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter correct command or type \"help\".')
                continue

    def play(self):
        intro1()
        name = input()
        player = Player(name)
        intro2(name)
        gameRules()
        while self.flag:
            print(str(self.level))
            ctrl = input('Which way would you like to go?').lower()
            if ctrl in Game.ctrls:
                d = Game.ctrls.index(ctrl)
                self.prevPos = self.currPos[:]
                self.currPos[d > 2] += d - (1 if d < 3 else 4) # need to look at
                self.movePlayer()
                self.action(player, items)
            elif ctrl == Game.exit:
                self.flag = False
            else:
                print('Please enter a proper direction.')


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
smallShield = Shield('Small Shield', 'small shield', 'common', 4, 5, 5, -0.1)
greatShield = Shield('Great Shield', 'great shield', 'common', 6, 10, 11, -0.2)
dawnGuard = Shield('Dawn Guard', 'small shield', 'uncommon', 13, 6, 13, -0.1)
heroWarden = Shield('Hero Warden', 'great shield', 'uncommon', 17, 12, 19, -0.2)
tranquility = Shield('Tranquility', 'small shield', 'rare', 28, 5, 22, -0.1)
theSentry = Shield('The Sentry', 'small shield', 'rare', 36, 13, 32, -0.2)
leatherArmor = Armor('Leather Armor', 'light armor', 'common', 8, 10, 16, -0.1)
plateArmor = Armor('Plate Armor', 'heavy armor', 'common', 13, 32, 35, -0.2)
soulOfTheEast = Armor('Soul of the East', 'light armor', 'uncommon', 29, 11, 28,
                      -0.1)
twillightIronArmor = Armor('Twillight Iron Armor', 'heavy armor', 'uncommon',
                           34, 36, 62, -0.2)
favorOfPhantoms = Armor('Favor of Phantoms', 'light armor', 'rare', 62, 10, 42,
                        -0.1)
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

map = [[lesserShade, vileBat, None, chest], [rat, chest, zombie, vileBat],
       [chest, skeletonWarrior, shrine, chest], [rat, giantSpider, lesserShade,
                                                 darkKnight]]

def intro1():
    print("""
You wake up in the darkness. Your head hurts like some troll hit it with a huge 
club. You remember nothing... wait! You remember your name which is...     
    """)

def intro2(name):
    print(f"""
Oh yes, you are {name}.! That\'s right. After a while you got used to the dark 
and realized you had woke up in a cell. Somebody had to lock you up after he had 
knocked you out. You try to get up and then you notice that the cell doors are 
open. OK, let\'s do this! You step into the unknown... 

You come to an empty room consisting of doors on each side lit by torches.
""")

def gameRules()
    print("""
                GAME RULES
============================================


=============================================
""")

def help()
    print("""
COMMANDS:
attack             attack monster
char               shows your statistics and equiped gear
inv                shows your inventory 
equip >item<       equips item
unequip >item<     unequips item
drink              drink potion to regain health
quit               exit game       
""")
