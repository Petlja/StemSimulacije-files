import math
from simanim import *

# konstante:
sl_dole_w, sl_dole_h = 2.55, 3.78
sl_gore_w, sl_gore_h = 2.55, 2.62
balon_w, balon_h = 2.55, 2.62 # dimenzije slike balona su iste kao dimenzije 
                              # gornje slike, a oko balona je transparentna pozadina
h0 = 0.2 # visina poda (prikazana kao 0)
h_b = (1 - 278/472)*2.62 # Visina donje tacke balona u gornjoj slici = 1.077

def setup(m):
    PixelsPerUnit(70)
    ViewBox((0, 0), 5, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.v0 = InputFloat(10, (0.1, 29.9)) # pocetna brzina na dole
    m.H = InputFloat(3.3,(2.3,4.3)) # rastojanje od pocetne pozicije balona do poda

    m.y_gornje_sl = m.H - (h_b - h0)
    m.h = m.H + h0 # visina donje tacke balona u simulaciji
    m.v = m.v0 # m.v ce biti brzina nanize
    m.g = 10 # koristimo g = 10 zbog jednostavnijeg racunanja

def update(m):
    v_novo = m.v + m.g * m.dt
    h_novo = m.h - m.v * m.dt - m.g * m.dt * m.dt / 2
    if h_novo < h0:
        h_novo = h0 # ne nize od poda

    m.h, m.v = h_novo, v_novo

    if m.h == h0:
        Finish()

def draw(m):
    sl_gore = Image("romeo3_upper.png", (0, m.y_gornje_sl), sl_gore_w, sl_gore_h)
    sl_dole = Image("romeo3_lower.png", (0, 0), sl_dole_w, sl_dole_h)
    balon = Image("romeo3_balloon.png", (0, m.h - h_b), balon_w, balon_h)

    tekst_t = Text((3, 5.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.25
    tekst_v = Text((3, 5.5), f'v ={abs(m.v):6.2f}m/s')
    tekst_h = Text((3, 5.3), f'h ={(m.h-h0):6.2f}m')

    Draw(sl_dole, sl_gore, balon, tekst_t, tekst_v, tekst_h)

Run(setup, update, draw)