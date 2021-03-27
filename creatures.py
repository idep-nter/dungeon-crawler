import random
import time
import items as it


class Creature:
    def __init__(self, name, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, potions=None, items=None,
                 shield=None):
        self.name = name
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.minDps = minDps
        self.maxDps = maxDps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance
        self.shield = shield

    def attack(self, target):
        attack = random.randint(self.minDps, self.maxDps)
        crit = False
        if random.random() < target.evasion:
            print(f'{self.name} missed the attack!')
            return False
        if random.random() < self.critChance:
            crit = True
            attack = (attack / 100) * 150
        if target.shield:
            attack = (attack / 100) * 70
        attack = round(attack / (1 + (target.armorValue / 100)))
        if crit:
            print(f'{target.name} was critically hit by {attack}!')
        else:
            print(f'{target.name} was hit by {attack}!')
        target.currentHealth -= attack

    def itemDrop(self, items, player):
        n = random.random()
        if n < 0.1:
            item = self.randomItem(items, 'rare')
        elif n < 0.3:
            item = self.randomItem(items, 'uncommon')
        else:
            item = self.randomItem(items, 'common')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def potionDrop(self, potions, player):
        n = random.random()
        if n < 0.3:
            potion = potions[1]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)
        elif n < 0.6:
            potion = potions[0]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def randomItem(self, items, rarity):
        iType = random.choice(list(items[rarity]))
        item = random.choice(list(items[rarity][iType]))
        return item


class Player(Creature):
    def __init__(self, name, maxHealth=100, currentHealth=100, minDps=1,
                 maxDps=4, armorValue=0, evasion=0.2, critChance=0.1,
                 maxWeight=100, currentWeight=0, gold=0, weapon=None,
                 armor=None, ring1=None, ring2=None, shield=None):
        super().__init__(name, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, shield)
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.inventory = []
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.ring1 = ring1
        self.ring2 = ring2
        self.shield = shield

    def showChar(self, player):
        attrs = vars(player)
        for key, value in attrs.items():
            if key == 'inventory' or key == 'gold':
                continue
            if isinstance(value, it.Item):
                print(f'{key:^15} : {value.name:^15}')
            else:
                value = it.strNone(value)
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
                self.inventory.append(item)
            elif item == self.shield:
                self.shield = None
                self.currentWeight -= item.weight
                self.armorValue -= item.armorValue
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
                self.inventory.append(item)
            elif item == self.ring2:
                self.ring2 = None
                self.maxHealth -= item.maxHealth
                self.minDps -= item.minDps
                self.maxDps -= item.maxDps
                self.armorValue -= item.armorValue
                self.evasion -= item.evasion
                self.critChance -= item.critChance
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


class Monster(Creature):
    def __init__(self, name, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, potions, items, shield=None):
        super().__init__(name, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, potions, items, shield)


    def goldDrop(self, player):
        gold = random.randint(5, 20)
        print(f'You have found {gold} gold!')
        player.gold += gold

    def death(self, items, potions, player):
        if self.currentHealth <= 0:
            print(f'{self.name} was slain!')
            time.sleep(1)
            self.itemDrop(items, player)
            time.sleep(1)
            self.goldDrop(player)
            time.sleep(1)
            self.potionDrop(potions, player)
            time.sleep(1)
            return True
        return False

class Boss(Creature):
    def __init__(self, name, maxHealth, currentHealth, minDps, maxDps,
                 armorValue, evasion, critChance, potions, items, shield=None):
        super().__init__(name, maxHealth, currentHealth, minDps, maxDps,
                         armorValue, evasion, critChance, potions, items,
                         shield)

    def death(self, items, potions, player):
        if self.currentHealth <= 0:
            time.sleep(1)
            self.itemDrop(items, player)
            time.sleep(1)
            self.goldDrop(player)
            time.sleep(1)
            self.potionDrop(potions, player)
            time.sleep(1)
            return True
        return False

    def itemDrop(self, items, player):
        item = self.randomItem(items, 'rare')
        print(f'You have found {item.name}!')
        player.inventory.append(item)
        n = random.random()
        if n < 0.3:
            item = self.randomItem(items, 'rare')
        elif n < 0.5:
            item = self.randomItem(items, 'uncommon')
        else:
            item = self.randomItem(items, 'common')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def goldDrop(self, player):
        gold = random.randint(50, 100)
        print(f'You have found {gold} gold!')
        player.gold += gold

    def potionDrop(self, potions, player):
        potion = potions[1]
        print(f'You have found {potion.name}!')
        player.inventory.append(potion)
        n = random.random()
        if n < 0.5:
            potion = potions[1]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)
        else:
            potion = potions[0]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)


