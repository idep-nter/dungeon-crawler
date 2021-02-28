import random
import time
import re


class Creature:
    def __init__(self, name, currentHealth, minDps, maxDps, armorValue,
                 evasion, critChance, shield=None):
        self.name = name
        self.currentHealth = currentHealth
        self.minDps = minDps
        self.maxDps = maxDps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance
        self.shield = shield

    def attack(self, target):
        attack = random.randint(self.minDps, self.maxDps)
        if random.random() < target.evasion:
            print(f'{self.name} missed the attack!')
            return False
        if random.random() < self.critChance:
            attack = (attack / 100) * 150
        if target.shield:
            attack = (attack / 100) * 70
        attack = attack / (1 + (target.armorValue / 100))
        print(f'{target.name} was hit by {attack}!')
        target.currentHealth -= attack

    def itemDrop(self, player):
        n = random.random()
        if n < 0.1:
            item = self.randomItem('rare')
        elif n < 0.3:
            item = self.randomItem('uncommon')
        else:
            item = self.randomItem('common')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def potionDrop(self, player):
        n = random.random()
        if n < 0.3:
            potion = healthPotion
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)
        elif n < 0.6:
            potion = smallHealthPotion
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def randomItem(self, rarity):
        global items
        iType = random.choice(list(items[rarity]))
        item = random.choice(list(items[rarity][iType]))
        return item

    # def specialAbility(self):


