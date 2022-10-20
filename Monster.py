from pico2d import *
import play_state
import random



spawn_x = 600

class Normal_mob:
    global spawn_x, monster
    def __init__(self):
        self.x, self.y = spawn_x, 900
        self.frame = 0
        self.mlv = 'MobLv1'
        self.mlv1_image = load_image('gunner_image.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.y -= 5

    def draw(self):
        if self.mlv == 'MobLv1':
            self.mlv1_image.clip_draw = (self.frame*35, 465, 35, 35, self.x, self.y, 50, 50)

class Boss_mob:
    def __init__(self):
        #self.image = load_image()
        pass
    def update(self):
        pass

    def draw(self):
        pass
