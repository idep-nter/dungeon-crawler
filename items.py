class Item:
    def __init__(self, name, type, rarity, value, weight=None):
        self.name = name
        self.type = type
        self.rarity = rarity
        self.value = value
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, weight)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance
        self.critMulti = critMulti

    def itemView(self):
        """
        Prints weapon's stats in formatted way.
        """
        dps = self.maxDps - self.minDps
        critChance = f'{int(self.critChance * 100)} %'
        critMulti = f'x{self.critMulti}'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'DPS': dps, 'Crit Chance': critChance,
                 'Crit Multiplier': critMulti, 'Weight': self.weight,
                 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')


class Longsword(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, critMulti, weight)

    @staticmethod
    def heroicStrike(game, player, enemy):
        """
        Modifies player's attack by 150 %.
        """
        att, crit = player.attack(enemy)
        if att:
            att = round(att / 100 * 150)
            game.makeAttack(att, crit, enemy)

    @staticmethod
    def pommelAttack(game, player, enemy):
        """
        If target doesn't evade or block, player attacks target by 70% damage
        and stun it for a round.
        """
        att, crit = player.attack(enemy)
        if att:
            att = round(att / 100 * 70)
            print(f'{enemy.name} is stunned!')
            enemy.status['stunned']['duration'] = \
                enemy.status.setdefault('stunned',
                                         {}).setdefault('duration', 0) + 1
            game.makeAttack(att, crit, enemy)


class Greatsword(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, critMulti, weight)

    @staticmethod
    def execute(game, player, enemy):
        """
        The target instantly dies if it's under 30 % health or else player's
        attack is reduced to 70 %.
        """
        att, crit = player.attack(enemy)
        if att:
            health = enemy.currentHealth / (enemy.maxHealth / 100)
            if health < 30:
                enemy.currentHealth = 0
            else:
                att = round(att / 100 * 70)
                game.makeAttack(att, crit, enemy)

    @staticmethod
    def skullsplitter(game, player, enemy):
        """
        Modifies player's attack by 30 % for each available action point.
        """
        att, crit = player.attack(enemy)
        if att:
            aMod = 0
            for i in range(player.currentAp):
                aMod += 0.3
            att *= aMod
            game.makeAttack(att, crit, enemy)


class Dagger(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, critMulti, weight)

    @staticmethod
    def poisonStrike(player, enemy):
        """
        If target doesn't evade or block, it gets poisoned.
        """
        att, crit = player.attack(enemy)
        if att:
            print(f'{enemy.name} is poisoned!')
            enemy.status['poisoned']['duration'] = \
                enemy.status.setdefault('poisoned',
                                         {}).setdefault('duration', 0) + 3


    @staticmethod
    def sinisterStrike(game, player, enemy):
        """
        Modifies player's attack by 175 %.
        """
        att, crit = player.attack(enemy)
        if att:
            att = round(att / 100 * 150)
            game.makeAttack(att, crit, enemy)


class SmallAxe(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, critMulti, weight)

    @staticmethod
    def deepWounds(player, enemy):
        """
        If target doesn't evade or block, it gets bleeding effect.
        """
        att, crit = player.attack(enemy)
        if att:
            print(f'{enemy.name} is wounded!')
            enemy.status['wounded']['duration'] = \
                enemy.status.setdefault('wounded',
                                         {}).setdefault('duration', 0) + 3


    @staticmethod
    def armorCrush(player, enemy):
        """
        If target doesn't evade or block, it gets crushed effect.
        """
        att, crit = player.attack(enemy)
        if att:
            print(f'{enemy.name}\'s armor is crushed!')

            player.status.setdefault('crushed',
                                     {}).setdefault('active', False)
            player.status['crushed']['duration'] = \
                player.status.setdefault('crushed',
                                         {}).setdefault('duration', 0) + 4


class Greataxe(Weapon):
    def __init__(self, name, type, rarity, value, minDps, maxDps,
                 critChance, critMulti, weight):
        super().__init__(name, type, rarity, value, minDps, maxDps,
                         critChance, critMulti, weight)

    @staticmethod
    def bloodthirst(player):
        """
        The player gets bloodthirst effect.
        """
        print(f'{player.name} got crazy by blood!')
        player.status.setdefault('bloodthirst',
                                 {}).setdefault('active', False)
        player.status['bloodthirst']['duration'] = \
            player.status.setdefault('bloodthirst',
                                     {}).setdefault('duration', 0) + 3


    @staticmethod
    def rampage(game, player, enemy):
        """
        The player attacks 2 times.
        """
        for i in range(2):
            att, crit = player.attack(enemy)
            game.makeAttack(att, crit, enemy)


