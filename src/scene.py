import pygame
from const import *
from food import Food
from snake import Snake

class Scene:

    def __init__(self):
        self.food = Food()
        self.snake = Snake()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    color = L_GREEN
                else:
                    color = D_GREEN

                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_snake(self, surface, last_key):
        snake = self.snake
        rect = snake.head(last_key)
        pygame.draw.rect(surface, BLUE, rect)

    def show_tail(self, surface):
        snake = self.snake
        for segment in range(snake.tail_count):
            rect = snake.tail(segment)
            pygame.draw.rect(surface, BLUE, rect)

    def show_food(self, surface):
        snake = self.snake
        food = self.food

        if snake.locationX == food.foodX-10:
            if snake.locationY == food.foodY-10:
                snake.tail_count += 1
                food.spawn()

        circ = (food.foodX, food.foodY)
        pygame.draw.circle(surface, RED, circ, SQSIZE//2)

    def isdead(self):
        snake = self.snake

        if snake.locationX in snake.prev_locX:
            n = snake.prev_locX.index(snake.locationX)
            if snake.locationY == snake.prev_locY[n]:
                pygame.quit()

    def isout(self):
        snake = self.snake

        if snake.locationX < 0 or snake.locationX >= WIDTH or snake.locationY < 0 or snake.locationY >= HEIGHT:
            pygame.quit()