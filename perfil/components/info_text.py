import reflex as rx 
from perfil.styles.colors import Color
from perfil.styles.styles import Size, FontWeight

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
        rx.text(title,
                rx.text.span(
                    body,
                    font_weight= FontWeight.MEDIUM.value, 
                    color = Color.SECONDARY.value),
                    argin_right = Size.BIG.value)
            ),
            margin_right = Size.BIG.value
        )       