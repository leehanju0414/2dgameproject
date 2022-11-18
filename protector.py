from pico2d import *
import game_world

class Protector:
    def __init__(self):
        self.image = load_image('protector.png')
        self.hp = 100
        self.x, self.y = 300, 100

    def update(self):
        if self.hp == 0:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 300, self.y - 25, self.x +300, self.y + 25

    def handle_collision(self, other, group):
        self.hp -= 10