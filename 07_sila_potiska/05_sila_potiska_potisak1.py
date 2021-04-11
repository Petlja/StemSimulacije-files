import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
visina_suda = 1.9 
sud_d = 0.03    # debljina zidova suda
dno_h = -2.1    # y koordinata dna (y koordinata povrsine tecnosti je 0)
g = 10          # ubrzanje zemljine teze
gustine = { 
    "алкохол" : 700, 
    "уље" : 800, 
    "вода" : 1000, 
    "жива" : 13530 
}
boje = { 
    "алкохол" : "#e9ebf0", 
    "уље" : "#decc04", 
    "вода" : "#afd1ed", 
    "жива" : "#686d75" 
}

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, dno_h), 6, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(100) # vazno!

    m.маса_тега = InputFloat(1000, (100, 21000))
    m.течност = InputList("алкохол", ("алкохол", "уље", "вода", "жива"))
    m.l_clr = boje[m.течност]
    m.ro = gustine[m.течност]
    m.k_r = 9 * m.ro # uzeto otprilike, da se dobije dobar efekat

    m.v_u_tecnosti = 0 # zapremina uronjenog dela bureta
    m.F_potiska = 0
    m.F_otpora = 0 # sila otpora tecnosti (u smeru suprotnom od brzine)
    m.F_rez = 0
    m.a = 0 # ubrzanje bureta
    m.v = 0 # brzina bureta
    m.h = 0 # polozaj dna bureta, na pocetku na povrsini tecnosti

def update(m):
    # racunanje novog stanja u lokalnim promenljivama
    if m.h + visina_suda >= 0: # ako bure pluta (vrh je iznad povrsine)
        v_u_tecnosti = abs(m.h) * s0
        F_potiska = abs(m.h) * s0 * m.ro * g
    else: # tecnost preliva vrh bureta
        v_u_tecnosti = visina_suda * s0
        F_potiska = 0 # u sud je usla tecnost, nema potiska
    F_otpora = m.k_r * m.v 
    F_rez = g * m.маса_тега - F_otpora - F_potiska # nanize
    a = F_rez / m.маса_тега # nanize
    v = m.v + a * m.dt      # nanize
    h = m.h - m.v * m.dt - a * m.dt * m.dt / 2
    if h < dno_h:
        h = dno_h

    # pamcenje novog stanja
    m.v_u_tecnosti = v_u_tecnosti
    m.F_potiska = F_potiska
    m.F_otpora = F_otpora
    m.F_rez = F_rez
    m.a = a
    m.v = v
    m.h = h

    if m.h == dno_h or (abs(m.a) < 0.0001 and abs(m.v) < 0.00001):
    # if m.h == dno_h or abs(g * m.маса_тега - F_potiska) < 1:
        # bure je potonulo, ili je razlika sila manja od 0.001 KN
        Finish()

def draw(m):
    pozadina = Box((0, dno_h), 6, 4)
    pozadina.fill_color = '#ffffff'
    
    tecnost = Box((0, dno_h), 2, -dno_h)
    tecnost.fill_color = m.l_clr
    
    sud = Box((0.5, m.h), 1.0, visina_suda)
    sud.fill_color = '#753904'
    
    sud_unutra = Box((0.5 + sud_d, m.h + sud_d), 1 - 2*sud_d, visina_suda - sud_d)
    if m.h + visina_suda >= 0: # ako pluta
        sud_unutra.fill_color = sud.fill_color
    else:
        sud_unutra.fill_color = m.l_clr

    teg_razmera = (m.маса_тега / 21000) ** (1/3)
    teg_w, teg_h = 0.95 * teg_razmera, 1.15 * teg_razmera
    teg = Image("weight.png", (1 - teg_w/2, m.h), teg_w, teg_h)

    Draw(pozadina, tecnost, sud, sud_unutra, teg)

    v_ukupno = Text((2.2, 0.2), f'V ={(visina_suda * s0):6.2f} m³')  
    v_ukupno.pen_color = '#000000'
    v_ukupno.font_size = 0.25
    t_zap = Text((2.2, 0.0), f'v ={m.v_u_tecnosti:6.2f} m³')

    t_fp = Text((2.2, -0.8), f'Fp ={abs(0.001*m.F_potiska):6.2f} KN')
    t_mg = Text((2.2, -1.0), f'mg ={abs(0.001*g*m.маса_тега):6.2f} KN')

    Draw(v_ukupno, t_zap, t_fp, t_mg)


Run(setup, update, draw)