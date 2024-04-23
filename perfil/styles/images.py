import reflex as rx
from perfil.styles.styles import Size, BASE_STYLE


class Imagen(rx.State):
    valor:int = 0

    realogo:str = "/Realogo.jpeg"
    mangekyo:str = "/mangekyo.jpeg"
    humanoide:str= "/humanoide.jpeg"
    logocelu:str = "/LogoCelu.jpeg"
    
    def cambiar_imagen(self):
        
        if self.valor != 1:
            if self.realogo== "/Realogo.jpeg":
                self.realogo = "/mangekyo.jpeg"
            elif self.realogo == "/mangekyo.jpeg":
                self.realogo= "/humanoide.jpeg"
            elif self.realogo =="/humanoide.jpeg":
                self.realogo="/LogoCelu.jpeg"
                self.valor += 1
                print(BASE_STYLE["background_color"])
            elif self.realogo == "/LogoCelu.jpeg":
                self.realogo="/Realogo.jpeg"
        else : 
            self.valor = 0
            return rx.window_alert("QUE TOCAS MIS LOGOS GATO!")