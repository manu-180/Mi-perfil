import reflex as rx 
from perfil.components.navbar import navbar
from perfil.views.header.header import header
from perfil.views.links.courses_links import courses_links
from perfil.components.footer import footer
from perfil.styles.styles import Size, BASE_STYLE, MAX_WIDTH, STELESHEWTS
from perfil.components.title import title
from perfil.views.util import *
from perfil.views.routers import Route
 
 
@rx.page(
    title=title_page,
    description=description,
    image=image
)

def cv() -> rx.Component:
    return rx.center(
        rx.image(
            src="/cvv.jpeg",
            width="600px",
            height="auto"
            )
        )