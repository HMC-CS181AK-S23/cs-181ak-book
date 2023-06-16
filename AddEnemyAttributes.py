from graphics import *
from random import *
from math import *

WIDTH = 800
HEIGHT = 600

CIRCLE_START_SIZE = 2
COLORS = [
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 0, 0), (0, 255, 0), (0, 0, 255)
]
MAX_V = 2


class Circle:

    SIZE = CIRCLE_START_SIZE

    def __init__(self):
        # random number
        rx = 4 * random()
        ry = (rx + 1) % 4
        # Position computation
        self.x = min(max(abs(2 - rx) - 0.5, 0), 1) * (WIDTH + 4 * Circle.SIZE) - 2 * Circle.SIZE
        self.y = min(max(abs(2 - ry) - 0.5, 0), 1) * (HEIGHT + 4 * Circle.SIZE) - 2 * Circle.SIZE
        
        self.dx = (2 * random() - 1) * MAX_V
        self.dy = (2 * random() - 1) * MAX_V
        self.size = Circle.SIZE
        self.color = COLORS[randint(0, len(COLORS) - 1)]
        self.active = True
        Circle.SIZE += 1
        
    
    def update(self):
        # Move the circles
        self.x = (self.x + self.dx + self.size * 2) % (WIDTH + self.size * 4) - self.size * 2
        self.y = (self.y + self.dy + self.size * 2) % (HEIGHT + self.size * 4) - self.size * 2

    def draw(self):
        fillCircle(self.x, self.y, self.size, self.color)



def start(world):

    setBackground('black')

    hideMouse()

    world.circles = [Circle() for _ in range(30)]



def update(world):
    for circle in world.circles:
        circle.update()



def draw(world):

    for circle in world.circles:

        circle.draw()



    (x, y) = getMousePosition()

    fillCircle(x, y, 10, 'white')



makeGraphicsWindow(WIDTH, HEIGHT, False)

runGraphics(start, update, draw)