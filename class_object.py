import math

class circle:

    def __init__(self, x, y, speed_x, speed_y, radius):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
    
    def get_radius_by_dist(self, x1, y1):
        dist = math.sqrt((x1 - self.x) ** 2 + (y1 - self.y) ** 2)
        if(dist == 0):
            return 1
        else:
            return self.radius / math.sqrt((x1 - self.x) ** 2 + (y1 - self.y) ** 2)