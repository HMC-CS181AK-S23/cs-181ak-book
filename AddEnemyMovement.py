from graphics import *
from random import *
from math import *

WIDTH = 800
HEIGHT = 600

class Circle:
    
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
        # Initialize velocity here!
        self.dx = (2 * random() - 1) * 2
        self.dy = (2 * random() - 1) * 2
        self.size = 2
        self.color = 'blue'
    
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