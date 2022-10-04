from const import *

class Snake:
    
    def __init__(self):
        self.tail_count = 2
        self.locationX = 100
        self.locationY = 100
        self.prev_locX = [80,60]
        self.prev_locY = [80,60]

    def head(self, last_key):
        
        if last_key == None:
            pass
        elif last_key == 'R':
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationX += SQSIZE
        elif last_key == 'L':
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationX -= SQSIZE
        elif last_key == 'U':
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationY -= SQSIZE
        elif last_key == 'D':
            self.prev_locX.append(self.locationX)
            self.prev_locY.append(self.locationY)
            self.locationY += SQSIZE

        if len(self.prev_locX) > self.tail_count:
            del self.prev_locX[0]
            del self.prev_locY[0]

        return (self.locationX, self.locationY, SQSIZE, SQSIZE)

    def tail(self, segment):

        return (self.prev_locX[segment],self.prev_locY[segment], SQSIZE, SQSIZE)
