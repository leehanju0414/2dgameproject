from pico2d import *
import game_world
import game_framework
import end_state

class Protector:
    def __init__(self):
        self.tenhp_image = load_image('image_source/protector_10.png')
        self.ninehp_image = load_image('image_source/protector_9.png')
        self.eighthp_image = load_image('image_source/protector_8.png')
        self.sevenhp_image = load_image('image_source/protector_7.png')
        self.sixhp_image = load_image('image_source/protector_6.png')
        self.fivehp_image = load_image('image_source/protector_5.png')
        self.fourhp_image = load_image('image_source/protector_4.png')
        self.threehp_image = load_image('image_source/protector_3.png')
        self.twohp_image = load_image('image_source/protector_2.png')
        self.onehp_image = load_image('image_source/protector_1.png')
        self.hp = 100
        self.x, self.y = 300, 100

    def update(self):
        # if self.hp == 0:
        #     game_world.remove_object(self)
        if self.hp == 0:
            game_world.remove_object(self)
            game_framework.change_state(end_state)

    def draw(self):
        if self.hp == 100:
            self.tenhp_image.draw(self.x, self.y)
        elif self.hp == 90:
            self.ninehp_image.draw(self.x, self.y)
        elif self.hp == 80:
            self.eighthp_image.draw(self.x, self.y)
        elif self.hp == 70:
            self.sevenhp_image.draw(self.x, self.y)
        elif self.hp == 60:
            self.sixhp_image.draw(self.x, self.y)
        elif self.hp == 50:
            self.fivehp_image.draw(self.x, self.y)
        elif self.hp == 40:
            self.fourhp_image.draw(self.x, self.y)
        elif self.hp == 30:
            self.threehp_image.draw(self.x, self.y)
        elif self.hp == 20:
            self.twohp_image.draw(self.x, self.y)
        elif self.hp == 10:
            self.onehp_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 300, self.y - 25, self.x +300, self.y + 25

    def handle_collision(self, other, group):
        if group == 'monster:protector':
            self.hp -= 10