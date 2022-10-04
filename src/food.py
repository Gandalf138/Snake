import random
from const import *

class Food:
    
    def __init__(self):
        self.food_location = None

    def spawn(self):
        self.foodX = random.randrange(0, WIDTH, SQSIZE)
        self.foodY = random.randrange(0, HEIGHT, SQSIZE)
        self.food_location = (foodX, foodY)