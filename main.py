import time
import re
import creatures as cr
import items as it
import objects as ob
import random

dagger = it.Dagger('Dagger', 'dagger', 'common', 3, 2, 2, 4, 0.2)
axe = it.SmallAxe('Axe', 'small axe', 'common', 5, 5, 3, 6, 0.1)
longsword = it.Longsword('Longsword', 'longsword', 'common', 5, 4, 4, 7, 0.05)
greatsword = it.Greatsword('Greatsword', 'greatsword', 'common', 8, 8, 6, 10,
                           0.1)
greataxe = it.Greataxe('Greataxe', 'greataxe', 'common', 9, 10, 5, 11, 0.15)
swiftDagger = it.Dagger('Swift Dagger', 'dagger', 'uncommon', 7, 2, 3, 7, 0.2)
battleAxe = it.SmallAxe('Battle Axe', 'small axe', 'uncommon', 8, 5, 4, 9, 0.1)
noblemansSword = it.Longsword('Nobleman\'s sword', 'longsword', 'uncommon', 8,
                              4, 6, 11, 0.05)
balancedGreatSword = it.Greatsword('Balanced Greatsword', 'greatsword',
                                   'uncommon', 13, 8, 9, 15, 0.1)
chieftainsGreataxe = it.Greataxe('Chieftain\'s Greataxe', 'greataxe',
                                 'uncommon', 12, 10, 8, 14, 0.15)
shadowStrike = it.Dagger('Shadow Strike', 'dagger', 'rare', 23, 2, 8, 14,
                         0.2)
peaceMaker = it.SmallAxe('Peace Maker', 'small axe', 'rare', 28, 6, 11, 17,
                         0.1)
oathKeeper = it.Longsword('Oath Keeper', 'longsword', 'rare', 26, 4, 13, 18,
                          0.05)
soulReaper = it.Greatsword('Soul Reaper', 'greatsword', 'rare', 35, 10, 20,
                           28, 0.1)
rapture = it.Greataxe('Rapture', 'greataxe', 'rare', 37, 11, 18, 27, 0.15)
sinisterCarver = it.Dagger('Sinister Carver', 'dagger', 'epic', 50, 2, 17, 25,
                           0.2)
harbinger = it.SmallAxe('Harbinger', 'small axe', 'epic', 56, 6, 23, 30, 0.1)
blindJustice = it.Longsword('Blind Justice', 'longsword', 'epic', 58, 4, 26, 32,
                            0.05)
stormbringer = it.Greatsword('Stormbringer', 'greatsword', 'epic', 72, 12, 39,
                             45, 0.1)
eclipse = it.Greataxe('Eclipse', 'greataxe', 'epic', 78, 12, 36, 44, 0.15)
smallShield = it.SmallShield('Small Shield', 'small shield', 'common', 4, 5, 5,
                             -0.1)
greatshield = it.Greatshield('Greatshield', 'greatshield', 'common', 6, 10, 11,
                             -0.2)
compactShied = it.SmallShield('Compact Shield', 'small shield', 'uncommon', 8,
                              5, 8, -0.1)
sturdyGreatshield = it.SmallShield('Sturdy Greatshield', 'greatshield',
                                   'uncommon', 10, 5, 15, -0.2)
dawnGuard = it.SmallShield('Dawn Guard', 'small shield', 'rare', 16, 6, 16,
                           -0.1)
heroWarden = it.Greatshield('Hero Warden', 'greatshield', 'rare', 19, 12,
                            27, -0.2)
tranquility = it.SmallShield('Tranquility', 'small shield', 'epic', 35, 5, 27,
                             -0.1)
theSentry = it.Greatshield('The Sentry', 'greatshield', 'epic', 40, 13, 38,
                           -0.2)
leatherArmor = it.LightArmor('Leather Armor', 'light armor', 'common', 8, 10,
                             16, -0.1)
plateArmor = it.HeavyArmor('Plate Armor', 'heavy armor', 'common', 13, 32, 35,
                           -0.2)
scoutsLeatherArmor = it.LightArmor('Scout\'s Leather Armor', 'light armor',
                                   'uncommon', 8, 10, 25, -0.1)
knightsPlateArmor = it.HeavyArmor('Knight\'s Plate Armor', 'heavy armor',
                                  'uncommon', 13, 32, 41, -0.2)
