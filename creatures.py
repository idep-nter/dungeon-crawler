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
        attack = random.randint(self.minDps, self.maxDps)
        crit = False
        if random.random() < target.evasion:
            print(f'{self.name} missed the attack!')
            return False
        if random.random() < self.critChance:
            crit = True
            attack = attack * self.critMulti
        if random.random() < target.blockChance:
            print(f'{target.name} blocked the attack!')
            return False
        attack = round(attack / (1 + (target.armorValue / 100)))
        if crit:
            print(f'{target.name} was critically hit by {attack}!')
        else:
            print(f'{target.name} was hit by {attack}!')
        target.currentHealth -= attack
        return attack

    def creatureType(self):
        if isinstance(self, Boss):
            tMode = 2
        else:
            tMode = 1
        return tMode

    def goldDrop(self, player):
        tMode = self.creatureType()
        baseGold = [5, 10]
        goldDict = {}
        for l in range(1, 11):
            gMin = baseGold[0] * l * tMode
            gMax = baseGold[1] * l * tMode
            goldDict.setdefault(l, [gMin, gMax])
        rng = goldDict[self.lvl]
        gold = random.randint(rng[0], rng[1])
        print(f'You have found {gold} gold!')
        player.gold += gold

    def itemDrop(self, player):
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
        tMode = self.creatureType()
        iMod = self.lvl * 0.05
        n = random.random()
        if n < 0.3 + iMod * tMode:
            potion = random.choice(self.potions)
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def randomItem(self, rarity):
        iType = random.choice(list(self.items[rarity]))
        item = random.choice(list(self.items[rarity][iType]))
        return item

    def regenerate(self):
        n = random.random()
        if n < 0.3:
            hp = random.randint(1, 5)
            print(f'{self.name} regenerated {hp} health!')
            self.currentHealth += hp

    def stealLife(self, attack):
        n = random.random()
        if n < 0.3:
            hp = attack
            print(f'{self.name} stole {hp} health from you!')
            self.currentHealth += hp

    def stun(self):
        n = random.random()
        if n < 0.3:
            print('You have been stunned!')
            return True
        return False

    def poison(self):
        n = random.random()
        if n < 0.2:
            print('You have been poisoned!')
            return True
        return False

    def curse(self):
        n = random.random()
        if n < 0.5:
            print('You have been cursed!')
            return True
        return False

    def disease(self):
        n = random.random()
        if n < 0.2:
            print('You got a disease!')
            return True
        return False


class Player(Creature):
    def __init__(self, name, lvl=1, exp=0, maxHealth=100, currentHealth=100,
                 minDps=1, maxDps=2, armorValue=0, evasion=0.2, critChance=0.1,
                 critMulti=1.5, blockChance=0, maxWeight=100, currentWeight=0,
                 gold=0, weapon=None, armor=None, ring1=None, ring2=None,
                 shield=None):
        super().__init__(name, lvl, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, critMulti,
                         blockChance)
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
        self.status = []

    def showChar(self):
        exp = f'{self.exp}/{int(self.lvl * 1000 * 1.5)}'
        health = f'{self.currentHealth}/{self.maxHealth}'
        dps = f'{self.minDps}-{self.maxDps}'
        weight = f'{self.currentWeight}/{self.maxWeight}'
        evasion = f'{int(self.evasion * 100)} %'
        critChance = f'{int(self.critChance * 100)} %'
        critMulti = f'x{self.critMulti}'
        blockChance = f'{int(self.blockChance * 100)} %'
        attrs = {'Name': self.name, 'Level': self.lvl, 'Experience': exp,
                 'Health': health, 'Weight': weight, 'DPS': dps, 'Armor Value':
                 self.armorValue, 'Block Chance': blockChance,
                 'Evasion': evasion, 'Crit Chance': critChance,
                 'Crit Multiplier': critMulti, 'Weapon': self.weapon,
                 'Armor': self.armor, 'Ring 1': self.ring1,
                 'Ring 2': self.ring2, 'Status':self.status,
                 'Perks': self.perks}
        for key, value in attrs.items():
            if key == 'Perks' or key == 'Status':
                value = strNone(value)
                if value == '-':
                    print(f'{key:^15} : {value:^15}')
                else:
                    print(f'{key:^15} : {value}') #check
            elif isinstance(value, it.Item):
                print(f'{key:^15} : {value.name:^15}')
            else:
                value = strNone(value)
                print(f'{key:^15} : {value:^15}')

    def showInventory(self):
        print(f'{self.gold} gold')
        for item in self.inventory:
            print(f'{item.name}')

    def equipItem(self, item):
        try:
            if not isinstance(item, it.Ring):
                if not self.weightCheck(item):
                    print('You weight too much!')
                    raise ValueError
            if isinstance(item, it.Weapon):
                if not self.handCheck(item):
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
                if not self.handCheck(item):
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
        elif isinstance(potion, it.Regen):
            self.status.insert(0, ['regenerate', 5])
        elif isinstance(potion, it.Antidote):
            potion.curePoison(self)
            print('Poison was cured!')

    def death(self):
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
        return False if self.currentWeight + item.weight > self.maxWeight else \
            True

    def levelCheck(self):
        lvls = {2 : 1000}
        for i in range(3, 21):
            num = 1000 * i * 1.5
            lvls.setdefault(i, num)
        for k, v in lvls.items():
            if self.exp >= v and self.lvl < k:
                self.levelUp(lvls)
        return False

    def levelUp(self):
        self.lvl += 1
        print('LEVEL UP!')
        self.maxHealth += 20
        print('Max health +20!')
        self.exp -= lvls[self.lvl]
        if self.lvl % 4 == 0:
            self.choosePerk()

    def choosePerk(self):
        perks = {'Ninja': '+0.1 evasion', 'Berserk': '+0.1 crit chance',
                 'Bud Spencer': '+50 max health', 'Defendor': '+30 armor'}
        for key, value in perks.items():
            print(f'{key:^15} : {value:^15}')
        while True:
            try:
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
                    raise ValueError
            except ValueError:
                print('Please type the right perk from the list.')


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
        self.status = []

    def death(self, player):
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
        self.status = []

    def death(self, player):
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
            time.sleep(1)
            player.exp += self.expValue
            print(f'You have gained {self.expValue} exp!')
            return True
        return False


def strNone(value):
    if not value:
        return '-'
    return value


