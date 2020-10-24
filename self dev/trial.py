from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):

    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

    def build(self):
        img = Image(source='C:/Users/messi/Pictures/samurai.jpg',
                    size_hint=(.5,1),
                    pos_hint={'bottom_x':0, 'bottom_y':0 })
        return img

if __name__ == '__main__':
    MainApp().run()
