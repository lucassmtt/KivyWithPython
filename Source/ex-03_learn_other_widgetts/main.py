#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button


def click():
    print('O botão foi clicado!')


def build():
    btn = Button()
    btn.text = 'Aperte o botão'
    btn.font_size = 20
    btn.on_press = click

    return btn


window = App()
window.build = build
window.run()