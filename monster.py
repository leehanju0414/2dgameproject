from pico2d import *
from random import randint
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12


class Normal:
    image = None

    def monster_make(self):
        monster = Normal()
        game_world.add_object(monster, 1)


    def __init__(self):
        self.x, self.y = randint(50, 550), 850
        self.frame = 0
        self.dir = 0.5
        self.mlv = 'lv1'
        self.timer = 1000
        if Normal.image == None:
            Normal.image = load_image('Lv1_monster.png')

    def update(self):
        self.y -= self.dir
        self.timer -= 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if  self.timer == 0:
            self.monster_make()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 35, 0, 35, 49, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x +20, self.y + 25

    def handle_collision(self, other, group):
        pass
