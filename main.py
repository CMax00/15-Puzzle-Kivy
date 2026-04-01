import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):

    def build(self):
        layout = GridLayout(cols=4, rows=4, spacing=10, padding=20)

        for i in range(15):
            btn = Button(text=str(i+ 1), font_size=32)
            layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    MyApp().run()