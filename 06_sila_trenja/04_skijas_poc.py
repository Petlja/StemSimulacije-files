import math
from simanim import *

scena_w, scena_h = 70, 13.25
w_skijas, h_skijas = 2, 1.5
visina_podloge = 1.22
x_0 = 16.56 # x koordinata kraja strmog dela
y_0 = 4     # y koordinata kraja strmog dela

def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.терен = InputList("лед", ("лед", "сув снег", "влажан снег"))
    # vrednost m.mi za "лед" iz tablica je 0.02, ali onda skijas ode predaleko
    k_trenja = {"лед" : 0.065, "сув снег" : 0.35, "влажан снег" : 0.4}
    m.mi = k_trenja[m.терен] # koeficijent trenja
    boje = {"лед" : '#baf7f7', "сув снег" : '#f0f5f5', "влажан снег" : '#d5dede'}
    m.boja_podloge = boje[m.терен]

    m.v0 = 7.63 # u ovoj simulaciji pocetna brzina moze da bude bilo koja vrednost

    m.x, m.y = x_0, y_0 # polozaj skijasa
    m.v = m.v0          # brzina skijasa
    m.a = 0             # ubrzanje skijasa
    m.g = 10            # zemljino ubrzanje
    m.masa = 80         # masa skijasa


def update(m):
    F = m.mi * m.masa * m.g # sila usmerena na levo (trenje)
    m.a = F / m.masa
    dv = -m.a * m.dt
    dx = m.v * m.dt - m.a * m.dt * m.dt / 2
    m.v += dv
    m.x += dx

    if m.x >= scena_w:
        Finish()
    elif m.v < 0.001:
        m.a = 0
        Finish()


def draw(m):
    scena = Image('skier_background.png', (0, 0), scena_w, scena_h)
    skijas = Image('skier.png', (m.x - w_skijas, m.y), w_skijas, h_skijas)
    podloga = Box( (x_0, y_0 - visina_podloge), scena_w - x_0, visina_podloge)
    podloga.fill_color = m.boja_podloge
    Draw(scena, skijas, podloga)

    t_teren = Text((scena_w / 2, y_0 - visina_podloge), m.терен)
    t_teren.pen_color = '#000000'
    t_teren.font_size = 1.5

    t_v = Text((0, 0.5), f'v0 = {m.v0:5.2f}m/s')
    t_t = Text((15, 0.5), f' t = {m.t:5.2f}s')
    t_s = Text((30, 0.5), f' s = {(m.x - x_0):5.2f}m')
    Draw(t_teren, t_v, t_t, t_s)


Run(setup, update, draw)
