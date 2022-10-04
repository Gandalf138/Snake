import pygame
import random
from const import *
from food import Food
from snake import Snake

class Scene:

    def __init__(self):
        self.food = Food()
        self.snake = Snake()
        self.food_start()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    color = L_GREEN
                else:
                    color = D_GREEN

                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_food(self, surface):
        snake = self.snake
        food = self.food

        if snake == food.food_location:
            food.spawn()

        circ = (food.food_location)
        pygame.draw.circle(surface, RED, circ, SQSIZE//2)

    def food_start():
        food.spawn()