from pico2d import *
import game_world

class Bullet:
    image = None
    def __init__(self, x, y, v):
        if Bullet.image == None:
            Bullet.image = load_image('Blv1.png')
        self.x, self.y, self.v = x, y, v

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.v

        if self.y > 900:
            game_world.remove_object(self)
