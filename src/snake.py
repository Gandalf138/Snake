from const import *
from vector import Vector, ZERO, RIGHT, LEFT, UP, DOWN


class Snake:

    def __init__(self):
        self.tail_count = 2
        self.locationX = 100
        self.locationY = 100
        self.prev_locX = [80, 60]
        self.prev_locY = [80, 60]
        # now snake's direction is abstracted - it doesn't need to know anything about your input system
        self.direction = DOWN

    def change_direction(self, new_direction):
        merged_direction = new_direction + self.direction
        if merged_direction == ZERO:
            return
        self.direction = new_direction

    def head(self):
        
        if self.direction == ZERO:
            pass
        elif self.direction == RIGHT:
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationX += SQSIZE
        elif self.direction == LEFT:
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationX -= SQSIZE
        elif self.direction == UP:
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationY -= SQSIZE
        elif self.direction == DOWN:
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationY += SQSIZE

        if len(self.prev_locX) > self.tail_count:
            del self.prev_locX[0]
            del self.prev_locY[0]

        return (self.locationX, self.locationY, SQSIZE, SQSIZE)

    def tail(self, segment):

        return (self.prev_locX[segment],self.prev_locY[segment], SQSIZE, SQSIZE)
