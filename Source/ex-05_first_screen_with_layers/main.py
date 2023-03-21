# coding: utf-8


from kivy.app import App
from kivy.app import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def click_callback():
    print(input_text.text)


def build():
    layout = FloatLayout()

    input_text = TextInput(text='My name is: ')
    input_text.size_hint = None, None
    input_text.height = 300
    input_text.width = 300
    input_text.y = 60
    input_text.x = 250



    btn = Button(text='Click-me')
    btn.size_hint = None, None
    btn.height = 100
    btn.width = 100
    btn.y = 270
    btn.x = 360
    btn.on_press = click_callback


    layout.add_widget(input_text)
    layout.add_widget(btn)

    return layout


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.size = 600, 600
    app = App()

    app.build = build
    app.run()