import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(60)
    UpdatesPerFrame(1)

    m.mi = InputFloat(0.2, (0.15, 0.4)) # koficijent trenja
    m.masa = InputFloat(1.5, (1, 2.7))

    m.g = 10
    m.F = 0.0
    m.Ftr = 0.0
    m.Fr = 0.0 # rezultanta sila
    m.v = 0.0
    m.x = 0.0
    m.sanduk_w = m.masa ** (1/3)
    m.tabela = []


def update(m):
    maxtr = m.mi * m.masa * m.g
    m.Ftr = min(maxtr, m.F)
    m.Fr = m.F - m.Ftr
    a = m.Fr / m.masa
    
    m.x += m.v * m.dt
    m.v += a * m.dt

    if m.update_count % 5 == 0:
        # dopunjavamo tabelu
        if abs(m.F - round(m.F)) < 1e-3:
            if len(m.tabela) > 0 and m.tabela[-1][0] + 1e-3 < maxtr < m.F - 1e-3:
                m.tabela += [(maxtr, -maxtr)]
            m.tabela += [(m.F, m.Ftr)]

        # povecavamo silu vuce dok sanduk ne postigne dovoljnu brzinu (procena)
        if m.v <= 1.0:
            m.F += 0.1 
        else:
            m.tabela += [(m.F, m.Ftr)]
            Finish()

    if m.x >= 10:
        Finish()


def crtaj_vektor(x, y, dx, dy, boja):
    dd = dx*dx + dy*dy
    if dd > 1e-6:
        vec = Arrow((x, y), (x + dx, y + dy))
        vec.pen_color = boja
        vec.line_width = 0.05
        vec.head_len = 0.2 if dd > 0.2*0.2 else math.sqrt(dd)/2
        Draw(vec)


def hex_boja(k):
    r, g, b = map(int, (k*218, k*241, k*248))
    return f'#{r:02x}{g:02x}{b:02x}'


def draw(m):
    pozadina = Box((0, 0), 10, 6)
    pozadina.fill_color = '#3698bf' # plava

    y0 = 2.5
    pod = Box((0, 0), 10, y0)
    pod.fill_color = hex_boja(1 - m.mi) # tamnija za vece trenje
    
    
    dinm_w = 1.6 # 16 crta dinamometra (sa slike) se prikazuje kao dinm_w duznih jedinica
    k_dinm = dinm_w/16 # jedna crta (1N) je dinm_w/16
    x0 = 2.5 + m.x
    sanduk = Image('box.png', (x0, y0), m.sanduk_w, m.sanduk_w)
    x1 = x0 + m.sanduk_w
    kutija = Image('dynamometer_case.png', (x1, y0 + 0.1), dinm_w, 0.5)
    traka = Image('dynamometer_stripes.png', (x1 + k_dinm * m.Ftr, y0 + 0.1), dinm_w, 0.5)
    x2 = x1 + k_dinm * m.Ftr + dinm_w
    
    Draw(pozadina, pod, sanduk, traka, kutija)

    # aktivna sila, sila trenja, rezultanta
    k = 0.1
    crtaj_vektor(x2, y0 + 0.35, m.F * k, 0, '#ffff00')
    crtaj_vektor(x0, y0 - 0.1, -m.Ftr * k, 0, '#ff0000')
    crtaj_vektor(x1, y0 - 0.1, m.Fr * k, 0, '#008000')
    
    # uspravne sile
    mg = abs(m.masa * m.g)
    crtaj_vektor(x0 + m.sanduk_w/2, y0 + m.sanduk_w/2, 0, -k * mg, '#000000') # mg
    crtaj_vektor(x0 + m.sanduk_w/2, y0 + m.sanduk_w/2, 0, k * mg, '#805000') # N

    tekst_F = Text((6, 1.2), f'  F={abs(m.F):6.2f}N')
    tekst_F.font_size = 0.5
    tekst_F.pen_color = '#ffff00'
    tekst_Ftr = Text((6, 0.7), f'Ftr={abs(m.Ftr):6.2f}N')
    tekst_Ftr.pen_color = '#ff0000'
    tekst_Fr = Text((6, 0.2),  f' Fr={abs(m.Fr):6.2f}N')
    tekst_Fr.pen_color = '#008000'

    tekst_n = Text((0.5, 0.7),  f' N={mg:6.2f}N')
    tekst_n.pen_color = '#805000'
    tekst_mg = Text((0.5, 0.2),  f' mg={mg:6.2f}N')
    tekst_mg.pen_color = '#000000'
    Draw(tekst_F, tekst_Ftr, tekst_Fr, tekst_n, tekst_mg)
    
    xt, yt, dyt = 0.1, 5.70, 0.25
    tekst_pozadina = Box((xt, yt), dyt*10, dyt*0.9)
    tekst_pozadina.fill_color = '#404040'
    tekst_1 = Text((xt, yt), '    F')
    tekst_1.font_size = dyt
    tekst_1.pen_color = '#ffff00'
    tekst_2 = Text((xt, yt), '             Ftr')
    tekst_2.pen_color = '#ff0000'
    Draw(tekst_pozadina, tekst_1, tekst_2)
    for  f, ftr in m.tabela:
        yt -= dyt
        tekst_pozadina = Box((xt, yt), dyt*10, dyt*0.9)
        tekst_pozadina.fill_color = '#404040'
        tekst_1 = Text((xt, yt),  f'{abs(f):6.2f}N')
        tekst_1.pen_color = '#ffff00'
        tekst_2 = Text((xt, yt),  f'         {abs(ftr):6.2f}N')
        tekst_2.pen_color = '#ff0000'
        Draw(tekst_pozadina, tekst_1, tekst_2)


Run(setup, update, draw)