class Player(Creature):
    def __init__(self, name, maxHealth=100, currentHealth=100, minDps=1,
                 maxDps=4, armorValue=0, evasion=0.2, critChance=0.1,
                 maxWeight=100, currentWeight=0, gold=0, weapon=None,
                 armor=None, ring1=None, ring2=None, shield=None):
        super().__init__(name, currentHealth, minDps, maxDps, armorValue,
                         evasion, critChance, shield)
        self.inventory = []
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.ring1 = ring1
        self.ring2 = ring2
        self.shield = shield

    def showChar(self): # not showing properly
        attrs = vars(Player)
        for key, value in attrs.items():
            print(f'{key} = {value}')

    def showInventory(self):
        print(i for i in self.inventory)

    def equipItem(self, item):
        try:
            if item not in self.inventory:
                print(f'{item} not in the inventory!')
                raise ValueError
            if not self.weightCheck(item):
                print('You weight too much!')
                raise ValueError
            if isinstance(item, Weapon):
                if not self.handCheck(item):
                    print(f'Cannot equip!')
                    raise ValueError
                if self.weapon:
                    pWeapon = self.weapon
                    self.unequipItem(pWeapon)
                self.weapon = item
                self.currentWeight += item.weight
                self.minDps += item.minDps
                self.maxDps += item.maxDps
                self.critChance += item.critChance
                self.inventory.remove(item)
            elif isinstance(item, Shield):
                if not self.handCheck(item):
                    print(f'Cannot equip!')
                    raise ValueError
                if self.shield:
                    pShield = self.shield
                    self.unequipItem(pShield)
                self.shield = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.inventory.remove(item)
            elif isinstance(item, Armor):
                if self.armor:
                    pArmor = self.armor
                    self.unequipItem(pArmor)
                self.armor = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.evasion += item.evasion
                self.inventory.remove(item)
            elif isinstance(item, Ring):
                if self.ring1 and not self.ring2:
                    self.ring2 = item
                elif not self.ring1 and self.ring2:
                    self.ring1 = item
                elif self.ring1 and self.ring2:
                    pRing = self.ring1
                    self.unequipItem(pRing)
                    self.ring1 = item
                else:
                    self.ring1 = item
                self.maxHealth += item.maxHealth
                self.minDps += item.minDps
                self.maxDps += item.maxDps
                self.armorValue += item.armorValue
                self.evasion += item.evasion
                self.critChance += item.critChance
                self.inventory.remove(item)
        except ValueError:
            pass

    def unequipItem(self, item):
        try:
            if item not in self.inventory:
                raise ValueError
            if isinstance(item, Weapon):
                self.weapon = None
                self.currentWeight -= item.weight
                self.minDps -= item.minDps
                self.maxDps -= item.maxDps
                self.critChance -= item.critChance
            elif isinstance(item, Shield):
                self.shield = None
                self.currentWeight -= item.weight
                self.armorValue -= item.armorValue
            elif isinstance(item, Armor):
                self.armor = None
                self.currentWeight -= item.weight
                self.armorValue -= item.armorValue
                self.evasion -= item.evasion
            elif isinstance(item, Ring):
                if self.ring1 == item:
                    self.ring1 = None
                elif self.ring2 == item:
                    self.ring2 = None
                self.maxHealth -= item.maxHealth
                self.minDps -= item.minDps
                self.maxDps -= item.maxDps
                self.armorValue -= item.armorValue
                self.evasion -= item.evasion
                self.critChance -= item.critChance
            self.inventory.append(item)
        except ValueError:
            print(f'{item} not in the inventory!')

    def drinkPotion(self):
        potion = self.potionChoice
        heal = potion.heal
        pHealth = self.currentHealth
        self.currentHealth += heal
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
            heal = self.maxHealth - pHealth
            print(f'{heal} health healed!')
        else:
            print(f'{heal} health healed!')
            self.inventory.remove(potion)

    def potionChoice(self):
        try:
            if Potion not in self.inventory:
                print('No potions in the inventory!')
                raise ValueError
            elif smallHealthPotion in self.inventory and healthPotion not in \
                    self.inventory:
                potion = smallHealthPotion
                return potion
            elif healthPotion in self.inventory and smallHealthPotion not in \
                    self.inventory:
                potion = healthPotion
                return potion
            else:
                q = input('Which potion do you want to use? Small or '
                          'big?').lower()
                if q == 'small':
                    potion = smallHealthPotion
                    return potion
                elif q == 'big':
                    potion = healthPotion
                    return potion
                else:
                    print('Please type correct potion size!')
                    raise ValueError
        except ValueError:
            pass

    def death(self):
        return True if self.currentHealth <= 0 else False

    def handCheck(self, item):
        if isinstance(item, Greataxe) or isinstance(item, Greatsword) and \
                self.shield:
            return False
        if isinstance(item, Shield) and isinstance(self.weapon, Greataxe) or \
                isinstance(self.weapon, Greatsword):
            return False
        return True

    def weightCheck(self, item):
        return False if self.currentWeight + item.weight > self.maxWeight else \
            True


class Monster(Creature):
    def __init__(self, name, currentHealth, minDps, maxDps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, currentHealth, minDps, maxDps, armorValue,
                         evasion, critChance, shield)

    def goldDrop(self, player):
        gold = random.randint(5, 20)
        print(f'You have found {gold} gold!')
        player.gold += gold

    def death(self, player):
        if self.currentHealth <= 0:
            self.itemDrop(player)
            self.goldDrop(player)
            self.potionDrop(player)
            return True
        return False

class Boss(Creature):
    def __init__(self, name, currentHealth, minDps, maxDps, armorValue, evasion,
                 critChance, shield=None):
        super().__init__(name, currentHealth, minDps, maxDps, armorValue,
                         evasion, critChance, shield)

    def death(self, player):
        if self.currentHealth <= 0:
            self.itemDrop(player)
            self.goldDrop(player)
            self.potionDrop(player)
            return True
        return False

    def itemDrop(self, player): # need to checkout override
        item = self.randomItem('rare')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def goldDrop(self, player):
        gold = random.randint(50, 100)
        print(f'You have found {gold} gold!')
        player.gold += gold

    def potionDrop(self, player):  # need to checkout override
        potion = healthPotion
        print(f'You have found {potion.name}!')
        player.inventory.append(potion)


