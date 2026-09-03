import random

class Dice:
    def __init__(self, sides):
        self.sides = sides  # number of sides on the die

    def roll(self):
        return random.randint(1, self.sides)  # random value from 1 to sides

# dice = Dice(6)              # create a 6-sided die (commented out)
# for roll in range(10):      # roll it 10 times (commented out)
#     print(dice.roll())

dice2 = Dice(20)          # create a 20-sided die
for roll in range(10):    # roll it 10 times
    print(dice2.roll())