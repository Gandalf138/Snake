import pygame

from snake import *

class Death:

    def __init__(self):
        self.snake = Snake()

    def bite(self):
        snake = self.snake

        if snake.locationX in snake.prev_locX:
            n = snake.prev_locX.index(snake.locationX)
            if snake.locationY == snake.prev_locationY[n]:
                pass