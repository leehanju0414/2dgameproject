from pico2d import *

import play_state


class Gunner:
    global head, shoot
    def __init__(self):
        self.x, self.y = 300, 30
        self.framea, self.frameb, self.framec = 0, 0, 0
        self.dir = 0
        self.image = load_image('gunner_image.png')

    def update(self):

        self.framea = (self.framea + 1) % 10
        self.frameb = (self.frameb + 1) % 12
        self.framec = (self.framec + 1) % 16

        if self.dir == -1:
            if 0 < self.x - 1 < 600:
                self.x += self.dir * 5
        elif self.dir == 1:
            if 0 < self.x + 1 < 600:
                self.x += self.dir * 5
        else: self.dir = 0

    def draw(self):
        if self.dir == 1 and play_state.shoot == 0:
            self.image.clip_draw(self.frameb*35, 465, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.framec*35, 430, 35, 35, self.x, self.y)
        elif self.dir == -1 and play_state.shoot == 0:
            self.image.clip_draw(self.frameb * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.framec * 35, 290, 35, 35, self.x, self.y,)
        elif self.dir == 0 and play_state.head == 0 and play_state.shoot == 0:
            self.image.clip_draw(self.framec * 35, 80, 35, 70, self.x, self.y+10)
        elif self.dir == 0 and play_state.head == 1 and play_state.shoot == 0:
            self.image.clip_draw(self.framec * 35, 150, 35, 70, self.x, self.y+10)
        elif play_state.shoot == 1 and play_state.head == 0:
            self.image.clip_draw(self.framea*35, 220, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.framec*35, 290, 35, 35, self.x, self.y)
        elif play_state.shoot == 1 and play_state.head == 1:
            self.image.clip_draw(self.framea*35, 360, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.framec*35, 430, 35, 35, self.x, self.y)

