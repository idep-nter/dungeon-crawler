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
        if random.random() < self.critChance:
            attack = (attack / 100) * 150
        target.health -= attack

class Player(Creature):
    def __init__(self, maxHealth=100, currentHealth=100, dps=[0, 0], 
        armorValue=0, evasion=0,critChance=0.01, maxWeight=100, currentWeight=0, 
        weapon=None, armor=None, ring=None):
        super().__init__(name, dps, armorValue, evasion, critChance)
        self.maxHealth = maxHealth 
        self.currentHealth = currentHealth
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.inventory = []
        self.weapon = weapon
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
            self.weapon = item
        elif item == Armor:
            self.armor = item
        elif item == Ring:
            self.ring = item

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

class Armor(Item):
    def __init__(self, value, weight, armorValue, evasion):
        super().__init__(value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

class Ring(Item):
    def __init__(self, value, weight=0.1, maxHealth=None, dps=None, 
        armorValue=None, evasion=None, critChance=None):
        super().__init__(value, weight)
        self.maxHealth = maxHealth
        self.dps = dps
        self.armorValue = armorValue
        self.evasion = evasion
        self.critChance = critChance

class Potion(Item):
    def __init__(self, value, health)
    super().__init__(value, weight)
    self.health = health