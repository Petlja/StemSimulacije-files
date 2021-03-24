from simanim import *

sirina_bicikla_u_metrima = 2
visina_bicikla_u_metrima = 1.1
sirina_scene_u_metrima = sirina_bicikla_u_metrima * 3
visina_scene_u_metrima = visina_bicikla_u_metrima * 2
broj_piksela_po_metru = 200

def setup(m):
    PixelsPerUnit(broj_piksela_po_metru)
    ViewBox((0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)

    m.x = 0
    m.y = 0.4
    m.v = InputFloat(1, (0, 2))
    m.seatX = 0.84
    m.seatY = 1.04
    m.frontX = 1.42
    m.frontY = 0.86

    m.path2 = [(m.x + m.seatX, m.y + m.seatY)]
    m.path3 = [(m.x + m.frontX, m.y + m.frontY)]

def update(m):
    if (m.x > sirina_scene_u_metrima):
        Finish()

    m.x += m.v * m.dt

    m.path2 += [(m.x + m.seatX, m.y + m.seatY)]
    m.path3 += [(m.x + m.frontX, m.y + m.frontY)]

def NacrtajPutanju(putanja, boja):
    linija = PolyLine(putanja)
    linija.pen_color = boja
    linija.line_width = 0.01
    Draw(linija)

    # center = path[-1]
    # endPoint = Circle(center, 0.02)
    # endPoint.fill_color = color
    # Draw(endPoint)

def draw(m):
    bicikl = Image('bicikl.png', (m.x, m.y), sirina_bicikla_u_metrima, visina_bicikla_u_metrima)
    Draw(bicikl)

    NacrtajPutanju(m.path2, '#0000FF')
    NacrtajPutanju(m.path3, '#00FF00')

Run(setup, update, draw)