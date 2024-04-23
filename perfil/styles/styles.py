import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from perfil.styles.fuentes import Font, FontWeight
import perfil.styles.styles as styles

MAX_WIDTH= "560px"
APARECE = "animate__animated animate__fadeInUp"
REBOTAR = "animate__animated animate__bounceInDown"

STELESHEWTS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Confortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]

class Size(Enum):
    ZERO = "0px"
    VERY_SMALL = "0.3em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE ="1.3em"
    BIG="2em"
    VERY_BIG="4em"
    
animated = False
    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGTH.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}
    


NAVBAR_STYLE= dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value,
    position="sticky",
    bg=Color.CONTENT.value,
    padding_y=Size.SMALL.value,
    padding_x=Size.SMALL.value,
    z_index="999",
    top="0"    
)

BOTTON_TITLE_STYLE = dict(
    font_family = Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    margin_top = Size.MEDIUM.value,
)

BOTTON_BODY_STYLE = dict(
    font_family = Font.DEFAULT.value,
    font_weight= FontWeight.LIGTH.value,
    font_size = Size.MEDIUM.value,
    margin_bottom = Size.MEDIUM.value,
    color = TextColor.BODY.value,

)

TITLE_STYLE = dict(
    font_family = Font.DEFAULT.value,
    font_weight= FontWeight.LIGTH.value,
    padding_y=Size.SMALL.value,
    color = TextColor.HEADER.value,
    letter_spacing = "-0.1em"
)

PADING_MARGIN_0 = dict(
    margin= Size.ZERO.value,
    padding = Size.ZERO.value
)