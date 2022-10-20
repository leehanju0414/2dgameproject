from pico2d import *
import game_framework
import Attack
import Monster



class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def draw(self):
        self.image.draw(300,450)


class Gunner:
    global head, shoot
    def __init__(self):
        self.x, self.y = 300, 30
        self.framea, self.frameb, self.framec = 1, 1, 1
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
        if self.dir == 1 and shoot == 0:
            self.image.clip_draw(self.frameb*35, 465, 35, 35, self.x, self.y+15, 50, 50)
            self.image.clip_draw(self.framec*35, 430, 35, 35, self.x, self.y, 50, 50)
        elif self.dir == -1 and shoot == 0:
            self.image.clip_draw(self.frameb * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.framec * 35, 290, 35, 35, self.x, self.y)
        elif self.dir == 0 and head == 0 and shoot == 0:
            self.image.clip_draw(self.framec * 35, 80, 35, 70, self.x, self.y+10)
        elif self.dir == 0 and head == 1 and shoot == 0:
            self.image.clip_draw(self.framec * 35, 150, 35, 70, self.x, self.y+10)
        elif shoot == 1 and head == 0:
            self.image.clip_draw(self.framea*35, 220, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.framec*35, 290, 35, 35, self.x, self.y)
        elif shoot == 1 and head == 1:
            self.image.clip_draw(self.framea*35, 360, 35, 70, self.x, self.y+30)
            self.image.clip_draw(self.framec*35, 430, 35, 35, self.x, self.y)


def handle_events():
    global cdir, head, shoot # head=머리 방향

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
                bullets.append(Attack.Bullet())
            elif event.key == SDLK_SPACE:
                monsters.append(Monster.Normal())

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                gunner.dir -= 1
            elif event.key == SDLK_LEFT:
                gunner.dir += 1
            elif event.key == SDLK_LCTRL:
                shoot -= 1


gunner = None
background = None
bullets = []
monsters = []
head = 1
shoot = 0

def enter():
    global gunner, background, monsters
    gunner = Gunner()
    background = Background()

def exit():
    global gunner, background
    del gunner
    del background
    for bullet in bullets:
        del bullet
    for monster in monsters:
        del monster

def update():
    gunner.update()
    for bullet in bullets:
        if bullet.y > 900:
            bullets.remove(bullet)
        bullet.update()
    for monster in monsters:
        monster.update()


def draw_world():
    background.draw()
    gunner.draw()
    for bullet in bullets:
        bullet.draw()
    for monster in monsters:
        monster.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.03)

