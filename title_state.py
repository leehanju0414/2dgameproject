from pico2d import *
import game_framework
import play_state

class Logo:

    def __init__(self):
        self.image = load_image('title.png')

    def draw(self):
        self.image.draw(300, 450)


logo = None

def enter():
    global logo
    logo = Logo()

def exit():
    global logo
    del logo

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_state(play_state)

def draw():
    clear_canvas()
    logo.draw()
    update_canvas()