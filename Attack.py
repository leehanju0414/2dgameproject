from pico2d import *
import game_world

class Bullet:
    image = None
    def __init__(self, x, y, v):
        if Bullet.image == None:
            Bullet.image = load_image('image_source/Blv1.png')
        self.x, self.y, self.v = x, y, v

    def draw(self):
        self.image.draw(self.x, self.y, 10, 10)

    def update(self):
        self.y += self.v

        if self.y > 900:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x +5, self.y + 5

    def handle_collision(self, other, group):
        if group == 'monster:bullet':
            game_world.remove_object(self)