soulOfTheEast = it.LightArmor('Soul of the East', 'light armor', 'rare', 38,
                              11, 28, -0.1)
twilightIronArmor = it.HeavyArmor('Twilight Iron Armor', 'heavy armor',
                                  'rare', 34, 36, 55, -0.2)
favorOfPhantoms = it.LightArmor('Favor of Phantoms', 'light armor', 'epic', 62,
                                10, 48, -0.1)
cryOfTheBerserker = it.HeavyArmor('Cry of the Berserker', 'heavy armor', 'epic',
                                  68, 36, 88, -0.2)
silverRing = it.Ring('Silver Ring', 'ring', 'common', 3)
goldRing = it.Ring('Gold Ring', 'ring', 'uncommon', 6)
jasperWhisper = it.Ring('Jasper Whisper', 'ring', 'rare', 12, evasion=0.1)
lunarShield = it.Ring('Lunar Shield', 'ring', 'rare', 11, armorValue=15)
jadeMoon = it.Ring('Jade Moon', 'ring', 'rare', 15, critChance=0.1)
emeraldFlame = it.Ring('Emerald Flame', 'ring', 'rare', 13, minDps=5,
                       maxDps=10)
lavishSpirit = it.Ring('Lavish Spirit', 'ring', 'epic', 25, evasion=0.2)
moltenCore = it.Ring('Molten Core', 'ring', 'epic', 22, armorValue=32)
forsakenPromise = it.Ring('Forsaken Promise', 'ring', 'epic', 26,
                          critChance=0.2)
ancientVigor = it.Ring('Ancient Vigor', 'ring', 'epic', 25, minDps=11,
                       maxDps=18)
smallHealthPotion = it.HealthPotion('Small Health Potion', 'potion', 'common',
                                    10, 20)
healthPotion = it.HealthPotion('Health Potion', 'potion', 'common', 20, 40)
regen = it.RegenPotion('Regeneration Potion', 'potion', 'common', 15, 5)
antidote = it.Antidote('Antidote', 'potion', 'common', 10)

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
                  'ring': [jasperWhisper, lunarShield, jadeMoon, emeraldFlame]},
         'epic': {'weapon': [sinisterCarver, harbinger, blindJustice,
                             stormbringer, eclipse],
                  'armor': [favorOfPhantoms, cryOfTheBerserker],
                  'shield': [tranquility, theSentry],
                  'ring': [lavishSpirit, moltenCore, forsakenPromise,
                           ancientVigor]}
         }

rat = cr.Monster('Rat', 20, 20, 1, 3, 0, 0.1, 0.2, 1, potions, items,
                 expValue=random.randint(300, 500))
vileBat = cr.Monster('Vile Bat', 15, 1, 2, 3, 0, 0.3, 0.2, 1, potions, items,
                     expValue=random.randint(300, 500))
zombie = cr.Monster('Zombie', 30, 30, 3, 5, 5, 0, 0.05, 2, potions, items,
                    expValue=random.randint(400, 700))
skeletonWarrior = cr.Monster('Skeleton Warrior', 25, 25, 3, 7, 20, 0.1, 0.1, 2,
                             potions, items, shield=True,
                             expValue=random.randint(400, 700))
lesserShade = cr.Monster('Lesser Shade', 10, 10, 2, 6, 0, 0.5, 0.1, 1, potions,
                         items, expValue=random.randint(300, 500))
giantSpider = cr.Monster('Giant Spider', 25, 25, 3, 8, 10, 0.1, 0.1, 2, potions,
                         items, expValue=random.randint(400, 700))
darkKnight = cr.Boss('Dark Knight', 80, 80, 10, 15, 50, 0.05, 0.1, 4, potions,
                     items, shield=True, expValue=random.randint(1500, 2000))
chest = ob.Chest()
shrine = ob.Shrine()


