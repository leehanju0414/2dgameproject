from pico2d import *
import game_framework


class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def draw(self):
        self.image.draw(300,450)

class Gunner:
    global cdir, head
    def __init__(self):
        self.x, self.y = 300, 30
        self.frame = 0
        self.dir = 0
        self.image = load_image('gunner_image.png')

    def update(self, imgcnt):
        self.frame = (self.frame + 1) % imgcnt

        if cdir == -1:
            self.dir = -1
            if 0 < self.x - 1 < 600:
                self.x += self.dir * 1
                print(self.x)
        elif cdir == 1:
            self.dir = 1
            if 0 < self.x + 1 < 600:
                self.x += self.dir * 1
                print(self.x)
        elif cdir == 0:
            self.dir = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*35, 465, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame*35, 430, 35, 35, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame * 35, 290, 35, 35, self.x, self.y)
        elif self.dir == 0 and head == 0:
            self.image.clip_draw(self.frame * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame * 35, 290, 35, 35, self.x, self.y)
        elif self.dir == 0 and head == 1:
            self.image.clip_draw(self.frame * 35, 465, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame * 35, 430, 35, 35, self.x, self.y)


def handle_events():
    global cdir, head # 머리 방향
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_LEFT:
                head = 0 # 왼쪽
                cdir -= 1
            elif event.key == SDLK_RIGHT:
                head = 1 # 오른쪽
                cdir += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                cdir -= 1
            elif event.key == SDLK_LEFT:
                cdir += 1

gunner = None
background = None
cdir = 0
head = 1

def enter():
    global gunner, background
    gunner = Gunner()
    background = Background()

def exit():
    global gunner, background
    del gunner
    del background

def update():
    gunner.update(8)

def draw():
    clear_canvas()
    background.draw()
    gunner.draw()
    update_canvas()