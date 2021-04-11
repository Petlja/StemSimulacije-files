import math
from simanim import *

scena_w = 70
w_skijas = 2

# konstante sa slike
scena_w_pix, scena_h_pix = 2874, 544
scena_h = scena_h_pix/scena_w_pix * scena_w
visina_podloge = 50/scena_w_pix * scena_w
x_poc_pada = 123/scena_w_pix * scena_w
x_kraj_pada = 680/scena_w_pix * scena_w
y_poc_pada = (1 - 240/scena_h_pix) * scena_h
y_kraj_pada = (1 - 380/scena_h_pix) * scena_h

pad_dx = x_kraj_pada - x_poc_pada
pad_dy = y_poc_pada - y_kraj_pada

tan_ugla = abs(y_kraj_pada - y_poc_pada) /
cos_ugla = 1 / math.sqrt(tan_ugla * tan_ugla + 1)
sin_ugla = cos_ugla * tan_ugla
ugao = math.atan(tan_ugla)

scena_w_pix_skijas, scena_h_pix_skijas = 658, 491
h_skijas = w_skijas * scena_h_pix_skijas / scena_w_pix_skijas


def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(50)

    m.терен = InputList("лед", ("лед", "сув снег", "влажан снег"))
    # vrednost m.mi za "лед" iz tablica je 0.02, ali onda skijas ode predaleko
    m.mi = {"лед" : 0.065, "сув снег" : 0.35, "влажан снег" : 0.4}[m.терен] # koeficijent trenja
    m.boja_podloge = {"лед" : '#baf7f7', "сув снег" : '#f0f5f5', "влажан снег" : '#d5dede'}[m.терен]

    m.v0 = 0
    m.x = x_poc_pada + w_skijas
    m.y = y_poc_pada - w_skijas * tan_ugla
    m.v = m.v0
    m.a = 0
    m.g = 10
    m.masa = 80
    m.nagnut = True

    m.v1 = 0
    m.s1 = 0
    m.t1 = 0


def update(m):
    if m.nagnut:
        F_rez = sin_ugla * m.masa * m.g # u smeru nizbrdice
        m.a = F_rez / m.masa
        m.v += m.a * m.dt
        ds = m.v * m.dt
        m.x += ds * cos_ugla
        m.y -= ds * sin_ugla
    else:
        F_rez = m.mi * m.masa * m.g # na levo (trenje)
        m.a = F_rez / m.masa
        m.v -= m.a * m.dt
        ds = m.v * m.dt
        m.x += ds

    if m.x > x_kraj_pada:
        m.s1 += ds
        m.t1 += m.dt
        if m.nagnut:
            m.v1 = m.v

    m.nagnut = (x_poc_pada < m.x < x_kraj_pada)
    if m.x >= scena_w:
        Finish()
    elif abs(m.v) < 0.001:
        m.a = 0
        Finish()


def hex_boja(k):
    r, g, b = map(int, (k*218, k*241, k*248))
    return f'#{r:02x}{g:02x}{b:02x}'


def crtaj_vektor(x, y, dx, dy, boja):
    dd = dx*dx + dy*dy
    if dd > 0:
        vec = Arrow((x, y), (x + dx, y + dy))
        vec.pen_color = boja
        vec.line_width = 0.1
        vec.head_len = 0.3 if dd > 0.3*0.3 else math.sqrt(dd)/2
        Draw(vec)


def draw(m):
    # scena
    scena = Image('skier_background.png', (0, 0), scena_w, scena_h)
    Draw(scena)

    # skijas
    skijas = Image('skier.png', (m.x - w_skijas, m.y), w_skijas, h_skijas)
    if m.nagnut:
        sin, cos = sin_ugla, cos_ugla
        with Rotate((m.x, m.y), ugao):
            Draw(skijas)
    else:
        sin, cos = 0, 1
        Draw(skijas)
        
    podloga = Box( (x_kraj_pada, y_kraj_pada - visina_podloge), scena_w - x_kraj_pada, visina_podloge)
    podloga.fill_color = m.boja_podloge
    Draw(podloga)
        
    
    if False: # debug
        # vektori brzine i ubrzanja
        crtaj_vektor(m.x-w_skijas, m.y, 3 * m.a * cos, 3 * m.a * sin, '#ff0000')
        crtaj_vektor(m.x, m.y, 3 * m.v * cos, 3 * m.v * sin, '#0000ff')
        t_a = Text((45, 0.5), f'a = {m.a:5.2f}m/s²')
        t_a.font_size = 1.0
        t_a.pen_color = '#ff0000'
        t_v = Text((60, 0.5), f'v = {m.v:5.2f}m/s')
        t_v.pen_color = '#0000ff'
        Draw(t_a, t_v)

    # tekst (v0, t, s za ravan deo posle pada)
    t_teren = Text((scena_w / 2, y_kraj_pada - visina_podloge), m.терен)
    t_teren.pen_color = '#000000'
    t_teren.font_size = 1.5
    Draw(t_teren)
    if m.x > x_kraj_pada:
        t_v = Text((0, 0.5), f'v0 = {m.v1:5.2f}m/s')
        t_t = Text((15, 0.5), f' t = {m.t1:5.2f}s')
        t_s = Text((30, 0.5), f' s = {m.s1:5.2f}m')
        Draw(t_v, t_t, t_s)


Run(setup, update, draw)
