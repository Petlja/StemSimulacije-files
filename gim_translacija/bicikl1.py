from simanim import *

sirina_bicikla_u_metrima = 2
visina_bicikla_u_metrima = 1.1
sirina_scene_u_metrima = sirina_bicikla_u_metrima * 3
visina_scene_u_metrima = visina_bicikla_u_metrima * 2
broj_piksela_po_metru = 150

def setup(m):
    PixelsPerUnit(broj_piksela_po_metru)
    ViewBox((0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)

    m.x = 0
    m.y = 0.4
    m.v = InputFloat(1, (0, 2))

def update(m):
    m.x += m.v * m.dt

def draw(m):
    bicikl = Image('bicikl.png', (m.x, m.y), sirina_bicikla_u_metrima, visina_bicikla_u_metrima)
    Draw(bicikl)

Run(setup, update, draw)