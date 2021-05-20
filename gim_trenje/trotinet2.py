import math
from simanim import *

# Ukupno imamo 7 zgrada. Ako je svaka široka 6m, tada u sceni ukupno imamo 42 metra.
# Visina scene je 2 puta manja od širine.
sirina_scene_u_metrima = 42
visina_scene_u_metrima = 30
broj_piksela_u_metrima = 15

def setup(m):
    PixelsPerUnit(broj_piksela_u_metrima)
    ViewBox((0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)

    m.v0 = InputFloat(5, (0, 30))
    m.mu = InputFloat(0.1, (0.05, 1.0))

    m.y = 2.4     # pozicija trotineta na y-osi
    m.x = 0       # pozicija trotineta na x-osi na početku simulacije
    m.v = m.v0    # brzina trotineta na početku simulacije
    m.a = 0       # ubrzanje trotineta na početku simulacije
    m.g = 9.81    # ubrzanje Zemljine teže
    m.masa = 50   # masa deteta sa trotinetom

def update(m):
    F_g = ???     # težina deteta sa trotinetom. Normalna sila trotineta na podlogu
    F_t = ???     # intenzitet sile trenja

    m.a = ???     # usporenje

    deltaX = ???  # promena pozicije
    deltaV = ???  # promena brzine
    m.v += deltaV
    m.x += deltaX

    if m.v <= 0:
        Finish()

def draw(m):
    pozadina = Image('city-summer.jpg', (0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)
    Draw(pozadina)

    trotinet = Image('boy-scooter.png', (m.x, m.y), 5, 5)
    Draw(trotinet)

Run(setup, update, draw)