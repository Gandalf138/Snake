import pygame
import sys

from const import *
from scene import Scene

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption('Snake')
        self.scene = Scene()
        self.last_key = 'R'

    def mainloop(self):
        scene = self.scene
        screen = self.screen
        last_key = self.last_key

        while True:
            scene.show_bg(screen)
            scene.show_food(screen)
            scene.show_snake(screen, last_key)
            scene.show_tail(screen)

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        last_key = 'R'
                    elif event.key == pygame.K_LEFT:
                        last_key = 'L'
                    elif event.key == pygame.K_UP:
                        last_key = 'U'
                    elif event.key == pygame.K_DOWN:
                        last_key = 'D'
                  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            pygame.time.Clock().tick(10)           
            pygame.display.update()

main = Main()
main.mainloop()

