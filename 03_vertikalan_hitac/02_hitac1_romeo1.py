import math
from simanim import *

# konstante:
scena_w, scena_h = 2.3, 4
ruza_w, ruza_h = 0.2, 0.4

h0 = 0.95 # Visina Romeove sake
h1 = 2.5 # Visina Julijine sake

def setup(m):
    PixelsPerUnit(80)
    ViewBox((0, 0), 4, 4)
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

    # brojevi u uslovu su odabrani procenom
    # koliko daleko ruza sme da bude i koliko brzo sme 
    # da se krece da bi Julija mogla da je uhvati
    if m.h == h0 or (abs(m.h - h1) < ruza_h/5 and abs(m.v - -0.1) < 0.1):
        Finish()


def draw(m):
    ruza = Image("rose.png", (1.35 - ruza_w/2, m.h - ruza_h/2), ruza_w, ruza_h)
    scena = Image("romeo1.png", (0, 0), scena_w, scena_h)

    tx = 2.6
    tekst_t = Text((tx, 3.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.15
    tekst_v = Text((tx, 3.5), f'v ={m.v:6.2f}m/s')
    tekst_h = Text((tx, 3.3), f'h ={(m.h-h0):6.2f}m')
    tekst_h1 = Text((tx, 3.1), f'h1 ={(h1-h0):5.2f}m')

    if m.h < h0 + ruza_h:
        Draw(ruza, scena, tekst_t, tekst_v, tekst_h, tekst_h1)
    else:
        Draw(scena, ruza, tekst_t, tekst_v, tekst_h, tekst_h1)

Run(setup, update, draw)