from pico2d import *
import game_framework
from Attack import Bullet
from Monster import Normal
from Player import Gunner
import game_world


class Background:
    def __init__(self):
        self.image = load_image('metal_background.png')

    def update(self):
        pass

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
                    bullets.append(Bullet())

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
    global gunner, background, bullets
    gunner = Gunner()
    background = Background()
    bullets = Bullet()
    game_world.add_object(background, 0)
    game_world.add_object(gunner, 1)
    bullets = [Bullet() for i in range(20)]
    game_world.add_object(bullets, 1)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.03)

def monster_add():
    monsters.append(Normal())

