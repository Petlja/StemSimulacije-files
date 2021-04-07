import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
visina_suda = 1.9 
sud_d = 0.03 # debljina zidova suda
dno_h = -2.1 # y koordinata dna (y koordinata povrsine tecnosti je 0)

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, dno_h), 6, 4)
    FramesPerSecond(60)
    UpdatesPerFrame(20)

    m.маса_тега = InputFloat(1000, (100, 21000))
    m.течност = InputList("алкохол", ("алкохол", "уље", "вода", "жива"))
    
    teg_razmera = (m.маса_тега / 21000) ** (1/3)
    m.teg_img, m.teg_w, m.teg_h = "weight.png", 0.95 * teg_razmera, 1.15 * teg_razmera
    
    gustine = { "алкохол" : 700, "уље" : 800, "вода" : 1000, "жива" : 13530 }
    boje = { "алкохол" : "#e9ebf0", "уље" : "#decc04", "вода" : "#afd1ed", "жива" : "#686d75" }

    m.h = 0 # nivo dna bureta
    m.v = 0
    m.v_u_tecnosti = 0
    m.ro = gustine[m.течност]
    m.l_clr = boje[m.течност]
    m.k_r = -9 * m.ro # uzeto otprilike, da se dobije dobar efekat
    m.sila_potiska = 0
    m.g = 10

def update(m):
    if m.h + visina_suda >= 0: # ako sud pluta
        m.v_u_tecnosti = -m.h * s0
        m.sila_potiska = m.v_u_tecnosti * m.ro * m.g
    else:
        m.v_u_tecnosti = visina_suda * s0
        m.sila_potiska = 0 # sud je potonuo, nema potiska

    f_otp = m.k_r * m.v # sila otpora tecnosti (u smeru suprotnom od vektora brzine)
    
    rez_sila = f_otp + m.sila_potiska - m.g * m.маса_тега
    a = rez_sila / m.маса_тега

    m.h = max(dno_h, m.h + m.v * m.dt)
    m.v += a * m.dt

    if (abs(a) < 0.0001 and abs(m.v) < 0.00001) or m.h == dno_h:
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

    teg = Image(m.teg_img, (1-m.teg_w/2, m.h), m.teg_w, m.teg_h)

    Draw(pozadina, tecnost, sud, sud_unutra, teg)

    v_ukupno = Text((2.2, 0.2), f'V ={(visina_suda * s0):6.2f} m³')  
    v_ukupno.pen_color = '#000000'
    v_ukupno.font_size = 0.25
    t_zap = Text((2.2, 0.0), f'v ={m.v_u_tecnosti:6.2f} m³')

    t_fp = Text((2.2, -0.8), f'Fp ={abs(0.001*m.sila_potiska):6.2f} KN')
    t_mg = Text((2.2, -1.0), f'mg ={abs(0.001*m.g*m.маса_тега):6.2f} KN')

    Draw(v_ukupno, t_zap, t_fp, t_mg)

    if False: # debug
        f_otp = m.k_r * m.v # sila otpora tecnosti
        rez_sila = f_otp + m.sila_potiska - m.g * m.маса_тега
        a = rez_sila / m.маса_тега

        t_fotp = Text((2, -1.2), f'Fo ={(f_otp)} N')
        tekst_fr = Text((2, -1.4), f'Fr ={(rez_sila)} N')
        tekst_a = Text((2, -1.6), f'a ={a} m/s²')
        tekst_v = Text((2, -1.8), f'v ={m.v} m/s')
        Draw(t_fotp, tekst_fr, tekst_a, tekst_v)

Run(setup, update, draw)