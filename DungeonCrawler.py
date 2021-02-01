import random

class Creature:
    def __init__(self, name, health, dps, armorValue, evasion, critChance):
        self.health = health
        self.dps = dps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance

    def attack(self, target): 
        attack = random.choice(range(self.dps[0], self.dps[1]+1))
        if random.random() < self.evasion:
            attack = 0
        elif random.random() < self.critChance:
            attack = (attack / 100) * 150
            if target.shield:
                attack = (attack / 100) * 70
        elif target.shield:
            attack = (attack / 100) * 70
        target.health -= attack

class Player(Creature):
    def __init__(self, maxHealth=100, currentHealth=100, dps=[0, 0], 
        armorValue=0, evasion=0,critChance=0.01, maxWeight=100, currentWeight=0, 
        weapon=None, shield=None, armor=None, ring=None):
        super().__init__(name, dps, armorValue, evasion, critChance)
        self.maxHealth = maxHealth 
        self.currentHealth = currentHealth
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.inventory = []
        self.weapon = weapon
        self.shield = shield
        self.armor = armor
        self.ring = ring

    def showChar(self):
        attrs = vars(Player)
        for key, value in attrs.items():
            print(f'{key} = {value}')

    def showInventory(self):
        print(i for i in self.inventory)

    def equipItem(self, item):
        if item == Weapon:
            if self.weapon:
                unEquipItem(self, item)
            self.weapon = item
            self.weight += item.weight
            self.dps += item.dps
            self.critChance += item.critChance
        elif item == Shield:
            if self.shield:
                unEquipItem(self, item)
            self.shield = item
            self.weight += item.weight
            self.armorValue += item.armorValue
        elif item == Armor:
            if self.armor:
                unEquipItem(self, item)
            self.armor = item
            self.weight += item.weight
            self.armorValue += item.armorValue
            self.evasion += item.evasion
        elif item == Ring:
            if self.ring:
                unEquipItem(self, item)
            self.ring = item
            self.maxHealth += item.maxHealth
            self.dps += item.dps
            self.armorValue += item.armorValue
            self.evasion += item.evasion
            self.critChance += item.critChance

    def unEquipItem(self, item):
        if item == Weapon:
            self.weapon = None
            self.weight -= item.weight
            self.dps -= item.dps
            self.critChance -= item.critChance
        elif item == Shield:
            self.shield = None
            self.weight -= item.weight
            self.armorValue -= item.armorValue
        elif item == Armor:
            self.armor = None
            self.weight -= item.weight
            self.armorValue -= item.armorValue
            self.evasion -= item.evasion
        elif item == Ring:
            self.ring = None
            self.maxHealth -= item.maxHealth
            self.dps -= item.dps
            self.armorValue -= item.armorValue
            self.evasion -= item.evasion
            self.critChance -= item.critChance

    def drinkPotion(self, potion):
        self.health += potion.health
        if self.health > maxHealth:
            health = maxHealth

class Monster(Creature):
    def __init__(self, name, health, dps, armorValue, evasion, critChance, 
        decription):
        super().__init__(name, health, dps, armorValue, evasion, critChance)
        self.inventory = []
        self.decription = decription

    def itemDrop(self):
        item = random.choice(self.inventory)
        Player.inventory.append(item)

    def __str__():
        return self.decription

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Weapon(Item):
    def __init__(self, value, weight, dps, critChance):
        super().__init__(value, weight)
        self.dps = dps
        self.critChance = critChance

class Shield(Item):
    def __init__(self, value, weight, armorValue):
        super().__init__(value, weight)
        self.armorValue = armorValue

class Armor(Item):
    def __init__(self, value, weight, armorValue, evasion):
        super().__init__(value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

class Ring(Item):
    def __init__(self, value, maxHealth=None, dps=None, 
        armorValue=None, evasion=None, critChance=None):
        super().__init__(value, weight)
        self.maxHealth = maxHealth
        self.dps = dps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance

class Potion(Item):
    def __init__(self, value, health):
        super().__init__(value, weight)
        self.health = health
