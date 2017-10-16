from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Test(App):
    def build(self):
        return Incrementador()

Test().run()