class Item:
    def __init__(self, name, type, rarity, value, weight=None):
        self.type = type
        self.name = name
        self.rarity = rarity
        self.value = value
        self.weight = weight

    def itemView(self): # mb not showing all attributes
        attrs = vars(Item)
        for key, value in attrs.items():
            print(f'{key} = {value}')


class Weapon(Item):
    def __init__(self, name, type, rarity, value, weight, minDps, maxDps,
                 critChance):
        super().__init__(name, type, rarity, value, weight)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance


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


class Potion(Item):
    def __init__(self, name, type, rarity, value, heal):
        super().__init__(name, type, rarity, value)
        self.heal = heal


class Shrine:
    def __init__(self):
        pass

    def heal(self, player):
        player.currentHealth = player.maxHealth


class Chest:
    def __init__(self):
        pass

    def open(self, player):
        self.itemFind(player)
        self.potionFind(player)
        self.trap(player)

    def itemFind(self, player):
        n = random.random()
        if n < 0.3:
            item = self.randomItem('rare')
        elif n < 0.5:
            item = self.randomItem('uncommon')
        else:
            item = self.randomItem('common')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def randomItem(self, rarity):
        global items
        iType = random.choice(list(items[rarity]))
        item = random.choice(list(items[rarity][iType]))
        return item

    def potionFind(self, player):
        n = random.random()
        if n < 0.5:
            potion = healthPotion
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)
        else:
            potion = smallHealthPotion
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def trap(self, player):
        if random.random() < 0.1:
            player.currentHealth -= random.randint(10, 30)


class Level(list):

    def __str__(self):
        return "\n".join(' '.join(row) for row in self)


class Game:
    markerX = 'X'
    markerO = 'O'
    ctrls = ['left', None, 'right', 'up', None, 'down']
    exit = 'quit'
    start = [2, 0]
    default = [['?'] * 4 for i in range(4)]

    def __init__(self, map):
        self.flag = True
        self.level = Level(Game.default)
        self.oLevel = Level(map)
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

    def action(self, player):
        cx, cy = self.currPos
        object = self.oLevel[cy][cx]
        if isinstance(object, Shrine):
            print('You see some kind of shrine before you and suddenly feel '
                  'strength coming back to your body.')
            object.heal(player)
            self.oLevel[cy][cx] = None
        elif isinstance(object, Chest):
            print('You see a wooden chest before you. What treasures does it '
                  'hold? You shiver with excitement as you opening it...')
            object.open(player)
            self.oLevel[cy][cx] = None
        elif isinstance(object, Monster):
            print(f'Damn, you see a {object.name}!')
            pAction = True
            while pAction:
                c = self.command(player)
                if c == 'auto-attack':
                    while True:
                        if self.battle(player, object, cx, cy):
                            pAction = False
                            break
                else:
                    if self.battle(player, object, cx, cy):
                        pAction = False
        elif isinstance(object, Boss):
            print(f'Damn, you see a {object.name}! He looks tough!')
            pAction = True
            while pAction:
                c = self.command(player)
                if c == 'auto-attack':
                    while True:
                        if self.battle(player, object, cx, cy):
                            pAction = False
                            break
                else:
                    if self.battle(player, object, cx, cy):
                        pAction = False

    def battle(self, player, object, cx, cy):
        time.sleep(1)
        player.attack(object)
        if object.death(player):
            self.oLevel[cy][cx] = None # mb not working
            return True
        else:
            time.sleep(1)
            object.attack(player)
            if player.death():
                print('YOU DIED')
                self.flag = False
            time.sleep(1)

    def command(self, player):
        global items
        eq = re.compile(r'equip (\w)+')
        uneq = re.compile(r'unequip (\w)+')
        view = re.compile(r'view (\w)+')
        while True:
            try:
                a = input('What\'s your action? ').lower()
                if a == 'attack' or a == 'auto-attack':
                    return a
                if a == 'help':
                    help()
                elif a == 'char':
                    player.showChar()
                elif a == 'inv':
                    player.showInventory()
                elif a == eq:
                    mo = eq.search(a)
                    item = mo.group(1)
                    player.equipItem(item)
                    print(f'{item} equiped!')
                elif a == uneq:
                    mo = uneq.search(a)
                    item = mo.group(1)
                    player.unequipItem(item)
                    print(f'{item} unequiped!')
                elif a == view:
                    mo = uneq.search(a)
                    item = mo.group(1)
                    item = items[item]
                    item.itemView()
                elif a == 'drink':
                    player.drinkPotion()
                elif a == Game.exit:
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
            print(str(self.level) + '\n')
            ctrl = input('Which way would you like to go? ').lower()
            if ctrl in Game.ctrls:
                d = Game.ctrls.index(ctrl)
                self.prevPos = self.currPos[:]
                self.currPos[d > 2] += d - (1 if d < 3 else 4)
                self.movePlayer()
                breakpoint()
                self.action(player)
            elif ctrl == Game.exit:
                self.flag = False
            else:
                print('Please enter a proper direction.')


