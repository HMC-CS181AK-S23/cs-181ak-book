from graphics import *
from random import *
from math import *

WIDTH = 800
HEIGHT = 600

def start(world):
    setBackground('black')  # This sets the background to black
    hideMouse()             # This hides the mouse

def update(world):
    pass

def draw(world):
    (x, y) = getMousePosition()
    fillCircle(x, y, 10, 'white')

makeGraphicsWindow(WIDTH, HEIGHT, False)
runGraphics(start, update, draw)