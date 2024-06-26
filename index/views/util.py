import reflex as rx


title_page="ManuNv | Desarrollador web"
description="Capacitandome diariamente"
image="corchetes.jpeg"

def lang() ->rx.Component:
    return rx.script("document.documentElement.lang='es'")