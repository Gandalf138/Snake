import pygame
import sys

from const import *
from scene import Scene
from food import Food

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption('Snake')
        self.scene = Scene()
        self.food = Food()

    def mainloop(self):
        scene = self.scene
        screen = self.screen
        food = self.food

        while True:
            scene.show_bg(screen)
            scene.show_food(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    food.spawn()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            pygame.display.update()

main = Main()
main.mainloop()

