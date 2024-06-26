import reflex as rx
from index.styles.styles import BOTTON_TITLE_STYLE, BOTTON_BODY_STYLE
from index.styles.styles import Size, Color




def box(title, body, image)-> rx.Component:
    return rx.box(
        rx.hstack(
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
            autofocus=True)
            ),
        style={
                "height":"100%",
                "width":"100%", 
                "color" : "white",
                "border_radius":Size.DEFAULT.value,
                "opacity": "0.5",
                "white_space": "normal",
                "_hover": {
                "background_color": Color.CONTENT.value,
                "opacity": "1",
                "transition": "opacity 0.6s ease"},
                "transition": "background-color 1s ease"}
        )