import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Draw(Widget):

    def __init__(self, **kwargs):
        super(Draw, self).__init__(**kwargs)

        with self.canvas:
            Color(0 , 1, 1, 0.5, mode='rgba')
            Line(points=(400, 550, 60, 420, 20, 250))
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        pass

class DrawApp(App):
    def build(self):
        return Draw()

if __name__ == "__main__":
    DrawApp().run()