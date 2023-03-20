#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    return TextInput(text="Componente Text Input")


def print_text_input(text):
    print(text)


window = App()
window.build = build
window.run()