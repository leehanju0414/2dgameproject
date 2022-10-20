from pico2d import *
import play_state
import random


class Normal:
    def __init__(self):
        self.x, self.y = 300, 899
        self.frame = 0
        self.mlv = 'MobLv1'
        self.mlv1_image = load_image('Lv1_monster.png')

    def update(self):
        self.frame = (self.frame + 1) % 12
        self.y -= 5

    def draw(self):
        self.mlv1_image.clip_draw = (self.frame*35, 0, 35, 35, self.x, self.y)
        #self.mlv1_image.draw(self.x, self.y)
