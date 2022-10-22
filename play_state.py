from pico2d import *
import game_framework
import Attack
import Monster
import Player


class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def draw(self):
        self.image.draw(300, 450)

def handle_events():
    global cdir, head, shoot # head=머리 방향

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_LEFT:
                    head = 0 # 왼쪽
                    gunner.dir -= 1
                case pico2d.SDLK_RIGHT:
                    head = 1 # 오른쪽
                    gunner.dir += 1
                case pico2d.SDLK_LCTRL:
                    shoot += 1
                    bullets.append(Attack.Bullet())
                case pico2d.SDLK_SPACE:
                    monster_add()

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
    global gunner, background
    gunner = Player.Gunner()
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

def monster_add():
    monsters.append(Monster.Normal())

