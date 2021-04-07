import math
from simanim import *

scena_w, scena_h = 2.56, 4
ruza_w, ruza_h = 0.25, 0.4


def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(5)
    UpdatesPerFrame(1)

    m.x = InputFloat(1, (0, scena_w))
    m.y = InputFloat(1, (0, scena_h))


def update(m):
    Finish()


def draw(m):
    scena = Image("romeo1.png", (0, 0), scena_w, scena_h)
    ruza = Image("rose.png", (m.x - ruza_w/2, m.y - ruza_h/2), ruza_w, ruza_h)
    Draw(scena, ruza)


Run(setup, update, draw)