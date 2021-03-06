#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


# CONSTANTS
GAMETYPE = {
    'PVP': 0,
    'IA_DUMMY': 1,
    'IA_EASY': 2
}


# Permet detectar colisio sobre qualsevol poligon
# poly es una llista de parelles (x,y), punts formant el poligon
def point_inside_polygon(x, y, poly):
    '''Source: http://www.ariel.com.au/a/python-point-int-poly.html'''
    n = len(poly)
    inside = False
    p1x = poly[0]
    p1y = poly[1]
    for i in range(0, n + 2, 2):
        p2x = poly[i % n]
        p2y = poly[(i + 1) % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def playClickSound():
    sound = SoundLoader.load('assets/click.ogg')
    if sound:
        sound.play()

def launchSimpleModal(text):
    view = ModalView(size_hint=(0.4, 0.2))
    content = SimpleModal(text=text)
    view.add_widget(content)
    # bind the on_press event of the button to the dismiss function
    content.bind(on_press=view.dismiss)
    # open the view
    view.open()

class SimpleModal(Button):
    pass


