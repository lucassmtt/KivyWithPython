# coding: utf-8


from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label()


app = MyApp()
app.run()
