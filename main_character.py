from pico2d import *
import game_framework


class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def draw(self):
        self.image.draw(300,450)

class Bullet:
    global shoot
    def __init__(self):
        self.x, self.y = gunner.x, gunner.y+70
        self.blv = 'Blv1'
        self.image = load_image('Blv1.png')

    def update(self):
        if self.y < 900:
            self.y += 1

    def draw(self):
        if self.blv == 'Blv1' and shoot == 1:
            self.image.draw(gunner.x, self.y)

class Gunner:
    global head, shoot
    def __init__(self):
        self.x, self.y = 300, 30
        self.frame = 0
        self.dir = 0
        self.image = load_image('gunner_image.png')

    def update(self, imgcnt):
        self.frame = (self.frame + 1) % imgcnt

        if self.dir == -1:
            if 0 < self.x - 1 < 600:
                self.x += self.dir * 1
        elif self.dir == 1:
            if 0 < self.x + 1 < 600:
                self.x += self.dir * 1
        else: self.dir = 0

    def draw(self):
        if self.dir == 1 and shoot == 0:
            self.image.clip_draw(self.frame*35, 465, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame*35, 430, 35, 35, self.x, self.y)
        elif self.dir == -1 and shoot == 0:
            self.image.clip_draw(self.frame * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame * 35, 290, 35, 35, self.x, self.y)
        elif self.dir == 0 and head == 0 and shoot == 0:
            self.image.clip_draw(self.frame * 35, 80, 35, 70, self.x, self.y+10)
        elif self.dir == 0 and head == 1 and shoot == 0:
            self.image.clip_draw(self.frame * 35, 150, 35, 70, self.x, self.y+10)
        elif shoot == 1 and head == 0:
            self.image.clip_draw(self.frame*35, 220, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.frame*35, 290, 35, 35, self.x, self.y)
        elif shoot == 1 and head == 1:
            self.image.clip_draw(self.frame*35, 360, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.frame*35, 430, 35, 35, self.x, self.y)

def handle_events():
    global cdir, head, shoot # head=머리 방향

    bullet_xy = []

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_LEFT:
                head = 0 # 왼쪽
                gunner.dir -= 1
            elif event.key == SDLK_RIGHT:
                head = 1 # 오른쪽
                gunner.dir += 1
            elif event.key == SDLK_LCTRL:
                shoot += 1
            elif event.key == SDLK_1:
                pass

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                gunner.dir -= 1
            elif event.key == SDLK_LEFT:
                gunner.dir += 1
            elif event.key == SDLK_LCTRL:
                shoot -= 1

gunner = None
background = None
bullet = None
head = 1
shoot = 0
imgcnt = 8
def enter():
    global gunner, background, bullet
    gunner = Gunner()
    background = Background()
    bullet = Bullet()

def exit():
    global gunner, background, bullet
    del gunner
    del background
    del bullet

def update():
    gunner.update(imgcnt)
    bullet.update()

def draw():
    clear_canvas()
    background.draw()
    gunner.draw()
    bullet.draw()
    update_canvas()
