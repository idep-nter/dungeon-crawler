import time
import re
import creatures as cr
import items as it
import objects as ob
import random

dagger = it.Dagger('Dagger', 'Dagger', 'Common', 3, 2, 4, 0.2, 0, 2)
axe = it.SmallAxe('Axe', 'Small Axe', 'Common', 5, 3, 6, 0.1, 0, 5)
longsword = it.Longsword('Longsword', 'Longsword', 'Common', 5, 4, 7, 0.05, 0,
                         4)
greatsword = it.Greatsword('Greatsword', 'Greatsword', 'Common', 8, 6, 10,
                           0.1, 0.5, 8)
greataxe = it.Greataxe('Greataxe', 'Greataxe', 'Common', 9, 5, 11, 0.15, 0.5,
                       10)
swiftDagger = it.Dagger('Swift Dagger', 'Dagger', 'Uncommon', 7, 3, 7, 0.2, 0,
                        2)
battleAxe = it.SmallAxe('Battle Axe', 'Small Axe', 'Uncommon', 8, 4, 9, 0.1, 0,
                        5)
noblemansSword = it.Longsword('Nobleman\'s sword', 'Longsword', 'Uncommon', 8,
                              6, 11, 0.05, 0, 4)
balancedGreatSword = it.Greatsword('Balanced Greatsword', 'Greatsword',
                                   'Uncommon', 13, 9, 15, 0.1, 0.5, 8)
chieftainsGreataxe = it.Greataxe('Chieftain\'s Greataxe', 'Greataxe',
                                 'Uncommon', 12, 8, 14, 0.15, 0.5, 10)
shadowStrike = it.Dagger('Shadow Strike', 'Dagger', 'Rare', 23, 8, 14,
                         0.2, 0, 2)
peaceMaker = it.SmallAxe('Peace Maker', 'Small Axe', 'Rare', 28, 11, 17,
                         0.1, 0, 6)
oathKeeper = it.Longsword('Oath Keeper', 'Longsword', 'Rare', 26, 13, 18,
                          0.05, 0, 4)
soulReaper = it.Greatsword('Soul Reaper', 'Greatsword', 'Rare', 35, 20,
                           28, 0.1, 0.5, 10)
rapture = it.Greataxe('Rapture', 'Greataxe', 'Rare', 37, 18, 27, 0.15, 0.5, 11)
sinisterCarver = it.Dagger('Sinister Carver', 'Dagger', 'Epic', 50, 17, 25,
                           0.2, 0, 2)
harbinger = it.SmallAxe('Harbinger', 'Small Axe', 'Epic', 56, 23, 30, 0.1, 0,
                        6)
blindJustice = it.Longsword('Blind Justice', 'Longsword', 'Epic', 58, 26, 32,
                            0.05, 0, 4)
stormbRinger = it.Greatsword('StormbRinger', 'Greatsword', 'Epic', 72, 39,
                             45, 0.1, 0.5, 12)
eclipse = it.Greataxe('Eclipse', 'Greataxe', 'Epic', 78, 36, 44, 0.15, 0.5, 36)
smallShield = it.SmallShield('Small Shield', 'Small Shield', 'Common', 4, 5,
                             -0.1, 0.15, 5)
greatshield = it.Greatshield('Greatshield', 'Greatshield', 'Common', 6, 11,
                             -0.3, 0.3, 10)
compactShied = it.SmallShield('Compact Shield', 'Small Shield', 'Uncommon', 8,
                              8, -0.1, 0.15, 5)
sturdyGreatshield = it.Greatshield('Sturdy Greatshield', 'Greatshield',
                                   'Uncommon', 10, 15, -0.3, 0.3, 11)
dawnGuard = it.SmallShield('Dawn Guard', 'Small Shield', 'Rare', 16, 16,
                           -0.1, 0.15, 6)
heroWarden = it.Greatshield('Hero Warden', 'Greatshield', 'Rare', 19, 27, -0.3,
                            0.3,
                            12)
tranquility = it.SmallShield('Tranquility', 'Small Shield', 'Epic', 35, 27,
                             -0.1, 0.15, 5)
theSentry = it.Greatshield('The Sentry', 'Greatshield', 'Epic', 40, 38, -0.3,
                           0.3,
                           13)
leatherArmor = it.LightArmor('Leather Armor', 'Light Armor', 'Common', 8, 16,
                             -0.1, 10)
plateArmor = it.HeavyArmor('Plate Armor', 'Heavy Armor', 'Common', 13, 35, -0.2,
                           32)
scoutsLeatherArmor = it.LightArmor('Scout\'s Leather Armor', 'Light Armor',
                                   'Uncommon', 8, 25, -0.1, 10)
