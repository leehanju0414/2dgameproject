from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 450)