import math
from simanim import *

dubina_mora = 9
scena_w, scena_h = 50, 30
brod_w, brod_h = 15, 9

def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, -dubina_mora), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.f = InputFloat(10_000, (0, 20_000))  # sila koja potice od veslanja
    m.f_vetra = 10_000
    m.brod_masa = 10_000
    m.a = (m.f_vetra + m.f) / m.brod_masa
    m.v = 0 # brzina broda (na desno)
    m.x = 0 # leva tacka broda

def update(m):
    m.x += m.v * m.dt + m.a * m.dt * m.dt / 2
    m.v += m.a * m.dt
    if m.x + brod_w >= 50:
        Finish()


def draw(m):
    nebo = Box((0, 0), scena_w, scena_h - dubina_mora)
    nebo.fill_color = '#b5d6ef'
    more = Box((0, -dubina_mora), scena_w, dubina_mora)
    more.fill_color = '#587acb'
    brod = Box((m.x, 0), brod_w, brod_h)
    brod.fill_color = '#000000'
    Draw(nebo, more, brod)

Run(setup, update, draw)