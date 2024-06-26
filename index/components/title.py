import reflex as rx
from index.styles.styles import Size,TITLE_STYLE 
from index.styles.styles import Size, MAX_WIDTH, APARECE

def title(text:str) -> rx.Component:
    return rx.flex(
    rx.text(
        text,
        style=TITLE_STYLE,
        font_size=Size.BIG.value,
        class_name=APARECE
    ),
)
