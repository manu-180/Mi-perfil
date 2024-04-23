import reflex as rx
from perfil.styles.styles import Size, NAVBAR_STYLE
from perfil.styles.colors import Color, TextColor
from perfil.views.routers import Route
from perfil.styles.fuentes import Font


def navbar(text=False) -> rx.Component:
    return rx.hstack(
        rx.link(
                rx.flex(
            rx.hstack(
                rx.hstack(
                    rx.text("Manu",
                        rx.text.strong(
                            "Nv",
                            color=Color.PRIMARY.value,
                            font_family=Font.LOGO.value
                        ),
                    as_="span",
                    font_size=Size.DEFAULT.value,
                    color=TextColor.HEADER.value,
                    padding_left=Size.DEFAULT.value,
                    
                    )),
                # rx.text("Nv",
                #     as_="span",
                #     font_size=Size.DEFAULT.value,
                #     color=Color.SECONDARY.value,
                #     padding_left="0"
                #     ),
                rx.cond(text,
                    rx.text("← Menu principal",
                    color=TextColor.HEADER.value)),
            ),
        ),
        href=Route.Index.value)
        ,
        style=NAVBAR_STYLE
    )
