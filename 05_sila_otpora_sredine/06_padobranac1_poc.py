import math
from simanim import *

masa = 0.1
k_otp = 0.5 # koeficijent otpora
x_oblak = (0.9, 3.2, 3.7, 6.6, 8.1)
y0_oblak = (2.5, 7.6, 3.3, 9.2, 5.3)
br_oblaka = len(x_oblak)
g_x0, g_y0 = 0.3, 0.3 # koordinatni pocetak grafika
scena_w, scena_h = 10, 8
oblak_w, oblak_h = 2, 0.8

def setup(m):
    PixelsPerUnit(50)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(10)

    m.vp = InputFloat(8, (0.1, 12)) # brzina pri kojoj se otvara padobran
    m.uspori = InputList(1, [1, 2, 5, 10]) # usporava simulaciju zadati broj puta

    m.h_oblak = [0] * br_oblaka
    for i in range(br_oblaka):
        m.h_oblak[i] = y0_oblak[i]

    m.v = 0     # brzina padobranca (tj. svega ostalog u odnosu na padobranca)
    m.g = 10
    m.a = m.g   # pozitivno kada je vektor ubrzanja usmeren na dole
    m.padobran = False
    m.s_ravn = 0

def update(m):
    dt = m.dt / m.uspori
    
    if m.v >= m.vp:
        m.padobran = True

    f = masa * m.g
    f_otp = k_otp * m.v if m.padobran else 0
    m.a = (f - f_otp) / masa
    
    dh = m.v * dt + m.a * dt * dt / 2
    dv = m.a * dt

    # visini oblaka dodajemo dh jer smo u ref. sistemu padobranca,
    # tj. padobranac stoji a sve ostalo se krece suprotno (na gore)
    for i in range(br_oblaka):
        m.h_oblak[i] += dh
        if m.h_oblak[i] > scena_h:
            m.h_oblak[i] -= (scena_h + oblak_h) # "novi oblak"

    m.v += dv

    if abs(m.a) < 0.001:
        m.s_ravn += dh
        if m.s_ravn >= 3.3:
            Finish()

def draw(m):
    # pozadina
    pozadina = Box((0, 0), scena_w, scena_h)
    pozadina.fill_color = '#cadade'
    Draw(pozadina)
    
    # oblaci
    for i in range(br_oblaka):
        ime_slike = 'cloud' + str(i) + '.png'
        oblak = Image(ime_slike, (x_oblak[i], m.h_oblak[i]), oblak_w, oblak_h)
        Draw(oblak)
    
    # zemlja
    zemlja = Box((0, 0), scena_w, m.s_ravn)
    zemlja.fill_color = '#d9c9b6'
    Draw(zemlja)
    
    # tekstualni podaci
    tekst_v = Text((7, 7.5), f'v ={abs(m.v):6.2f}')
    tekst_v.pen_color = '#000000'
    tekst_v.font_size = 0.5
    Draw(tekst_v)

    # padobranac
    padobran = Image('parachute.png', (4, 4), 2, 2)
    if m.padobran:
        Draw(padobran)
    padobranac = Image('bird.png', (4, 2.5), 2, 2)
    Draw(padobranac)


Run(setup, update, draw)