from pico2d import *
import game_framework
from Attack import Bullet
from monster import Normal
from background import Background
from Player import Gunner
from protector import Protector
import game_world
import schedule


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
protector = None
timer = 0

def enter():
    global gunner, background, protector
    gunner = Gunner()
    background = Background()
    protector = Protector()

    game_world.add_object(background, 0)
    game_world.add_object(protector, 1)
    game_world.add_object(gunner, 1)

    game_world.add_collision_pairs(protector, None, 'monster:protector')


def exit():
    game_world.clear()

def update():
    schedule.run_pending()
    global timer, monster
    for game_object in game_world.all_objects():
        game_object.update()

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

def monsterspawn():
    monster = Normal()
    game_world.add_object(monster, 2)
    game_world.add_collision_pairs(None, monster, 'monster:bullet')
    game_world.add_collision_pairs(None, monster, 'monster:protector')


schedule.every(1).seconds.do(monsterspawn)
