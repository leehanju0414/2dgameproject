from pico2d import *
import play_state

class Bullet:
    global shoot, bullet
    def __init__(self):
        self.x, self.y = play_state.gunner.x, play_state.gunner.y+70
        self.blv = 'Blv1'
        self.blv1_image = load_image('Blv1.png')

    def update(self):
        self.y += 1

    def draw(self):
        if self.blv == 'Blv1':
            self.blv1_image.draw(self.x, self.y)