knightsPlateArmor = it.HeavyArmor('Knight\'s Plate Armor', 'Heavy Armor',
                                  'Uncommon', 13, 41, -0.2, 32)
soulOfTheEast = it.LightArmor('Soul of the East', 'Light Armor', 'Rare', 38,
                              28, -0.1, 11)
twilightIronArmor = it.HeavyArmor('Twilight Iron Armor', 'Heavy Armor',
                                  'Rare', 34, 55, -0.2, 36)
favorOfPhantoms = it.LightArmor('Favor of Phantoms', 'Light Armor', 'Epic', 62,
                                48, -0.1, 8)
cryOfTheBerserker = it.HeavyArmor('Cry of the Berserker', 'Heavy Armor', 'Epic',
                                  68, 88, -0.2, 40)
silverRing = it.Ring('Silver Ring', 'Ring', 'Common', 3)
goldRing = it.Ring('Gold Ring', 'Ring', 'Uncommon', 6)
jasperWhisper = it.Ring('Jasper Whisper', 'Ring', 'Rare', 12, evasion=0.1)
lunarShield = it.Ring('Lunar Shield', 'Ring', 'Rare', 11, armorValue=15)
jadeMoon = it.Ring('Jade Moon', 'Ring', 'Rare', 15, critChance=0.1)
serpentHead = it.Ring('Serpent Head', 'Ring', 'Rare', 16, critMulti=0.1)
emeraldFlame = it.Ring('Emerald Flame', 'Ring', 'Rare', 13, minDps=5,
                       maxDps=10)
lavishSpirit = it.Ring('Lavish Spirit', 'Ring', 'Epic', 25, evasion=0.2)
moltenCore = it.Ring('Molten Core', 'Ring', 'Epic', 22, armorValue=32)
forsakenPromise = it.Ring('Forsaken Promise', 'Ring', 'Epic', 26,
                          critChance=0.2)
ancientVigor = it.Ring('Ancient Vigor', 'Ring', 'Epic', 25, minDps=11,
                       maxDps=18)
coupDeGrace = it.Ring('Coup de grâce', 'Ring', 'Epic', 25, critMulti=0.3)
smallHealthPotion = it.HealthPotion('Small Health Potion', 'Potion', 'Common',
                                    10, 20)
healthPotion = it.HealthPotion('Health Potion', 'Potion', 'Common', 20, 40)
regen = it.RegenPotion('Regeneration Potion', 'Potion', 'Common', 15, 5)
antidote = it.Antidote('Antidote', 'potion', 'Common', 10)

potions = [smallHealthPotion, healthPotion, regen, antidote]


items = {'common': {'weapon': [dagger, axe, longsword, greatsword,
                               greataxe],
                    'armor': [leatherArmor, plateArmor],
                    'shield': [smallShield, greatshield]},
         'uncommon': {'weapon': [swiftDagger, battleAxe, noblemansSword,
                                 balancedGreatSword, chieftainsGreataxe],
                      'armor': [scoutsLeatherArmor, knightsPlateArmor],
                      'shield': [compactShied, sturdyGreatshield]},
         'rare': {'weapon': [shadowStrike, peaceMaker, oathKeeper, soulReaper],
                  'armor': [soulOfTheEast, twilightIronArmor],
                  'shield': [dawnGuard, heroWarden],
                  'ring': [jasperWhisper, lunarShield, jadeMoon, emeraldFlame,
                           serpentHead]},
         'epic': {'weapon': [sinisterCarver, harbinger, blindJustice,
                             stormbRinger, eclipse],
                  'armor': [favorOfPhantoms, cryOfTheBerserker],
                  'shield': [tranquility, theSentry],
                  'ring': [lavishSpirit, moltenCore, forsakenPromise,
                           ancientVigor, coupDeGrace]}
         }

rat = cr.Monster('Rat', 1, 20, 1, 1, 3, 0, 0.1, 0.2, 2, 0,
                 random.randint(300, 500), potions, items)
vileBat = cr.Monster('Vile Bat', 1, 15, 1, 2, 3, 0, 0.3, 0.2, 1.5, 0,
                     random.randint(300, 500), potions, items)
zombie = cr.Monster('Zombie', 2, 30, 1, 3, 5, 5, 0, 0.05, 1.5, 0,
                    random.randint(400, 700), potions, items)
skeletonWarrior = cr.Monster('Skeleton Warrior', 2, 25, 1, 3, 7, 20, 0.1, 0.1,
                             1.5, 0.15, random.randint(400, 700), potions,
                             items)
lesserShade = cr.Monster('Lesser Shade', 1, 10, 1, 2, 6, 0, 0.5, 0.1, 1.5, 0,
                         random.randint(300, 500), potions, items)
giantSpider = cr.Monster('Giant Spider', 2, 25, 1, 3, 8, 10, 0.1, 0.1, 1.5, 0,
                         random.randint(400, 700), potions, items)
