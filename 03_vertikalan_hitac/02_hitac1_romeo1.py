import math
from simanim import *

# konstante:
scena_w, scena_h = 2.56, 4
ruza_w, ruza_h = 0.25, 0.4

h0 = 1.2 # Visina Romeove sake
h1 = 2.8 # Visina Julijine sake

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 2.6, 4)
    FramesPerSecond(60)
    UpdatesPerFrame(10)

    m.v0 = InputFloat(7.1, (1, 9))

    m.h = h0    # m.h ce biti visina sredista ruze
    m.v = m.v0  # m.v ce biti brzina ruze
    m.g = 10    # koristimo g = 10 zbog jednostavnijeg racunanja


def update(m):
    m.h = max(h0, m.h + m.v * m.dt) # ne nize od Romeove ruke
    m.v -= m.g * m.dt 

    # brojevi u uslovu su odabrani procenom
    # koliko daleko ruza sme da bude i koliko brzo sme 
    # da se krece da bi Julija mogla da je uhvati
    if m.h == h0 or (abs(m.h - h1) < ruza_h/5 and abs(m.v - -0.8) < 0.3):
        Finish()


def draw(m):
    scena = Image("romeo1.png", (0, 0), scena_w, scena_h)
    ruza = Image("rose.png", (1.6 - ruza_w/2, m.h - ruza_h/2), ruza_w, ruza_h)

    Draw(scena, ruza)

    tekst_t = Text((1.4, 3.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.15
    tekst_v = Text((1.4, 3.5), f'v ={m.v:6.2f}m/s')
    tekst_h = Text((1.4, 3.3), f'h ={(m.h-h0):6.2f}m')
    tekst_h1 = Text((1.4, 3.1), f'h1 ={(h1-h0):5.2f}m')

    Draw(tekst_t, tekst_v, tekst_h, tekst_h1)

Run(setup, update, draw)