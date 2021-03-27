import time
import re
import creatures as cr
import items as it
import objects as ob


dagger = it.Dagger('Dagger', 'dagger', 'common', 3, 2, 3, 7, 0.2)
axe = it.SmallAxe('Axe', 'small axe', 'common', 5, 5, 5, 10, 0.1)
longsword = it.Longsword('Longsword', 'longsword', 'common', 5, 4, 7, 9, 0.05)
greatsword = it.Greatsword('Greatsword', 'greatsword', 'common', 8, 8, 11, 15,
                           0.1)
greataxe = it.Greataxe('Greataxe', 'greataxe', 'common', 9, 10, 10, 17, 0.1)
shadowStrike = it.Dagger('Shadow Strike', 'dagger', 'uncommon', 23, 2, 12, 16,
                         0.2)
peaceMaker = it.SmallAxe('Peace Maker', 'small axe', 'uncommon', 28, 6, 12, 20,
                         0.1)
oathKeeper = it.Longsword('Oath Keeper', 'longsword', 'uncommon', 26, 4, 15, 18,
                          0.05)
soulReaper = it.Greatsword('Soul Reaper', 'greatsword', 'uncommon', 35, 10, 35,
                           40, 0.1)
rapture = it.Greataxe('Rapture', 'greataxe', 'uncommon', 37, 11, 31, 44, 0.1)
sinisterCarver = it.Dagger('Sinister Carver', 'dagger', 'rare', 50, 2, 42, 50,
                           0.2)
harbinger = it.SmallAxe('Harbinger', 'small axe', 'rare', 56, 6, 45, 60, 0.1)
blindJustice = it.Longsword('Blind Justice', 'longsword', 'rare', 58, 4, 51, 55,
                            0.05)
stormbringer = it.Greatsword('Stormbringer', 'greatsword', 'rare', 72, 12, 72,
                             79, 0.1)
eclipse = it.Greataxe('Eclipse', 'greataxe', 'rare', 78, 12, 68, 85, 0.1)
smallShield = it.SmallShield('Small Shield', 'small shield', 'common', 4, 5, 5,
                             -0.1)
greatshield = it.Greatshield('Greatshield', 'greatshield', 'common', 6, 10, 11,
                             -0.2)
dawnGuard = it.SmallShield('Dawn Guard', 'small shield', 'uncommon', 13, 6, 13,
                           -0.1)
heroWarden = it.Greatshield('Hero Warden', 'greatshield', 'uncommon', 17, 12,
                            19, -0.2)
tranquility = it.SmallShield('Tranquility', 'small shield', 'rare', 28, 5, 22,
                             -0.1)
theSentry = it.Greatshield('The Sentry', 'greatshield', 'rare', 36, 13, 32,
                           -0.2)
leatherArmor = it.LightArmor('Leather Armor', 'light armor', 'common', 8, 10, 16,
                             -0.1)
plateArmor = it.HeavyArmor('Plate Armor', 'heavy armor', 'common', 13, 32, 35,
                           -0.2)
soulOfTheEast = it.LightArmor('Soul of the East', 'light armor', 'uncommon', 29,
                              11, 28, -0.1)
twilightIronArmor = it.HeavyArmor('Twilight Iron Armor', 'heavy armor',
                                  'uncommon', 34, 36, 62, -0.2)
favorOfPhantoms = it.LightArmor('Favor of Phantoms', 'light armor', 'rare', 62,
                                10, 42, -0.1)
cryOfTheBerserker = it.HeavyArmor('Cry of the Berserker', 'heavy armor', 'rare',
                                  68, 36, 88, -0.2)
jasperWhisper = it.Ring('Jasper Whisper', 'ring', 'uncommon', 12, evasion=0.1)
lunarShield = it.Ring('Lunar Shield', 'ring', 'uncommon', 11, armorValue=15)
jadeMoon = it.Ring('Jade Moon', 'ring', 'uncommon', 15, critChance=0.1)
emeraldFlame = it.Ring('Emerald Flame', 'ring', 'uncommon', 13, minDps=5,
                       maxDps=10)
lavishSpirit = it.Ring('Lavish Spirit', 'ring', 'rare', 25, evasion=0.2)
moltenCore = it.Ring('Molten Core', 'ring', 'rare', 22, armorValue=32)
forsakenPromise = it.Ring('Forsaken Promise', 'ring', 'rare', 26,
                          critChance=0.2)
ancientVigor = it.Ring('Ancient Vigor', 'ring', 'rare', 25, minDps=11,
                       maxDps=18)
smallHealthPotion = it.Potion('Small Health Potion', 'potion', 'common', 10, 20)
healthPotion = it.Potion('Health Potion', 'potion', 'common', 20, 40)

potions = [smallHealthPotion, healthPotion]


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

rat = cr.Monster('Rat', 20, 20, 1, 3, 0, 0.1, 0.2, potions, items)
vileBat = cr.Monster('Vile Bat', 15, 1, 2, 3, 0, 0.3, 0.2, potions, items)
zombie = cr.Monster('Zombie', 30, 30, 3, 5, 5, 0, 0.05, potions, items)
skeletonWarrior = cr.Monster('Skeleton Warrior', 25, 25, 3, 7, 20, 0.1, 0.1,
                             potions, items)
lesserShade = cr.Monster('Lesser Shade', 10, 10, 2, 6, 0, 0.5, 0.1, potions,
                         items)
giantSpider = cr.Monster('Giant Spider', 25, 25, 3, 8, 10, 0.1, 0.1, potions,
                         items)
darkKnight = cr.Boss('Dark Knight', 80, 80, 10, 15, 50, 0.05, 0.1, potions,
                     items, shield=True)
chest = ob.Chest()
shrine = ob.Shrine()

map = [[lesserShade, vileBat, None, chest], [rat, chest, zombie, vileBat],
       [chest, skeletonWarrior, shrine, chest], [rat, giantSpider, lesserShade,
                                                 darkKnight]]


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

    def battle(self, player, object, cx, cy):
        time.sleep(1)
        player.attack(object)
        if isinstance(object, cr.Boss):
            if object.death(items, potions, player):
                print('VICTORY ACHIEVED')
                self.flag = False
                return True
        elif object.death(items, potions, player):
            self.oLevel[cy][cx] = None
            return True
        time.sleep(1)
        object.attack(player)
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
            print('\n' + str(self.level) + '\n')
            ctrl = input('Which way would you like to go? ').lower()
            if ctrl in Game.ctrls:
                d = Game.ctrls.index(ctrl)
                self.prevPos = self.currPos[:]
                self.currPos[d > 2] += d - (1 if d < 3 else 4)
                self.movePlayer()
                self.action(player)
            elif ctrl == Game.exit:
                self.flag = False
            else:
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
    game = Game(map)
    game.play()

