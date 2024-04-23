import reflex as rx 
from perfil.components.navbar import navbar
from perfil.views.header.header import header
from perfil.views.links.courses_links import courses_links
from perfil.components.footer import footer
from perfil.styles.styles import Size, BASE_STYLE, MAX_WIDTH, STELESHEWTS
from perfil.components.title import title
from perfil.views.util import *
from perfil.views.routers import Route
from perfil.components.float_button import float_button 
from perfil.constants.constants import MERCADO_PAGO
 
@rx.page(
    route=Route.Courses.value,
    title=title_page,
    description=description,
    image=image
)
def courses() -> rx.Component:
    return rx.box(
        rx.link(
        float_button(),
        href=MERCADO_PAGO,
        is_external=True),
        lang(),
        navbar(text=True),
        rx.center(
            rx.vstack(
            header(detail=False),
            title("Mis estudios:"),
            courses_links(),
            width="100%",
            margin_y=Size.BIG.value,
            max_width=MAX_WIDTH)),
        rx.vstack(  
            footer(detail=False),
            align="center",
            padding_x=Size.VERY_SMALL.value),
        padding=Size.MEDIUM.value
)

