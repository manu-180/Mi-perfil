import reflex as rx
import datetime
from perfil.styles.colors import TextColor
from perfil.styles.styles import Size, BASE_STYLE
from perfil.styles.images import Imagen
from perfil.styles.fuentes import Font
from perfil.styles.styles import Size, MAX_WIDTH, APARECE


def footer(detail=True) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.cond(
                detail,
        rx.box(
            rx.heading("Click aqui↓↓↓",
                margin="0px",
                size="7",
                   font_family=Font.DEFAULT.value),
            rx.image(src= Imagen.realogo,
                    on_click=Imagen.cambiar_imagen(),
                    height="10em",
                    width="10em",
                    alt= "logo",
                    class_name=APARECE
                )
            )
            ),
        rx.text(f"2023-{datetime.datetime.now().year} Manuel Navarro diseñador web",
        margin_y = "0px",
        padding_y="0px"),
        rx.spacer(),
        color= TextColor.FOOTER.value,
        margin_y = "0px",
        padding_y="0px"
    ))
    
    