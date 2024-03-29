import random
import time
import items as it


class Creature:
    def __init__(self, name, lvl, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, critMulti, blockChance):
        self.name = name
        self.lvl = lvl
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.minDps = minDps
        self.maxDps = maxDps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance
        self.critMulti = critMulti
        self.blockChance = blockChance

    def attack(self, target):
        """
        The base attack of a creature tries to pass target's evasion and
        block chance.
        Then it tries to modify attack by a crit chance.
        At the end the the attack number is reduced by target's armor value.
        """
        attack = random.randint(self.minDps, self.maxDps)
        crit = False
        if random.random() < target.evasion:
            print(f'{self.name} missed the attack!')
            return False, False
        if random.random() < target.blockChance:
            print(f'{target.name} blocked the attack!')
            return False, False
        if random.random() < self.critChance:
            crit = True
            attack = attack * self.critMulti
        attack = round(attack / (1 + (target.armorValue / 100)))
        return attack, crit

    def creatureType(self):
        """
        Returns a number depending on the creature type.
        """
        if isinstance(self, Boss):
            tMode = 2
        else:
            tMode = 1
        return tMode

    def goldDrop(self, player):
        """
        Calculates a gold range depending on creature's level and type and then
        adds a random number of gold to the player in a given range.
        """
        tMode = self.creatureType()
        baseGold = [5, 10]
        goldDict = {}
        for lvl in range(1, 11):
            gMin = baseGold[0] * lvl * tMode
            gMax = baseGold[1] * lvl * tMode
            goldDict.setdefault(lvl, [gMin, gMax])
        rng = goldDict[self.lvl]
        gold = random.randint(rng[0], rng[1])
        print(f'You have found {gold} gold!')
        player.gold += gold

    def itemDrop(self, player):
        """
        Adds an item to the player's inventory which quality depends on a
        random number. This random number is modified by creature's level and
        type.
        """
        item = None
        tMode = self.creatureType()
        iMod = self.lvl * 0.03
        n = random.random()
        if n < 0.05 + iMod * tMode:
            item = self.randomItem('epic')
        if n < 0.1 + iMod * tMode:
            item = self.randomItem('rare')
        elif n < 0.2 + iMod * tMode:
            item = self.randomItem('uncommon')
        elif n < 0.5 + iMod * tMode:
            item = self.randomItem('common')
        if item:
            print(f'You have found {item.name}!')
            player.inventory.append(item)

    def potionDrop(self, player):
        """
        Adds a potion to the player's inventory if it passes the random number
        test.
        This random number is modified by creature's level and type.
        """
        tMode = self.creatureType()
        iMod = self.lvl * 0.05
        n = random.random()
        if n < 0.3 + iMod * tMode:
            potion = random.choice(self.potions)
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def randomItem(self, rarity):
        """
        Returns a random item from given rarity.
        """
        iType = random.choice(list(self.items[rarity]))
        item = random.choice(list(self.items[rarity][iType]))
        return item

    def regenerate(self):
        """
        Enemy special ability.
        Regenerates creature's health in a given range if it passes the
        condition.
        """
        n = random.random()
        if n < 0.3:
            hp = random.randint(1, 5)
            print(f'{self.name} regenerated {hp} hp!')
            self.currentHealth += hp
            if self.currentHealth > self.maxHealth:
                self.currentHealth = self.maxHealth

    def stealLife(self, player):
        """
        Enemy special ability.
        Instead of a basic attack it tries to heal itself by the given damage if
        it passes all conditions.
        It is doesn't pass first random number condition, basic attack is used
        instead.
        """
        n = random.random()
        if n < 0.3:
            attack = random.randint(self.minDps, self.maxDps)
            if random.random() < player.evasion:
                print(f'{self.name} missed the attack!')
                return True
            if random.random() < player.blockChance:
                print(f'{player.name} blocked the attack!')
                return True
            if random.random() < self.critChance:
                attack = attack * self.critMulti
            attack = round(attack / (1 + (player.armorValue / 100)))
            steal = attack
            self.currentHealth += steal
            if self.currentHealth > self.maxHealth:
                steal = (self.currentHealth - self.maxHealth) - steal
                self.currentHealth = self.maxHealth
            print(f'{self.name} stole {steal} health from you!')
            player.currentHealth -= attack
        else:
            return False

    @staticmethod
    def stun(player):
        """
        Enemy special ability.
        The player gets a stunned effect if it passes the test.
        """
        n = random.random()
        if n < 0.2:
            player.status['stunned']['duration'] = \
                player.status.setdefault('stunned',
                                         {}).setdefault('duration',
                                                        0) + 2
            print('You have been stunned!')

    @staticmethod
    def poison(player):
        """
        Enemy special ability.
        The player gets a poisoned effect if it passes the test.
        """
        n = random.random()
        if n < 0.2:
            player.status['poisoned']['duration'] = \
                player.status.setdefault('poisoned',
                                         {}).setdefault('duration', 0) + 3
            print('You have been poisoned!')

    @staticmethod
    def curse(player):
        """
        Enemy special ability.
        The player gets a cursed effect if it passes the test.
        """
        n = random.random()
        if n < 0.2:
            player.status.setdefault('cursed',
                                     {}).setdefault('active', False)
            player.status.setdefault('cursed',
                                     {}).setdefault('duration', '~')
            print('You have been cursed!')

    @staticmethod
    def disease(player):
        """
        Enemy special ability.
        The player gets a diseased effect if it passes the test.
        """
        n = random.random()
        if n < 0.2:
            player.status.setdefault('diseased',
                                     {}).setdefault('active', False)
            player.status.setdefault('diseased',
                                     {}).setdefault('duration', '~')
            print('You have been diseased!')

    def fortify(self):
        """
        Enemy special ability.
        An enemy gets a fortify effect if it passes the test.
        """
        self.status.setdefault('fortified',
                                     {}).setdefault('active', False)
        self.status['fortified']['duration'] = \
            self.status.setdefault('fortified', {}).setdefault('duration', 0) \
            + 4
        print(f'{self.name} has been fortified!')


