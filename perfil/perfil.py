import reflex as rx 
from perfil.styles.styles import BASE_STYLE, STELESHEWTS
from perfil.pages.index import index
from perfil.pages.courses import courses
from perfil.pages.curriculum import cv


app = rx.App(
    style=BASE_STYLE,
    stylesheets=STELESHEWTS
    )
