import math
from simanim import *

h0 = 1 # pocetna visina ruze

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 4, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.v0 = InputFloat(4, (1, 9))

    m.h = 1     # m.h ce biti visina sredista ruze
    m.v = m.v0  # m.v ce biti brzina ruze
    m.g = 10    # koristimo g = 10 zbog jednostavnijeg racunanja


def update(m):
    dv = - m.g * m.dt
    dh = m.v * m.dt - m.g * m.dt * m.dt / 2

    m.h += dh
    m.v += dv
    if m.h < h0:
        m.h = h0 # ne nize od Romeove ruke

    if m.h == h0:
        Finish()


def draw(m):
    ruza = Image("rose.png", (2, m.h), 0.2, 0.4)
    Draw(ruza)

Run(setup, update, draw)