class Player(Creature):
    def __init__(self, name, lvl=1, exp=0, maxHealth=100, currentHealth=100,
                 currentAp=0, maxAp=10, minDps=0, maxDps=0, armorValue=0,
                 evasion=0.2, critChance=0.1, critMulti=1.5, blockChance=0,
                 maxWeight=100, currentWeight=0, gold=0, weapon=None,
                 armor=None, ring1=None, ring2=None, shield=None):
        super().__init__(name, lvl, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, critMulti,
                         blockChance)
        self.currentAp = currentAp
        self.maxAp = maxAp
        self.exp = exp
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.ring1 = ring1
        self.ring2 = ring2
        self.shield = shield
        self.inventory = []
        self.perks = []
        self.status = {}

    def showChar(self):
        """
        First it makes a dictionary of player's attributes from which it
        prints player's stats in formatted way.
        """
        exp = f'{self.exp}/{int(self.lvl * 1000 * 1.5)}'
        health = f'{self.currentHealth}/{self.maxHealth}'
        ap = f'{self.currentAp}/{self.maxAp}'
        dps = f'{self.minDps}-{self.maxDps}'
        weight = f'{self.currentWeight}/{self.maxWeight}'
        evasion = f'{int(self.evasion * 100)} %'
        critChance = f'{int(self.critChance * 100)} %'
        critMulti = f'x{self.critMulti}'
        blockChance = f'{int(self.blockChance * 100)} %'
        attrs = {'Name': self.name, 'Level': self.lvl, 'Experience': exp,
                 'Health': health, 'Action Points': ap, 'Weight': weight, 'DPS':
                     dps, 'Armor Value': self.armorValue, 'Block Chance':
                     blockChance, 'Evasion': evasion, 'Crit Chance': critChance,
                 'Crit Multiplier': critMulti, 'Weapon': self.weapon,
                 'Shield': self.shield, 'Armor': self.armor,
                 'Ring 1': self.ring1, 'Ring 2': self.ring2,
                 'Status': self.status, 'Perks': self.perks}
        for key, value in attrs.items():
            if key == 'Status':
                value = strNone(value)
                if value == '-':
                    print(f'{key:^15} : {value:^25}')
                else:
                    n = 1
                    for k in self.status.keys():
                        value = self.status[k]['duration']
                        v = f"{k.capitalize()} : {value} rounds"
                        if n:
                            print(f'{key:^25} : {v:^25}')
                            n -= 1
                        else:
                            x = " " * 17
                            print(f'{x} {v:^25}')
            elif key == 'Perks':
                value = strNone(value)
                if value == '-':
                    print(f'{key:^25} : {value:^25}')
                else:
                    print(f'{key:^25} : {value}')
            elif isinstance(value, it.Item):
                print(f'{key:^25} : {value.name:^25}')
            else:
                value = strNone(value)
                print(f'{key:^25} : {value:^25}')

    def showInventory(self):
        """
        First it makes a dictionary from player's inventory list from which
        prints items in formatted way.
        """
        invDict = {}
        for item in self.inventory:
            invDict[item.name] = invDict.setdefault(item.name, 0) + 1

        print(f'{self.gold} gold')
        for item, num in invDict.items():
            if num > 1:
                print(f'{item} [{num}]')
            else:
                print(f'{item}')

    def equipItem(self, item):
        """
        If it passes conditions it adds an item to the right slot and unequips
        previous item if any. It also modify player's stats by the item.
        """
        try:
            if not isinstance(item, it.Ring):
                if not self.weightCheck(item):  # checks player's total weight
                    print('You weight too much!')
                    raise ValueError
            if isinstance(item, it.Weapon):
                if not self.handCheck(item): # checks if player has free hand(s)
                    print('Cannot equip!')
                    raise ValueError
                if self.weapon:
                    pWeapon = self.weapon
                    self.unequipItem(pWeapon)
                self.weapon = item
                self.currentWeight += item.weight
                self.minDps += item.minDps
                self.maxDps += item.maxDps
                self.critChance += item.critChance
                self.critMulti += item.critMulti
                self.inventory.remove(item)
                print(f'{item.name} equiped!')
            elif isinstance(item, it.Shield):
                if not self.handCheck(item):  # hand check for shield
                    print(f'Cannot equip!')
                    raise ValueError
                if self.shield:
                    pShield = self.shield
                    self.unequipItem(pShield)
                self.shield = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.blockChance += item.blockChance
                self.inventory.remove(item)
                print(f'{item.name} equiped!')
            elif isinstance(item, it.Armor):
                if self.armor:
                    pArmor = self.armor
                    self.unequipItem(pArmor)
                self.armor = item
                self.currentWeight += item.weight
                self.armorValue += item.armorValue
                self.evasion += item.evasion
                self.inventory.remove(item)
                print(f'{item.name} equiped!')
            elif isinstance(item, it.Ring):
                if self.ring1 and not self.ring2: # equips ring in a proper slot
                    self.ring2 = item
                elif not self.ring1 and self.ring2:
                    self.ring1 = item
                elif self.ring1 and self.ring2:
                    pRing = self.ring1
                    self.unequipItem(pRing)
                    self.ring1 = item
                else:
                    self.ring1 = item
                if item.maxHealth:
                    self.maxHealth += item.maxHealth
                if item.minDps:
                    self.minDps += item.minDps
                    self.maxDps += item.maxDps
                if item.armorValue:
                    self.armorValue += item.armorValue
                if item.evasion:
                    self.evasion += item.evasion
                if item.critChance:
                    self.critChance += item.critChance
                if item.critMulti:
                    self.critMulti += item.critMulti
                self.inventory.remove(item)
                print(f'{item.name} equiped!')
        except ValueError:
            return False

    def unequipItem(self, item):
        """
        Unequips given item and modify player's stats.
        """
        if item == self.weapon:
            self.weapon = None
            self.currentWeight -= item.weight
            self.minDps -= item.minDps
            self.maxDps -= item.maxDps
            self.critChance -= item.critChance
            self.critMulti -= item.critMulti
            self.inventory.append(item)
        elif item == self.shield:
            self.shield = None
            self.currentWeight -= item.weight
            self.armorValue -= item.armorValue
            self.blockChance -= item.blockChance
            self.inventory.append(item)
        elif item == self.armor:
            self.armor = None
            self.currentWeight -= item.weight
            self.armorValue -= item.armorValue
            self.evasion -= item.evasion
            self.inventory.append(item)
        elif item == self.ring1:
            self.ring1 = None
            self.maxHealth -= item.maxHealth
            self.minDps -= item.minDps
            self.maxDps -= item.maxDps
            self.armorValue -= item.armorValue
            self.evasion -= item.evasion
            self.critChance -= item.critChance
            self.critMulti -= item.critMulti
            self.inventory.append(item)
        elif item == self.ring2:
            self.ring2 = None
            self.maxHealth -= item.maxHealth
            self.minDps -= item.minDps
            self.maxDps -= item.maxDps
            self.armorValue -= item.armorValue
            self.evasion -= item.evasion
            self.critChance -= item.critChance
            self.critMulti -= item.critMulti
            self.inventory.append(item)
        else:
            print('Wrong item!')

    def itemSearch(self, player, itemName):
        """
        Returns searched instance of an item from player's inventory if it's
        there.
        """
        attrs = vars(player)
        for item in self.inventory:
            if itemName.lower() == item.name.lower():
                return item
        for value in attrs.values():
            if isinstance(value, it.Item):
                if itemName.lower() == value.name.lower():
                    return value
        print(f'{itemName} not in the inventory!')

    def drinkPotion(self, potion):
        """
        Uses a potion if it's in player's inventory and does it's effect.
        """
        if isinstance(potion, it.HealthPotion):
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
        elif isinstance(potion, it.RegenPotion):
            potion.regen(self)
        elif isinstance(potion, it.Antidote):
            potion.curePoison(self)
            print('Poison was cured!')

    def death(self):
        """
        Checks creature's health points and returns True if they're 0 or below.
        """
        return True if self.currentHealth <= 0 else False

    def handCheck(self, item):
        if isinstance(item, it.Greataxe) or \
                isinstance(item, it.Greatsword) and self.shield:
            return False
        if isinstance(item, it.Shield) and \
                isinstance(self.weapon, it.Greataxe) or \
                isinstance(self.weapon, it.Greatsword):
            return False
        return True

    def weightCheck(self, item):
        """
        Checks player's weight limit and returns false if he carries too much.
        """
        return False if self.currentWeight + item.weight > self.maxWeight else \
            True

    def levelCheck(self):
        """
        Creates a dictionary of levels and exp and checks if the player has
        enough exp point to level up.
        """
        lvls = {2: 1000}
        for i in range(3, 21):
            num = 1000 * i * 1.5
            lvls.setdefault(i, num)
        for k, v in lvls.items():
            if self.exp >= v and self.lvl < k:
                self.levelUp(lvls)
        return False

    def levelUp(self, lvls):
        """
        Increments player's level by one, adds health points and subtract exp
        points needed for the current level.
        Also checks condition for adding AP point and a new perk.
        """
        self.lvl += 1
        print('LEVEL UP!')
        self.maxHealth += 20
        print('Max health +20!')
        self.exp -= lvls[self.lvl]
        if self.lvl % 3 == 0:
            self.addMaxAp()
        if self.lvl % 4 == 0:
            self.choosePerk()

    def addMaxAp(self):
        """Adds up 1 APP point."""
        self.maxAp += 1
        print('+1 max action point!')

    def choosePerk(self):
        """
        Prints perks to be chosen from and inputs the player to choose one.
        """
        perks = {'Ninja': '+0.1 evasion', 'Berserk': '+0.1 crit chance',
                 'Bud Spencer': '+50 max health', 'Defendor': '+30 armor'}
        for key, value in perks.items():
            print(f'{key:^25} : {value:^25}')
        while True:
            choice = input('Choose your new Perk!')
            if choice.lower() == 'ninja':
                self.perks.append('Ninja')
                self.evasion += 0.1
                return True
            elif choice.lower() == 'berserk':
                self.perks.append('Berserk')
                self.critChance += 0.1
                return True
            elif choice.lower() == 'bud spencer':
                self.perks.append('Bud Spencer')
                self.maxHealth += 50
                return True
            elif choice.lower() == 'defendor':
                self.perks.append('Defendor')
                self.armorValue += 30
                return True
            else:
                print('Please type the right perk from the list.')

    def appAdd(self, attack):
        """
        Gets an attack value from the argument and returns a number of AP points
        from a list.
        """
        ap = 0
        apList = [1, 10, 20, 40, 80, 160]
        for i in apList:
            if attack >= i:
                ap += 1
        self.currentAp += ap
        if self.currentAp > self.maxAp:
            self.currentAp = self.maxAp


