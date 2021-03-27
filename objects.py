import random


class Shrine:
    def __init__(self):
        pass

    def heal(self, player):
        player.currentHealth = player.maxHealth


class Chest:
    def __init__(self):
        pass

    def open(self, items, potions, player):
        self.itemFind(items, player)
        self.potionFind(potions, player)
        self.trap(player)

    def itemFind(self, items, player):
        n = random.random()
        if n < 0.3:
            item = self.randomItem(items, 'rare')
        elif n < 0.5:
            item = self.randomItem(items, 'uncommon')
        else:
            item = self.randomItem(items, 'common')
        print(f'You have found {item.name}!')
        player.inventory.append(item)

    def randomItem(self, items, rarity):
        iType = random.choice(list(items[rarity]))
        item = random.choice(list(items[rarity][iType]))
        return item

    def potionFind(self, potions, player):
        n = random.random()
        if n < 0.5:
            potion = potions[1]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)
        else:
            potion = potions[0]
            print(f'You have found {potion.name}!')
            player.inventory.append(potion)

    def trap(self, player):
        if random.random() < 0.1:
            dmg = random.randint(10, 30)
            player.currentHealth -= dmg
            print(f'There was a trap! You have been hit by {dmg}!')