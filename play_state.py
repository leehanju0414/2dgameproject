from pico2d import *
import game_framework
from Attack import Bullet
from monster import Normal
from background import Background
from Player import Gunner
import game_world


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            gunner.handle_event(event)



gunner = None
background = None
monster = None
bullet = None
timer = 0

def enter():
    global gunner, background, monster, bullet, timer
    gunner = Gunner()
    background = Background()
    monster = Normal()
    bullet = Bullet(gunner.x, gunner.y+30, 2)

    timer = 1000

    game_world.add_object(background, 0)
    game_world.add_object(gunner, 1)

    game_world.add_collision_pairs(monster, bullet, 'monster:bullet')


def exit():
    game_world.clear()

def update():
    global timer, monster
    for game_object in game_world.all_objects():
        game_object.update()
    timer -= 1
    if timer == 0:
        game_world.add_object(monster, 1)

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)




def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb : return False
    if ra < lb : return False
    if ta < bb : return False
    if ba > tb : return False

    return True
