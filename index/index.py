import reflex as rx 
from index.styles.styles import BASE_STYLE, STELESHEWTS
from index.pages.index import index
from index.pages.courses import courses
from index.pages.curriculum import cv


app = rx.App(
    style=BASE_STYLE,
    stylesheets=STELESHEWTS
    )

app.add_page(index)