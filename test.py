import random

target = 'xxxx'
player = 'misa'


def heroicStrike(player):

    def inner(func):

        def wrapper(*args):
            print(player)
            att = random.randint(1, 10) / 100 * 150
            return func(att, *args)
        return wrapper
    return inner

@heroicStrike(player)
def attack(att):
    print(att)

attack()