from pico2d import *
import game_framework
import play_state
import title_state
from Player import Gunner

image = None

def enter():
    global image
    image = load_image('image_source/pause.png')

def exit():
    global image
    del image
    gunner = Gunner()
    gunner.cur_state.enter(gunner, None)

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(300, 450)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_0:
                game_framework.pop_state()
                game_framework.change_state(title_state)