dagger = Dagger('Dagger', 'dagger', 'common', 3, 2, 3, 7, 0.2)
axe = SmallAxe('Axe', 'small axe', 'common', 5, 5, 5, 10, 0.1)
longsword = Longsword('Longsword', 'longsword', 'common', 5, 4, 7, 9, 0.05)
greatsword = Greatsword('Greatsword', 'greatsword', 'common', 8, 8,
                        11, 15, 0.1)
greataxe = Greataxe('Greataxe', 'greataxe', 'common', 9, 10,
                      10, 17, 0.1)
shadowStrike = Dagger('Shadow Strike', 'dagger', 'uncommon', 23, 2, 12, 16,
                      0.2)
peaceMaker = SmallAxe('Peace Maker', 'small axe', 'uncommon', 28, 6, 12, 20, 0.1)
oathKeeper = Longsword('Oath Keeper', 'longsword', 'uncommon', 26, 4, 15, 18,
                    0.05)
soulReaper = Greatsword('Soul Reaper', 'greatsword', 'uncommon', 35, 10,
                    35, 40, 0.1)
rapture = Greataxe('Rapture', 'greataxe', 'uncommon', 37, 11, 31, 44, 0.1)
sinisterCarver = Dagger('Sinister Carver', 'dagger', 'rare', 50, 2, 42, 50, 0.2)
harbinger = SmallAxe('Harbinger', 'small axe', 'rare', 56, 6, 45, 60, 0.1)
blindJustice = Longsword('Blind Justice', 'longsword', 'rare', 58, 4, 51, 55,
                      0.05)
stormbringer = Greatsword('Stormbringer', 'greatsword', 'rare', 72, 12,
                      72, 79, 0.1)
eclipse = Greataxe('Eclipse', 'greataxe', 'rare', 78, 12, 68, 85, 0.1)
smallShield = SmallShield('Small Shield', 'small shield', 'common', 4, 5, 5, -0.1)
greatshield = Greatshield('Greatshield', 'greatshield', 'common', 6, 10, 11, -0.2)
dawnGuard = SmallShield('Dawn Guard', 'small shield', 'uncommon', 13, 6, 13, -0.1)
heroWarden = Greatshield('Hero Warden', 'greatshield', 'uncommon', 17, 12, 19, -0.2)
tranquility = SmallShield('Tranquility', 'small shield', 'rare', 28, 5, 22, -0.1)
theSentry = Greatshield('The Sentry', 'greatshield', 'rare', 36, 13, 32, -0.2)
leatherArmor = LightArmor('Leather Armor', 'light armor', 'common', 8, 10, 16, -0.1)
plateArmor = HeavyArmor('Plate Armor', 'heavy armor', 'common', 13, 32, 35, -0.2)
soulOfTheEast = LightArmor('Soul of the East', 'light armor', 'uncommon', 29, 11, 28,
                      -0.1)
