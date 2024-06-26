import reflex as rx 
from index.styles.styles import BOTTON_TITLE_STYLE, BOTTON_BODY_STYLE
from index.styles.colors import Color
from index.styles.styles import Size, MAX_WIDTH, APARECE
import index.styles.styles as styles

def link_button(title: str, body: str, url: str, image:str, is_external=True, animated=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.image(src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin = Size.MEDIUM.value,
                    color= Color.PRIMARY.value,
                    alt=title),
            rx.vstack(
                    rx.text(title, style= BOTTON_TITLE_STYLE,width= "100%"),
                    rx.text(body, style= BOTTON_BODY_STYLE,width= "100%"),
                    spacing="0",
            align="start",
            width= "100%",
            autofocus=True),
            class_name=APARECE),
        is_external=is_external,
        href=url,
        width="100%"
    )
    




def mi_boton_animado() -> rx.Component:
    return rx.button(
        "Contenido del botón",
        class_name="mi-elemento animate__animated animate__flip",  # Clase de animación inicial
    )

# Agrega más componentes y animaciones según tu diseño



def manejar_scroll() -> None:
    elementos_animados = rx.find(".mi-elemento")  # Encuentra los elementos con la clase "mi-elemento"
    for elemento in elementos_animados:
        rect = elemento.getBoundingClientRect()
        es_visible = rect.top < rx.window.innerHeight()  # Compara con la altura de la ventana
        if es_visible:
            elemento.add_class("animate__fadeIn")  # Agrega la clase de animación

# Agrega más componentes y animaciones según tu diseño
