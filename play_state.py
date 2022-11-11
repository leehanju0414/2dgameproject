from pico2d import *
import game_framework
from Attack import Bullet
from Monster import Normal
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
monsters = []


def enter():
    global gunner, background
    gunner = Gunner()
    background = Background()
    game_world.add_object(background, 0)
    game_world.add_object(gunner, 1)

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

# def monster_add():
#     monsters.append(Normal())

