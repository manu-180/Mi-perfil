import reflex as rx 
from index.components.navbar import navbar
from index.views.header.header import header
from index.views.links.courses_links import courses_links
from index.components.footer import footer
from index.styles.styles import Size, BASE_STYLE, MAX_WIDTH, STELESHEWTS
from index.components.title import title
from index.views.util import *
from index.views.routers import Route
 
 
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