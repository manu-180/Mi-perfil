import reflex as rx
import datetime
from index.styles.colors import TextColor
from index.styles.styles import Size, BASE_STYLE
from index.styles.images import Imagen
from index.styles.fuentes import Font
from index.styles.styles import Size, MAX_WIDTH, APARECE

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
        rx.text(f"2023-{datetime.datetime.now().year} Manuel Navarro diseñador web",
        margin_y = "0px",
        padding_y="0px"),
        rx.spacer(),
        color= TextColor.FOOTER.value,
        margin_y = "0px",
        padding_y="0px"
    ))
    
