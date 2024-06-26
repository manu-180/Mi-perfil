import reflex as rx 

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon = rx.image(src="/imagen_icon/donate.svg")
    
    
float_button = FloatButton.create