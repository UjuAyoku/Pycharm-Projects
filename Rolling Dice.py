import random


class Dice:
    def roll(self):
        first = random.randint(1, 7)
        second = random.randint(1, 7)
        return first, second  # auto creates a tuple


dice = Dice()
print(dice.roll())
