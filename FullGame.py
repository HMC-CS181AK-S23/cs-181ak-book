from graphics import *
from random import *
from math import *

WIDTH = 800
HEIGHT = 600

START_SIZE = 10
CIRCLE_START_SIZE = 2
MAX_ACTIVE = 30
MAX_V = 2

COLORS = [
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 0, 0), (0, 255, 0), (0, 0, 255)
]

class Circle:
    
    SIZE = CIRCLE_START_SIZE
    
    def __init__(self):
        rx = 4 * random()
        ry = (rx + 1) % 4
        self.x = min(max(abs(2 - rx) - 0.5, 0), 1) * (WIDTH + 4 * Circle.SIZE) - 2 * Circle.SIZE
        self.y = min(max(abs(2 - ry) - 0.5, 0), 1) * (HEIGHT + 4 * Circle.SIZE) - 2 * Circle.SIZE
        self.dx = (2 * random() - 1) * MAX_V
        self.dy = (2 * random() - 1) * MAX_V
        self.size = Circle.SIZE
        self.color = COLORS[randint(0, len(COLORS) - 1)]
        self.active = True
        Circle.SIZE += 1
    
    def update(self, x, y, r):
        self.x = (self.x + self.dx + self.size * 2) % (WIDTH + self.size * 4) - self.size * 2
        self.y = (self.y + self.dy + self.size * 2) % (HEIGHT + self.size * 4) - self.size * 2
        if (self.x - x)**2 + (self.y - y)**2 <= (r + self.size)**2:
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
    world.circles = []
    world.size = START_SIZE
    world.alive = True

def update(world):
    for _ in range(MAX_ACTIVE - len(world.circles)):
        world.circles.append(Circle())
    
    (x, y) = getMousePosition()
    for circle in world.circles:
        world.alive = circle.update(x, y, world.size) and world.alive
        if world.alive and not circle.active:
            world.size += 1
    
    if world.alive:
        world.circles = [circle for circle in world.circles if circle.active]
    else:
        if isKeyPressed("space"):
            world.circles = []
            world.size = START_SIZE
            world.alive = True
            Circle.SIZE = CIRCLE_START_SIZE

def draw(world):
    for circle in world.circles:
        circle.draw()
    
    if world.alive:
        (x, y) = getMousePosition()
        fillCircle(x, y, world.size, 'white')
    else:
        (text1, size1) = ("Game Over!", 60)
        ss = sizeString(text1, size1)
        drawString(text1, WIDTH/2 - ss[0]/2, HEIGHT/2 - ss[1] - 10, size1, 'white')
        
        (text2, size2) = (f"Score: {(world.size - START_SIZE)}", 40)
        ss = sizeString(text2, size2)
        drawString(text2, WIDTH/2 - ss[0]/2, HEIGHT/2 + 10, size2, 'white')

makeGraphicsWindow(WIDTH, HEIGHT, False)
runGraphics(start, update, draw)