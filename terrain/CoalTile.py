import random

from terrain.Tile import Tile

MIN_COAL_DEPOSIT = 100
MAX_COAL_AMOUNT_DEVIATION = 20


class CoalTile(Tile):

    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.coal_amount = (
            MIN_COAL_DEPOSIT + self.getCoalAmounDeviation()
        )  # <-- Amount of coal available on the tile.
        self.coal_exhausted = False

    def isCoalExhausted(self):
        return self.coal_exhausted

    def getCoalAmounDeviation(self):
        return random.randint(-MAX_COAL_AMOUNT_DEVIATION, MAX_COAL_AMOUNT_DEVIATION)

    def digCoal(self, amount):
        """
        Dig some coal amount from the deposit if available.
        Return True - if some coal was digged, else False if no more deposits.
        """
        if self.coal_amount > amount:
            self.coal_amount -= amount
            return True
        else:
            self.coal_exhausted = True
            return False
        
            
