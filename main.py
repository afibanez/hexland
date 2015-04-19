#!/usr/bin/env python#:include button.kv
# -*- coding: utf-8 -*-

__version__ = "0.0.1"

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation

from hexgrid import HexGame
from menu import Menu, NewMenu

class HexlandGame(Widget):

    def __init__(self, **kwargs):
        super(HexlandGame, self).__init__(**kwargs)

        # self.add_widget(HexGame(gridsize = 5))
        self.add_widget(Menu())

    def setup(self):

        def complete(anim,widget):
            self.clear_widgets()
            self.add_widget(NewMenu(opacity=0))
            Animation(d=0.5,opacity=1).start(self.getCurrentScreenWidget())

        anim = Animation(d=0.5,opacity=0)
        anim.bind(on_complete=complete)
        anim.start(self.getCurrentScreenWidget())

    def start(self,size,state=None):

        def complete(anim,widget):
            self.clear_widgets()
            self.add_widget(HexGame(d=0.5,opacity=0,gridsize=size,state=state))
            Animation(opacity=1).start(self.getCurrentScreenWidget())

        anim = Animation(d=0.5,opacity=0)
        anim.bind(on_complete=complete)
        anim.start(self.getCurrentScreenWidget())

    def gameOver(self):

        def complete(anim,widget):
            self.clear_widgets()
            self.add_widget(Menu())
            Animation(opacity=1).start(self.getCurrentScreenWidget())

        anim = Animation(d=0.5,opacity=0)
        anim.bind(on_complete=complete)
        anim.start(self.getCurrentScreenWidget())

    def getCurrentScreenWidget(self):
        return self.children[0]

class HexlandApp(App):
    def build(self):
        game = HexlandGame()
        return game


if __name__ == '__main__':
    HexlandApp().run()