darkKnight = cr.Boss('Dark Knight', 4, 80, 1, 10, 15, 50, 0.05, 0.1, 2, 0.3,
                     random.randint(1500, 2000), potions, items)
chest = ob.Chest(potions, items)
shrine = ob.Shrine()


mapObjects = [rat, vileBat, zombie, skeletonWarrior, lesserShade, giantSpider,
              chest, shrine, None, None]


class Level(list):

    def __str__(self):
        return "\n".join(' '.join(row) for row in self)


class Game:
    markerX = 'X'
    markerO = 'O'
    ctrls = ['left', None, 'right', 'up', None, 'down']
    exit = 'quit'
    sx = random.randint(0, 4)
    sy = random.randint(0, 7)
    start = [sx, sy]
    default = [['?'] * 8 for i in range(5)]
    mapObj = mapObjects

    def __init__(self):
        self.flag = True
        self.level = Level(Game.default)
        self.oLevel = Level(self.mapGenerator())
        self.prevPos = Game.start[:]
        self.currPos = Game.start[:]
        self.movePlayer()

    def mapGenerator(self):
        map = []
        for i in range(5):
            line = []
            for x in range(8):
                object = random.choice(self.mapObj)
                line.append(object)
            map.append(line)
        map[self.start[0]][self.start[1]] = None
        while True:
            nList = random.randint(0, 4)
            nIndex = random.randint(0, 7)
            if map[nList][nIndex] == map[self.start[0]][self.start[1]]:
                continue
            else:
                map[nList][nIndex] = darkKnight
                break
        return map

    def movePlayer(self):
        try:
            px, py = self.prevPos
            cx, cy = self.currPos
            if (-1 < cx < 8) and (-1 < cy < 8):
                if self.bossCheck(cx, cy):
                    self.level[px][py] = Game.markerO
                    self.level[cx][cy] = Game.markerX
                    return True
                else:
                    return False
            else:
                raise ValueError
        except ValueError:
            print('You can\'t go in there.')
            return False

    def bossCheck(self, cx, cy):
        object = self.oLevel[cx][cy]
        if isinstance(object, cr.Boss):
            while True:
                try:
                    q = input('You feel that something terribly dangerous '
                              'dwells in this room, do you really want to '
                              'continue? ')
                    if q.lower() == 'yes' or q.lower() == 'y':
                        return True
                    elif q.lower() == 'no' or q.lower() == 'n':
                        self.level[cx][cy] = '!'
                        return False
                    else:
                        raise ValueError
                except ValueError:
                    print('Please answer \'yes\' or \'no\'.')
        return True

    def action(self, player):
        cx, cy = self.currPos
        object = self.oLevel[cx][cy]
        if isinstance(object, ob.Shrine):
            print('You see some kind of shrine before you and suddenly feel '
                  'strength coming back to your body.')
            object.heal(player)
            self.oLevel[cx][cy] = None
        elif isinstance(object, ob.Chest):
            print('You see a wooden chest before you. What treasures does it '
                  'hold? You shiver with excitement as you opening it...')
            time.sleep(1)
            object.open(player)
            self.oLevel[cx][cy] = None
        elif isinstance(object, cr.Monster):
            print(f'Damn, you see a {object.name}!')
            pAction = True
            while pAction:
                self.showStats(player, object)
                c = self.command(player)
                if c == 'auto-attack' or 'auto':
                    while True:
                        if self.battle(player, object, cx, cy):
                            pAction = False
                            break
                else:
                    if self.battle(player, object, cx, cy):
                        pAction = False
        elif isinstance(object, cr.Boss):
            print(f'Damn, you see a {object.name}! He looks tough!')
            pAction = True
            while pAction:
                self.showStats(player, object)
                c = self.command(player)
                if c == 'auto-attack' or 'auto':
                    while True:
                        if self.battle(player, object, cx, cy):
                            pAction = False
                            break
                else:
                    if self.battle(player, object, cx, cy):
                        pAction = False

    @staticmethod
    def showStats(player, object):
        hp = f'HP: {player.currentHealth}/{player.maxHealth}'
        ap = f'AP: {player.currentAp}/{player.maxAp}'
        eHp = f'HP: {object.currentHealth}/{object.maxHealth}'
        print(f'\n{player.name}\n' + hp + '\n' + ap + '\n')
        print(f'{object.name}\n' + eHp)


    @staticmethod
    def special(object, player, attack): # add other statuses + special for player
        if object == zombie:
            object.regenerate()
        elif object == vileBat:
            if attack:
                object.stealLife(attack)
        elif object == giantSpider and 'poisoned' not in player.status:
            if object.poison():
                player.status.append('poisoned')
        elif object == lesserShade and 'cursed' not in player.status:
            if object.curse():
                player.status.append('cursed')
                player.minDps = round((player.minDps / 100) * 50)
                player.maxDps = round((player.maxDps / 100) * 50)
        elif object == rat and 'diseased' not in player.status:
            if object.disease():
                player.status.append('diseased')
                player.maxHealth = round((player.maxHealth / 100) * 80)
                if player.currentHealth > player.maxHealth:
                    player.currentHealth = player.maxHealth
        elif object == darkKnight:
            if object.stun():
                player.status.append('stunned')

    @staticmethod
    def stateCheck(player): # add other statuses + state check for monsters
        if player.status:
            if 'poisoned' in player.status:
                n = random.randint(1, 5)
                print(f'{player.name} took {n} damage from poison!')
                player.currentHealth -= n
            if 'stunned' in player.status:
                player.status.remove('stunned')
                return False
            if 'regenerate' in player.status:
                if player.status[0][1] > 0:
                    player.currentHealth += regen.heal
                    print(f'{regeb.heal} hp regenerated!')
                    player.status[0][1] -= 1
                else:
                    player.status.remove(['regenerate', 0])
            return True
        else:
            return True

    @staticmethod
    def restore(player): # add other statuses
        if 'cursed' in player.status:
            player.minDps = round((player.minDps / 50) * 100)
            player.maxDps = round((player.maxDps / 50) * 100)
        if 'diseased' in player.status:
            player.maxHealth = round((player.maxHealth / 80) * 100)
        player.status = []
        player.currentAp = 0

    def battle(self, player, object, cx, cy):
        time.sleep(1)
        if self.stateCheck(player):
            att = player.attack(object)
            if att:
                player.appAdd(att)
        if isinstance(object, cr.Boss):
            if object.death(player):
                player.levelCheck()
                print('VICTORY ACHIEVED')
                time.sleep(1)
                self.restore(player)
                self.flag = False
                return True
        elif object.death(player):
            player.levelCheck()
            time.sleep(1)
            self.oLevel[cx][cy] = None
            self.restore(player)
            return True
        time.sleep(1)
        att = object.attack(player)
        self.special(object, player, att)
        if player.death():
            print('YOU DIED')
            self.flag = False
            return True
        time.sleep(1)

    def command(self, player):
        eq = re.compile(r'equip ((\w+\'?\s*)+)')
        uneq = re.compile(r'unequip ((\w+\'?\s*)+)')
        view = re.compile(r'view ((\w+\'?\s*)+)')
        drink = re.compile(r'drink ((\w+\'?\s*)+)')
        while True:
            try:
                a = input('\nWhat\'s your action? ').lower()
                if a == 'attack' or a == 'auto-attack' or a == 'auto':
                    return a
                if a == 'help':
                    help()
                elif a == 'char':
                    player.showChar()
                elif a == 'inv':
                    player.showInventory()
                elif 'unequip' in a:
                    mo = uneq.search(a)
                    itemName = mo.group(1)
                    item = player.itemSearch(player, itemName)
                    if item:
                        player.unequipItem(item)
                        print(f'{item.name} unequiped!')
                elif 'equip' in a:
                    mo = eq.search(a)
                    itemName = mo.group(1)
                    item = player.itemSearch(player, itemName)
                    if item:
                        player.equipItem(item)
                elif 'view' in a:
                    mo = view.search(a)
                    itemName = mo.group(1)
                    item = player.itemSearch(player, itemName)
                    if item:
                        item.itemView()
                elif 'drink' in a:
                    mo = drink.search(a)
                    itemName = mo.group(1)
                    potion = player.itemSearch(player, itemName)
                    player.drinkPotion(potion)
                elif a == 'map':
                    print('\n' + str(self.level) + '\n')
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
        player = cr.Player(name)
        intro2(name)
        gameRules()
        while self.flag:
            try:
                print('\n' + str(self.level) + '\n')
                ctrl = input('Which way would you like to go? ').lower()
                if ctrl in Game.ctrls:
                    d = Game.ctrls.index(ctrl)
                    self.prevPos = self.currPos[:]
                    self.currPos[d <= 2] += d - (1 if d < 3 else 4)
                    if self.movePlayer():
                        time.sleep(1)
                        self.action(player)
                    else:
                        self.currPos = self.prevPos[:]
                elif ctrl == Game.exit:
                    self.flag = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a proper direction.')


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
map                shows a map
attack             attack a monster
auto-attack        attack a monster until the fight ends
char               shows your statistics and equiped gear
inv                shows your inventory 
equip 'item'       equip an item
unequip 'item'     unequip an item
view 'item'        shows attributes of an item
drink 'potion'     drink a potion to regain health
quit               exit game       
""")


if __name__ == '__main__':
    game = Game()
    game.play()
