from simanim import *

def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, 0),60, 20)
    m.x = 0
    m.y = 0
    m.v = 10

def update(m):
    m.x += m.v * m.dt
    print(m.dt)

def draw(m):
    kutija = Box((m.x,m.y), 10, 5)
    kutija.fill_color = '#000000'
    Draw(kutija)

Run(setup, update, draw)
