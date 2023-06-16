from graphics import *
from random import *
from math import *

WIDTH = 800
HEIGHT = 600

START_SIZE = 10

CIRCLE_START_SIZE = 2
COLORS = [
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 0, 0), (0, 255, 0), (0, 0, 255)
]
MAX_V = 2
MAX_ACTIVE = 30


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
        
    
    # Now returns whether the player is alive.
    def update(self, x, y, r):
        # Move the circle
        self.x = (self.x + self.dx + self.size * 2) % (WIDTH + self.size * 4) - self.size * 2
        self.y = (self.y + self.dy + self.size * 2) % (HEIGHT + self.size * 4) - self.size * 2

        # See if the distance between the centers is less than the sum of the radii
        if (self.x - x)**2 + (self.y - y)**2 <= (r + self.size)**2:
            # Circle is active if its radius is smaller than player radius.
            if self.size < r:
                self.active = False
            if self.size > r:
                return False
        return True

    def draw(self):
        fillCircle(self.x, self.y, self.size, self.color)



def start(world):
    setBackground('black')
    hideMouse()
    # Change initial value here
    world.circles = []
    world.size = START_SIZE
    world.alive = True
    
def update(world):
    # Adds the appropriate number of circles.
    for _ in range(MAX_ACTIVE - len(world.circles)):
        world.circles.append(Circle())
    (x, y) = getMousePosition()
    for circle in world.circles:
        # Update world.alive
        world.alive = circle.update(x, y, world.size) and world.alive
        if world.alive and not circle.active:
            # Update world.size
            world.size += 1
    
    # Now, circles should only be removed if the player is alive
    if world.alive:
        world.circles = [circle for circle in world.circles if circle.active]

def draw(world):
    for circle in world.circles:
        circle.draw()

    (x, y) = getMousePosition()
    # Replace the circle size with the world.size
    fillCircle(x, y, world.size, 'white')



makeGraphicsWindow(WIDTH, HEIGHT, False)

runGraphics(start, update, draw)