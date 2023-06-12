from random import randint

class Dice:
    """Representation of a dice."""

    def __init__(self, sides=6) -> None:
        """Initialized a dice with default attribute value."""
        self.sided = sides
    
    def roll_dice(self, number):
        """Method that rolls the dice number of times."""

        for x in range(0,number):
            print(f"Roll number {x} out of {number}")
            roll = randint(1,number)
            print(f"You have rolled {roll}\n")


# my_basic_dice = Dice()
# my_basic_dice.roll_dice(10)

my_bigger_dice = Dice(10)
my_bigger_dice.roll_dice(10)

# my_biggest_dice = Dice(20)
# my_biggest_dice.roll_dice(20)
