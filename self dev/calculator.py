import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class Layout(Widget):
    pass

class CalcApp(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    CalcApp().run()