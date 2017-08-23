from random import randrange


class Dice():
    """class for simulation dice throws"""
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return self.sides[randrange(0, len(self.sides))]

    def roll_plus(self):
        rolled_number = self.roll
        total_rolled = rolled_number
        while rolled_number == self.sides[len(self.sides) - 1]:
            rolled_number = self.roll
            total_rolled += rolled_number
        return total_rolled
