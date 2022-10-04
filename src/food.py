import random
from const import *

class Food:
    
    def __init__(self):
        self.foodX = 310
        self.foodY = 310

    def spawn(self):
        self.foodX = random.randrange(10, WIDTH, SQSIZE)
        self.foodY = random.randrange(10, HEIGHT, SQSIZE)
        self.food_location = (self.foodX, self.foodY)