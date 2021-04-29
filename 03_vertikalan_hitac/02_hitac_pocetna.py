import math
from simanim import *

# konstante:            
scena_w, scena_h = 4.6, 6
ruza_w, ruza_h = 0.25, 0.5
h0 = 1.30 # Visina Romeove sake
h1 = 3.54 # Visina Julijine sake

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 4.6, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.v0 = InputFloat(7.1, (1, 9))

    m.h = h0    # m.h ce biti visina sredista ruze
    m.v = m.v0  # m.v ce biti brzina ruze
    m.g = 10    # koristimo g = 10 zbog jednostavnijeg racunanja


def update(m):
    dv = - m.g * m.dt
    dh = m.v * m.dt - m.g * m.dt * m.dt / 2

    m.h += dh
    m.v += dv
    if m.h < h0:
        m.h = h0 # ne nize od Romeove ruke

    if m.h == h0 or (abs(m.h - h1) < ruza_h/10 and abs(m.v) <= 0.1):
        Finish()


def draw(m):
    scena = Image("romeo1_background.png", (0, 0), scena_w, scena_h)
    ruza = Image("rose.png", (2.55 - ruza_w/2, m.h - ruza_h/2), ruza_w, ruza_h)
    romeo = Image("romeo1_romeo.png", (0, 0), scena_w, scena_h)
    Draw(scena, ruza, romeo)


Run(setup, update, draw)