mapObjects = [rat, vileBat, zombie, skeletonWarrior, lesserShade, giantSpider,
              chest, shrine, None, None, None, None]


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
            if (-1 < cx < 4) and (-1 < cy < 4):
                if self.bossCheck():
                    self.level[py][px] = Game.markerO #check coords
                    self.level[cy][cx] = Game.markerX
                    return True
                else:
                    return False
            else:
                raise ValueError
        except ValueError:
            print('You can\'t go in there.')
            return False

    def bossCheck(self):
        cx, cy = self.currPos
        object = self.oLevel[cy][cx]  #check coords
        if isinstance(object, cr.Boss):
            while True:
                try:
                    q = input('You feel that something terribly dangerous '
                              'dwells in this room, do you really want to '
                              'continue?')
                    if q.lower == 'yes' or q.lower == 'y':
                        return True
                    elif q.lower == 'no' or q.lower == 'n':
                        return False
                    else:
                        raise ValueError
                except ValueError:
                    print('Please answer \'yes\' or \'no\'.')
        return True

    def action(self, player):
        cx, cy = self.currPos
        object = self.oLevel[cy][cx]
        if isinstance(object, ob.Shrine):
            print('You see some kind of shrine before you and suddenly feel '
                  'strength coming back to your body.')
            object.heal(player)
            self.oLevel[cy][cx] = None
        elif isinstance(object, ob.Chest):
            print('You see a wooden chest before you. What treasures does it '
                  'hold? You shiver with excitement as you opening it...')
            object.open(items, potions, player)
            self.oLevel[cy][cx] = None
        elif isinstance(object, cr.Monster):
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
        elif isinstance(object, cr.Boss):
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

    @staticmethod
    def special(object, player, attack):
        if object == zombie:
            object.regenerate()
        elif object == vileBat:
            object.stealLife(attack)
        elif object == giantSpider and 'poisoned' not in player.states:
            if object.poison():
                player.states.append('poisoned')
        elif object == shade and 'cursed' not in player.states:
            if object.curse():
                player.states.append('cursed')
                player.minDps = round((player.minDps / 100) * 50)
                player.maxDps = round((player.maxDps / 100) * 50)
        elif object == rat and 'diseased' not in player.states:
            if object.disease():
                player.states.append('diseased')
                player.maxHealth = round((player.maxHealth / 100) * 80)
                if player.currentHealth > player.maxHealth:
                    player.currentHealth = player.maxHealth
        elif object == darkKnight:
            if object.stun():
                player.states.append('stunned')

    @staticmethod
    def stateCheck(player):
        if player.states:
            if 'poisoned' in player.states:
                n = random.randint(1, 5)
                print(f'{player.name} took {n} damage from poison!')
                player.currentHealth -= n
            if 'stunned' in player.states:
                player.states.remove('stunned')
                return False
            if 'regenerate' in player.states:
                if player.states[0][1] > 0:
                    player.currentHealth += regen.heal
                    print(f'{regeb.heal} hp regenerated!')
                    player.states[0][1] -= 1
                else:
                    player.states.remove(['regenerate', 0])
            return True
        else:
            return True

    @staticmethod
    def restore(player):
        if 'cursed' in player.states:
            player.minDps = round((player.minDps / 50) * 100)
            player.maxDps = round((player.maxDps / 50) * 100)
        if 'diseased' in player.states:
            player.maxHealth = round((player.maxHealth / 80) * 100)
        player.states = []

    def battle(self, player, object, cx, cy):
        time.sleep(1)
        if stateCheck(player):
            player.attack(object)
        if isinstance(object, cr.Boss):
            if object.death(items, potions, player):
                player.levelCheck()
                print('VICTORY ACHIEVED')
                restore(player)
                self.flag = False
                return True
        elif object.death(items, potions, player):
            player.levelCheck()
            self.oLevel[cy][cx] = None
            restore(player)
            return True
        time.sleep(1)
        att = object.attack(player)
        special(object, player, att)
        if player.death():
            print('YOU DIED')
            self.flag = False
            return True
        time.sleep(1)

    def command(self, player):
        eq = re.compile(r'equip ((\w+\s*)+)')
        uneq = re.compile(r'unequip ((\w+\s*)+)')
        view = re.compile(r'view ((\w+\s*)+)')
        drink = re.compile(r'drink ((\w+\s*)+)')
        while True:
            try:
                a = input('\nWhat\'s your action? ').lower()
                if a == 'attack' or a == 'auto-attack':
                    return a
                if a == 'help':
                    help()
                elif a == 'char':
                    player.showChar(player)
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
                    self.currPos[d > 2] += d - (1 if d < 3 else 4)
                    if self.movePlayer():
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
equip >item<       equip an item
unequip >item<     unequip an item
view >item<        shows attributes of an item
drink              drink a potion to regain health
quit               exit game       
""")


if __name__ == '__main__':
    game = Game()
    game.play()

