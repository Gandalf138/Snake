from event import Event
import pygame

from vector import Vector, DOWN, UP, LEFT, RIGHT

# Think how you could make multiple controllers
class ArrowInput:
    def __init__(self):
        self.on_change_direction = Event()

    def update(self, key):
        if key == pygame.K_RIGHT:
            self.on_change_direction(RIGHT)
        elif key == pygame.K_LEFT:
            self.on_change_direction(LEFT)
        elif key == pygame.K_UP:
            self.on_change_direction(UP)
        elif key == pygame.K_DOWN:
            self.on_change_direction(DOWN)

# I'm showing off here
class WASDInput:
    def __init__(self):
        self.on_change_direction = Event()

    def update(self, key):
        if key == pygame.K_d:
            self.on_change_direction(RIGHT)
        elif key == pygame.K_a:
            self.on_change_direction(LEFT)
        elif key == pygame.K_w:
            self.on_change_direction(UP)
        elif key == pygame.K_s:
            self.on_change_direction(DOWN)

