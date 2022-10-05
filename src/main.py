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
                    if event.key == pygame.K_RIGHT and last_key != 'L':
                        last_key = 'R'
                    elif event.key == pygame.K_LEFT and last_key != 'R':
                        last_key = 'L'
                    elif event.key == pygame.K_UP and last_key != 'D':
                        last_key = 'U'
                    elif event.key == pygame.K_DOWN and last_key != 'U':
                        last_key = 'D'
                  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            scene.isdead()
            scene.isout()

            pygame.time.Clock().tick(15)           
            pygame.display.update()

main = Main()
main.mainloop()

