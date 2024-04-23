import reflex as rx 
from perfil.components.navbar import navbar
from perfil.views.header.header import header
from perfil.views.links.index_links import index_links
from perfil.components.footer import footer
from perfil.styles.styles import Size, BASE_STYLE, MAX_WIDTH, STELESHEWTS
from perfil.components.title import title
from perfil.views.util import *
from perfil.components.float_button import float_button 
from perfil.constants.constants import MERCADO_PAGO
from perfil.styles.styles import REBOTAR, APARECE
 
@rx.page(
    title=title_page,
    description=description,
    image=image
)
def index() -> rx.Component:
    return rx.box(
        rx.link(
        float_button(),
        href=MERCADO_PAGO,
        is_external=True),
        lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            title("Contactame en mis redes:"),
            index_links(),
            title("Contactame en mis redes:"),
            index_links(),
            width="100%",
            margin_y=Size.BIG.value,
            max_width=MAX_WIDTH)),
        rx.vstack(  
            footer(),
            align="center",
            padding_x=Size.VERY_SMALL.value),
        padding=Size.MEDIUM.value,
)

