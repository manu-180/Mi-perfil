import reflex as rx 
from perfil.components.link_button.link_icon import link_icon
from perfil.components.info_text import info_text
from perfil.styles.colors import TextColor, Color
from perfil.styles.styles import TITLE_STYLE, Size
from perfil.styles.fuentes import Font
from perfil.constants.constants import *
import perfil.styles.styles as styles



def header(detail=True, animated=False) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
    size="8",  
    src="/2.jpg",
    padding = "1px",
    style={"border-radius": "100%", "border": "3px solid #AC5699 !important"}),
            rx.vstack(
                rx.heading(
                    "Manuel Navarro",
                        size="6",
                        font_family=Font.TITLE.value
                        ),
                rx.text(
                    "@ManuNv",
                ),
            rx.hstack(
                link_icon(LINKEDIN_URL,"/imagen_icon/linkedin-in.svg","linkedin"),
                link_icon(IG_URL,"/imagen_icon/instagram.svg","instagram"),
                link_icon("https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcRwRdqSjkhHNlRzLqlTGwVTwRNHwTfQwXCWghLDmhCxqJcBQGLCJLxFfCqwWNbzRgrmVsZsz", "/imagen_icon/envelope-regular.svg","gmail"),
                link_icon("https://twitter.com/Inicio/","/imagen_icon/twitter.svg","twitter"))),
            color= TextColor.BODY.value,
            spacing="3",
            style=TITLE_STYLE
        ),
        rx.cond(
            detail,
                rx.flex(
                    rx.hstack(
                info_text("Lenguaje"," Python"),
                rx.spacer(),
                info_text("Framework"," Reflex"),
                width= "100%",
                color= TextColor.HEADER.value,
                white_space = "normal",
                align="start",
                padding_bottom=Size.DEFAULT.value),
                ),
            ),
        rx.cond(
            detail,
            rx.text("Mi nombre es Manuel Navarro, especialista en creación de páginas web. Mi experiencia abarca desde el diseño hasta el desarrollo y la optimización de sitios web",
                color= TextColor.HEADER.value)),
        width = "100%")
    