#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.8.0"

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

from hexgrid import HexGame
from menu import Menu, NewMenu, Help, Credits
from utils import playClickSound

class HexlandGame(Widget):

    def __init__(self, **kwargs):
        super(HexlandGame, self).__init__(**kwargs)

        #self.add_widget(HexGame(gridsize = 5,gametype=2,state=None))
        self.add_widget(Menu())

    def setup(self):
        self.changeScreen(NewMenu())

    def start(self,size,vs,state=None):
        self.changeScreen(HexGame(gridsize=size,gametype=vs,state=state),0)

    def gameOver(self):
        self.changeScreen(Menu())

    def help(self):
        self.changeScreen(Help())

    def credits(self):
        self.changeScreen(Credits())

    def changeScreen(self,nextScreen,enterDuration=0.5):

        def complete(anim,widget):
            self.clear_widgets()
            nextScreen.opacity = 0
            self.add_widget(nextScreen)
            Animation(d=enterDuration,opacity=1).start(self.getCurrentScreenWidget())

        anim = Animation(d=0.5,opacity=0)
        anim.bind(on_complete=complete)
        anim.start(self.getCurrentScreenWidget())
        playClickSound()

    def getCurrentScreenWidget(self):
        return self.children[0]


class HexlandApp(App):
    def build(self):
        game = HexlandGame()
        self.playBSO()
        return game

    def on_pause(self):
        # no cal guardar res ja que es guarda automaticament
        return True

    def playClickSound(self):
        playClickSound()

    def playBSO(self):
        self.bso = SoundLoader.load('assets/serenity.mp3')
        if self.bso:
            self.bso.loop = True
            self.bso.volume = 0.7
            self.bso.play()


if __name__ == '__main__':
    HexlandApp().run()
