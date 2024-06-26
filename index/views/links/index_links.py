import reflex as rx 
from index.components.link_button.link_button import link_button
from index.constants.constants import *
from index.views.routers import Route
from index.styles.styles import APARECE


def index_links() -> rx.Component:
    return rx.vstack(
        link_button("likedIn", "Programador backend", LINKEDIN_URL,"/imagen_icon/linkedin-in.svg"),
        link_button("Instagram","Tormenta de facha", IG_URL,"/imagen_icon/instagram.svg"),
        link_button("Gmail","manuelnavarro@baakend.com", "https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcRwRdqSjkhHNlRzLqlTGwVTwRNHwTfQwXCWghLDmhCxqJcBQGLCJLxFfCqwWNbzRgrmVsZsz","/imagen_icon/envelope-regular.svg"),
        link_button("twitter", "No tengo", "https://twitter.com/Inicio/","/imagen_icon/twitter.svg"),
        link_button("Mis estudios","1 año de estudio",Route.Courses.value,"imagen_icon/book-solid.svg", is_external=False),
        link_button("Curriculum Vitae", "Contratenme", "/cv","/imagen_icon/file-regular.svg"),
        width = "100%",
        class_name=APARECE
    )