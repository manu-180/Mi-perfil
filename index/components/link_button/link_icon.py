import reflex as rx
from index.styles.styles import Size

def link_icon(url:str, image:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
            margin = Size.VERY_SMALL.value,
            alt=alt
        ), 
        href= url,
        is_external= True
)