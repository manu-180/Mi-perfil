import reflex as rx 
from perfil.components.link_button.link_button import link_button
from perfil.constants.constants import *
from perfil.views.routers import Route
from perfil.components.box import box
from perfil.styles.styles import APARECE

def courses_links() -> rx.Component:
    return rx.box(
        rx.vstack(
        box("Python", "Lenguaje orientado a objetos" ,"/imagen_icon/python.svg"),
        box("PromptEngineering", "Inteligencia artificial" ,"/imagen_icon/microchip-solid.svg"),
        box("SQL","Base de datos relacionales","/imagen_icon/database-solid.svg"),
        box("MongoDB","Base de datos no relacionales","/imagen_icon/envira.svg"),
        box("Reflex", "Framework","/imagen_icon/favicon.ico"),
        width = "100%",
        class_name=APARECE
    ),width="100%")