class Shield(Item):
    def __init__(self, name, type, rarity, value, armorValue, evasion,
                 blockChance, weight):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion
        self.blockChance = blockChance

    def itemView(self):
        """
        Print's shield's stats in formatted way.
        """
        evasion = f'{int(self.evasion * 100)} %'
        blockChance = f'{int(self.blockChance * 100)} %'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Block Chance': blockChance,
                 'Armor Value': self.armorValue, 'Evasion': evasion,
                 'Weight': self.weight, 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')

    @staticmethod
    def shieldBash(player, enemy):
        """
        If target doesn't evade or block, it gets stunned for 2 rounds.
        """
        att, crit = player.attack(enemy)
        if att:
            print(f'{enemy.name} is stunned!')
            enemy.status['stunned']['duration'] = \
                enemy.status.setdefault('stunned',
                                         {}).setdefault('duration', 0) + 2


    @staticmethod
    def shieldWall(player):
        """
        The player gets fortified effect.
        """
        print(f'{player.name} is now fortified!!')
        player.status.setdefault('fortified',
                                 {}).setdefault('active', False)
        player.status['fortified']['duration'] = \
            player.status.setdefault('fortified',
                                     {}).setdefault('duration', 0) + 4


class Greatshield(Shield):
    def __init__(self, name, type, rarity, value, armorValue, evasion,
                 blockChance, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion,
                         blockChance, weight)


class SmallShield(Shield):
    def __init__(self, name, type, rarity, value, armorValue, evasion,
                 blockChance, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion,
                         blockChance, weight)


class Armor(Item):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, weight)
        self.armorValue = armorValue
        self.evasion = evasion

    def itemView(self):
        """
        Prints armor's stats in formatted way.
        """
        evasion = f'{int(self.evasion * 100)} %'
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Armor Value': self.armorValue, 'Evasion': evasion,
                 'Weight': self.weight, 'Value': self.value}
        for key, value in attrs.items():
            print(f'{key:^15} : {value:^15}')


class LightArmor(Armor):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class HeavyArmor(Armor):
    def __init__(self, name, type, rarity, value, armorValue, evasion, weight):
        super().__init__(name, type, rarity, value, armorValue, evasion, weight)


class Ring(Item):
    def __init__(self, name, type, rarity, value, minDps=None, maxDps=None,
                 armorValue=None, evasion=None, critChance=None, critMulti=None,
                 maxHealth=None):
        super().__init__(name, type, rarity, value)
        self.minDps = minDps
        self.maxDps = maxDps
        self.critChance = critChance
        self.critMulti = critMulti
        self.armorValue = armorValue
        self.evasion = evasion
        self.maxHealth = maxHealth

    def itemView(self):
        """
        Prints ring's stats depending on which it has in formatted way.
        """
        if self.maxDps:
            dps = self.maxDps - self.minDps
        else:
            dps = None
        if self.evasion:
            evasion = f'{int(self.evasion * 100)} %'
        else:
            evasion = None
        if self.critChance:
            critChance = f'{int(self.critChance * 100)} %'
        else:
            critChance = None
        if self.critMulti:
            critMulti = f'x{self.critMulti}'
        else:
            critMulti = None
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Health': self.maxHealth, 'DPS': dps, 'Armor Value':
                     self.armorValue, 'Evasion': evasion,
                 'Crit Chance': critChance, 'Crit Multiplier': critMulti,
                 'Value': self.value}
        for key, value in attrs.items():
            if not value:
                continue
            else:
                print(f'{key:^15} : {value:^15}')


class Potion(Item):
    def __init__(self, name, type, rarity, value, heal=None):
        super().__init__(name, type, rarity, value, heal)
        self.heal = heal

    def itemView(self):
        """
        Prints potion's stats in formatted way.
        """
        attrs = {'Name': self.name, 'Type': self.type, 'Rarity': self.rarity,
                 'Heal': self.heal, 'Value': self.value}
        for key, value in attrs.items():
            if not value:
                continue
            else:
                print(f'{key:^15} : {value:^15}')


class HealthPotion(Potion):
    def __init__(self, name, type, rarity, value, heal):
        super().__init__(name, type, rarity, value, heal)


class Antidote(Potion):
    def __init__(self, name, type, rarity, value):
        super().__init__(name, type, rarity, value)

    @staticmethod
    def curePoison(player):
        """
        Removes player's poison effect.
        """
        del player.status['poisoned']


class RegenPotion(Potion):
    def __init__(self, name, type, rarity, value):
        super().__init__(name, type, rarity, value)

    @staticmethod
    def regen(player):
        """
        Adds regeneration status to the player.
        """
        player.status.setdefault('regeneration',
                                 {}).setdefault('duration',
                                                5) + 5