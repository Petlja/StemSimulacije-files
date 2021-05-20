from simanim import *

visina_bicikla_u_metrima = 1
sirina_bicikla_u_metrima = visina_bicikla_u_metrima * 1000 / 620
visina_scene_u_metrima = visina_bicikla_u_metrima * 2
sirina_scene_u_metrima = visina_scene_u_metrima * 6614 / 3000

broj_piksela_po_metru = 150

def setup(m):
    PixelsPerUnit(broj_piksela_po_metru)
    ViewBox((0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)

    m.x = 0
    m.y = 0
    m.v = InputFloat(1, (0, 2))
    m.sicX_start = 0.73
    m.sicY = 0.86
    m.kormanX_start = 1.18
    m.kormanY = 0.80

def update(m):
    if (m.x > sirina_scene_u_metrima):
        Finish()

    m.x += m.v * m.dt

def NacrtajLiniju(x_pocetak, x_pomeraj, y, boja):
    x_kraj = x_pocetak + x_pomeraj
    linija = PolyLine([(x_pocetak, y), (x_kraj, y)])
    linija.pen_color = boja
    linija.line_width = 0.01
    Draw(linija)

    krug = Circle((x_kraj, y), 0.02)
    krug.fill_color = boja
    Draw(krug)

def draw(m):
    scena = Image('bicycle_background.png', (0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)
    bicikl = Image('bicikl.png', (m.x, m.y), sirina_bicikla_u_metrima, visina_bicikla_u_metrima)
    Draw(scena, bicikl)

    NacrtajLiniju(m.sicX_start, m.x, m.sicY, '#0000FF')
    NacrtajLiniju(m.kormanX_start, m.x, m.kormanY, '#00FF00')

Run(setup, update, draw)