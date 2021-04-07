import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
sud_d = 0.03    # debljina zidova suda
y0 = 0.5        # y koordinata podloge

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 6, 4)
    FramesPerSecond(60)
    UpdatesPerFrame(20)

    m.m = InputFloat(1, (0.1, 1.5))
    teg_razmera = (m.m / 1.5) ** (1/3)
    m.teg_img, m.teg_w, m.teg_h = "crown.png", 1 * teg_razmera, 0.74 * teg_razmera
    
    # m.течност = InputList("алкохол", ("алкохол", "уље", "вода", "жива")) # m.liquid
    # gustine = { "алкохол" : 700, "уље" : 800, "вода" : 1000, "жива" : 13530 }
    # boje = { "алкохол" : "#e9ebf0", "уље" : "#decc04", "вода" : "#afd1ed", "жива" : "#686d75" }
    # m.ro = gustine[m.течност]
    # m.l_clr = boje[m.течност]
    m.ro = InputFloat(1000, (500, 14000)) # gustina tecnosti
    m.l_clr = "#afd1ed" # boja tecnosti (moze da se zatamnjuje sa povecanjem gustine)

    m.izmeren = False
    m.v_u_tecnosti = 0
    m.sila_potiska = 0
    m.g = 10
    m.q1 = 0
    m.q2 = 0

def update(m):
    m.izmeren = True
    m.v_u_tecnosti = m.m / 19300 # kao da je od zlata
    m.sila_potiska = m.v_u_tecnosti * m.ro * m.g
    m.q1 = m.m * m.g
    m.q2 = m.q1 - m.sila_potiska
    Finish()

def crtaj_merenje(m, x0, uronjen):
    dinm_w, dinm_h = 0.25, 1.6
    x2 = x0 - dinm_w / 2
    y1 = y0 + 0.2
    y2 = y1 + 1.0
    teg = Image(m.teg_img, (x0 - m.teg_w/2, y1), m.teg_w, m.teg_h)
    
    teg_leva_nit = Line((x0 - 0.434*m.teg_w, y1 + 0.696*m.teg_h), (x0, y2))
    teg_leva_nit.pen_color = '#ff0000'
    teg_leva_nit.line_width = 0.02
    teg_desna_nit = Line((x0 + 0.423*m.teg_w, y1 + 0.705*m.teg_h), (x0, y2))

    Draw(teg, teg_leva_nit, teg_desna_nit)
    
    q = m.q2 if uronjen else m.q1
    dinm_traka = Image('dynamometer_stripes_vertical.png', (x2, y2), dinm_w, dinm_h)
    dinm_kutija = Image('dynamometer_case_vertical.png', (x2, y2 + 0.1 * q), dinm_w, dinm_h)
    
    str_tekst = f'Q ={abs(q):6.2f} N' if m.izmeren else 'Q = ...'
    tekst_q = Text((x0 + 0.2, y2), str_tekst)
    tekst_q.pen_color = '#ffffff'
    tekst_q.font_size = 0.2
    Draw(dinm_traka,  dinm_kutija, tekst_q)



def draw(m):
    vazduh = Box((0, 0), 6, 4)
    vazduh.fill_color = '#3698bf'
    podloga = Box((0, 0), 6, y0)
    podloga.fill_color = '#6e675f'
    Draw(vazduh, podloga)
    
    sud = Box((3.4-sud_d, y0), 1.2 + 2*sud_d, 1.1)
    sud.fill_color = '#c76f0a'    
    tecnost = Box((3.4, y0 + sud_d), 1.2, 1.0)
    tecnost.fill_color = m.l_clr
    vazduh_u_sudu = Box((3.4, y0 + sud_d + 1.0), 1.2, 0.1 - sud_d)
    vazduh_u_sudu.fill_color = vazduh.fill_color
    Draw(sud, tecnost, vazduh_u_sudu)

    crtaj_merenje(m, 1, False) # uronjen == False
    crtaj_merenje(m, 4, True)  # uronjen == True


Run(setup, update, draw)