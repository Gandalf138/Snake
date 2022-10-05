import pygame
import sys

from const import *
from scene import Scene
from input_controller import ArrowInput, WASDInput


class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption('Snake')
        self.scene = Scene()
        self.input_manager = ArrowInput()

        # you could uncomment this and it would override the above controller
        # self.input_manager = WASDInput()

        # this is an event listener pattern - check this out here:
        # https://www.educba.com/python-event-handler/
        self.input_manager.on_change_direction += self.scene.get_player_snake().change_direction

    def mainloop(self):
        scene = self.scene
        screen = self.screen

        while True:
            scene.show_bg(screen)
            scene.show_food(screen)
            scene.show_snake(screen)
            scene.show_tail(screen)

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    self.input_manager.update(event.key)
                  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            scene.isdead()
            scene.isout()

            pygame.time.Clock().tick(15)           
            pygame.display.update()

main = Main()
main.mainloop()