twilightIronArmor = HeavyArmor('Twilight Iron Armor', 'heavy armor', 'uncommon',
                           34, 36, 62, -0.2)
favorOfPhantoms = LightArmor('Favor of Phantoms', 'light armor', 'rare', 62, 10, 42,
                        -0.1)
cryOfTheBerserker = HeavyArmor('Cry of the Berserker', 'heavy armor', 'rare', 68, 36,
                          88, -0.2)
jasperWhisper = Ring('Jasper Whisper', 'ring', 'uncommon', 12, evasion=0.1)
lunarShield = Ring('Lunar Shield', 'ring', 'uncommon', 11, armorValue=15)
jadeMoon = Ring('Jade Moon', 'ring', 'uncommon', 15, critChance=0.1)
emeraldFlame = Ring('Emerald Flame', 'ring', 'uncommon', 13, minDps=5,
                    maxDps=10)
lavishSpirit = Ring('Lavish Spirit', 'ring', 'rare', 25, evasion=0.2)
moltenCore = Ring('Molten Core', 'ring', 'rare', 22, armorValue=32)
forsakenPromise = Ring('Forsaken Promise', 'ring', 'rare', 26, critChance=0.2)
ancientVigor = Ring('Ancient Vigor', 'ring', 'rare', 25, minDps=11, maxDps=18)
smallHealthPotion = Potion('Small Health Potion', 'potion', 'common', 10, 20)
healthPotion = Potion('Health Potion', 'potion', 'common', 20, 40)

items = {'common': {'weapon': [dagger, axe, longsword, greatsword,
                               greataxe],
                    'armor': [leatherArmor, plateArmor],
                    'shield': [smallShield, greatshield]},
         'uncommon': {'weapon': [shadowStrike, peaceMaker, oathKeeper,
                                 soulReaper],
                      'armor': [soulOfTheEast, twilightIronArmor],
                      'shield': [dawnGuard, heroWarden],
                      'ring': [jasperWhisper, lunarShield, jadeMoon,
                               emeraldFlame]},
         'rare': {'weapon': [sinisterCarver, harbinger, blindJustice,
                             stormbringer, eclipse],
                  'armor': [favorOfPhantoms, cryOfTheBerserker],
                  'shield': [tranquility, theSentry],
                  'ring': [lavishSpirit, moltenCore, forsakenPromise,
                           ancientVigor]}
         }
potions = {'common': [smallHealthPotion, healthPotion]}

rat = Monster('Rat', 20, 1, 3, 0, 0.1, 0.2)
vileBat = Monster('Vile Bat', 1, 2, 3, 0, 0.3, 0.2)
zombie = Monster('Zombie', 30, 3, 5, 5, 0, 0.05)
skeletonWarrior = Monster('Skeleton Warrior', 25, 3, 7, 20, 0.1, 0.1)
lesserShade = Monster('Lesser Shade', 10, 2, 6, 0, 0.5, 0.1)
giantSpider = Monster('Giant Spider', 25, 3, 8, 10, 0.1, 0.1)
darkKnight = Boss('Dark Knight', 80, 10, 15, 50, 0.05, 0.1, shield=True)
shrine = Shrine()
chest = Chest()

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

def gameRules():
    print("""
                                GAME RULES
================================================================================
The dungeon you want to escape from consists of several rooms which are filled
with objects and monsters. At the start and after clearing each room you will
be asked which way do you want to continue. If you encounter a monster you will
be given time to prepare e.g. refill health, switch gear etc. You can also do it 
after each round.

The game ends when you defeat the boss of the level or you die trying... 
================================================================================
""")

def help():
    print("""
COMMANDS:
attack             attack a monster
auto-attack        attack a monster until the fight ends
char               shows your statistics and equiped gear
inv                shows your inventory 
equip >item<       equip an item
unequip >item<     unequip an item
view >item<        shows attributes of an item
drink              drink a potion to regain health
quit               exit game       
""")

if __name__ == '__main__':
    game = Game(map)
    game.play()

