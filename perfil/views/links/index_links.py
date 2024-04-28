import reflex as rx 
from perfil.components.link_button.link_button import link_button
from perfil.constants.constants import *
from perfil.views.routers import Route
from perfil.styles.styles import APARECE


def index_links() -> rx.Component:
    return rx.vstack(
        link_button("likedIn", "Programador backend", "","/imagen_icon/linkedin-in.svg"),
        link_button("Instagram","Tormenta de facha", "","/imagen_icon/instagram.svg"),
        link_button("Gmail","manuelnavarro@baakend.com", "","/imagen_icon/envelope-regular.svg"),
        link_button("twitter", "No tengo", "","/imagen_icon/twitter.svg"),
        link_button("Mis estudios","1 año de estudio","","imagen_icon/book-solid.svg", is_external=False),
        link_button("Curriculum Vitae", "Contratenme", "","/imagen_icon/file-regular.svg"),
        width = "100%",
        class_name=APARECE
    )