class Monster(Creature):
    def __init__(self, name, lvl, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, critMulti, blockChance,
                 expValue, potions, items):
        super().__init__(name,  lvl, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, critMulti,
                         blockChance)
        self.potions = potions
        self.items = items
        self.expValue = expValue
        self.status = {}

    def death(self, player):
        """
        Checks monster's health points and if it passes the condition it uses
        drop functions.
        It also adds up exp points to the player and resets monster's health
        for the next encounter.
        """
        if self.currentHealth <= 0:
            print(f'{self.name} was slain!')
            time.sleep(1)
            self.itemDrop(player)
            time.sleep(1)
            self.goldDrop(player)
            time.sleep(1)
            self.potionDrop(player)
            time.sleep(1)
            player.exp += self.expValue
            print(f'You have gained {self.expValue} exp!')
            self.currentHealth = self.maxHealth
            return True
        return False


class Boss(Creature):
    def __init__(self, name, lvl, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, critMulti, blockChance, expValue,
                 potions, items):
        super().__init__(name, lvl, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, critMulti,
                         blockChance)
        self.potions = potions
        self.items = items
        self.expValue = expValue
        self.status = {}

    def death(self, player):
        """
        Same as monster's death function just with more item drop functions.
        """
        if self.currentHealth <= 0:
            print(f'{self.name} was slain!')
            time.sleep(1)
            self.itemDrop(player)
            self.itemDrop(player)
            self.itemDrop(player)
            time.sleep(1)
            self.goldDrop(player)
            time.sleep(1)
            self.potionDrop(player)
            self.potionDrop(player)
            self.potionDrop(player)
            time.sleep(1)
            player.exp += self.expValue
            print(f'You have gained {self.expValue} exp!')
            return True
        return False


def strNone(value):
    """
    Helps to format text by returning '-' if the value is none or an empty
    list.
    """
    if value == None or value == []:
        return '-'
    return value
