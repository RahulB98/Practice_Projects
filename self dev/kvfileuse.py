import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("name: ", self.name.text, "email: ", self.email.text)
        self.name.text = ""
        self.email.text = ""

    pass

class YoApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    YoApp().run()
