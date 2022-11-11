from pico2d import *
import play_state
from Attack import Bullet
import game_world


RD, LD, RU, LU, SD, SU= range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'SD', 'SU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_LCTRL): SD,
    (SDL_KEYUP, SDLK_LCTRL): SU
}

class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    def exit(self, event):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 35, 150, 35, 70, self.x, self.y+10)
        else:
            self.image.clip_draw(self.frame * 35, 80, 35, 70, self.x, self.y+10)



class RUN:
    def enter(self, event):
        print('ENTER RUN')

        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 600)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 35, 325, 35, 35, self.x, self.y+15)
            self.image.clip_draw(self.frame * 35, 290, 35, 35, self.x, self.y,)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 35, 465, 35, 35, self.x, self.y + 15)
            self.image.clip_draw(self.frame * 35, 430, 35, 35, self.x, self.y)


class IDLE_SHOOT:
    def enter(self, event):
        print('ENTER SHOOT')
        self.dir = 0
        self.shooting()

    def exit(self, event):
        print('EXIT SHOOT')

    def do(self):
        print('shooting')
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 35, 360, 35, 70, self.x, self.y + 30)
            self.image.clip_draw(self.frame * 35, 430, 35, 35, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 35, 220, 35, 70, self.x, self.y + 30)
            self.image.clip_draw(self.frame*35, 290, 35, 35, self.x, self.y)

class RUN_SHOOT:
    def enter(self, event):
        print('ENTER SHOOT')
        self.shooting()

        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT SHOOT')

    def do(self):
        print('shooting')
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 600)

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 35, 360, 35, 70, self.x, self.y + 30)
            self.image.clip_draw(self.frame * 35, 430, 35, 35, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 35, 220, 35, 70, self.x, self.y + 30)
            self.image.clip_draw(self.frame*35, 290, 35, 35, self.x, self.y)


next_state = {
    IDLE:  {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SD: IDLE_SHOOT, SU: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SD: RUN_SHOOT, SU: RUN},
    IDLE_SHOOT: {RU: RUN_SHOOT, LU: RUN_SHOOT, RD: RUN_SHOOT, LD: RUN_SHOOT, SD: IDLE_SHOOT, SU: IDLE},
    RUN_SHOOT: {RU: IDLE_SHOOT, LU: IDLE_SHOOT, RD: IDLE_SHOOT, LD: IDLE_SHOOT, SD: RUN_SHOOT, SU: RUN}
}



class Gunner:

    def __init__(self):
        self.x, self.y = 300 // 2, 30
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('gunner_image.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR: ', self.cur_state, event_name[event])

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def shooting(self):
        print('shooting')
        bullet = Bullet(self.x, self.y+30, 2)
        game_world.add_object(bullet, 1)