import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super()

class MyApp(App):
    def build(self):
        return Label(text="Hello! I'm learning Kivy")
    


if __name__ == '__main__':
    MyApp().run()