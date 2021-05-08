import random
import time


class Shrine:
    def __init__(self):
        pass

    def heal(self, player):
        player.currentHealth = player.maxHealth


class Chest:
    def __init__(self, potions, items):
        self.potions = potions
        self.items = items

    def open(self, player):
        self.itemFind(player)
        time.sleep(1)
        self.potionFind(player)
        time.sleep(1)
        self.goldFind(player)
        time.sleep(1)
        self.trap(player)

    @staticmethod
    def goldFind(player):
        rng = [20, 50]
        gold = random.randint(rng[0], rng[1])
        print(f'You have found {gold} gold!')
        player.gold += gold

    def itemFind(self, player):
        item = None
        n = random.random()
        if n < 0.1:
            item = self.randomItem('epic')
        if n < 0.2:
            item = self.randomItem('rare')
        elif n < 0.5:
            item = self.randomItem('uncommon')
        elif n < 0.8:
            item = self.randomItem('common')
        if item:
            print(f'You have found {item.name}!')
            player.inventory.append(item)

    def randomItem(self, rarity):
        iType = random.choice(list(self.items[rarity]))
        item = random.choice(list(self.items[rarity][iType]))
        return item

    def potionFind(self, player):
        n = random.random()
        if n < 0.5:
            potion = random.choice(self.potions)
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    @staticmethod
    def trap(player):
        if random.random() < 0.2:
            dmg = random.randint(10, 20)
            player.currentHealth -= dmg
            print(f'There was a trap! You have been hit by {dmg}!')