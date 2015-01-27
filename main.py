#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.image import Image


class Tile(Widget):
    def __init__(self,**kwargs):

        self.grid_x = kwargs['grid_x']
        self.grid_y = kwargs['grid_y']
        self.gridparent = kwargs['caller']
        self.img = "assets/tileSand.png"

        super(Tile, self).__init__(**kwargs)

        # Diferencia amb el centre, segons el que mourem horitzontalment les diferents files
        dif = self.grid_y-int(self.gridparent.gridsize/2)
        offset = 32*dif

        # posicio final, tenint en compte que y=0 està abaix, girem vertricalment
        # perque tingui sentit amb l'array guardada
        self.pos = offset+self.grid_x*65,(self.gridparent.gridsize-self.grid_y-1)*50

    # TODO: Aqui algo no va bien...
    def on_touch_up(self, touch):
        localtouch = self.to_local(*touch.pos)
        if self.collide_point(*localtouch):
            print self.grid_y,self.grid_x,localtouch
            return True

class HexGrid(ScatterLayout):
    def __init__(self,**kwargs):
        super(HexGrid, self).__init__(do_rotation=False,scale_min=.5, scale_max=3.)
        self.gridsize = kwargs['gridsize']

        # Nomes gridsize inparell
        assert(self.gridsize%2 != 0)
        
        self.grid = []
        self.pos = 10,10
        self.size = self.gridsize*65,89+(int(self.gridsize/2)*(35+65))
        self.setup()

    def setup(self):
        # Crea la capa de sota, de sorra
        sz = self.gridsize
        mid = int(sz/2)
        for y in range(0,sz):
            line = []
            dif = abs(mid-y)
            for x in range(0,sz):
                if y==mid or (y < mid and x >= dif) or (y>mid and x<sz-dif):
                    line.append('s')
                    # Graphics
                    t = Tile(grid_x = x, grid_y = y, caller = self, content = 's')
                    self.add_widget(t) # tile, zindex
                else:
                    line.append(None)
            self.grid.append(line)


class HexlandGame(Widget):

    def setup(self):
        self.grid = HexGrid(gridsize = 5)
        self.add_widget(self.grid)



class HexlandApp(App):
    def build(self):
    	game = HexlandGame()
    	game.setup()
        return game


if __name__ == '__main__':
    HexlandApp().run()
