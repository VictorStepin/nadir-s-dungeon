import raylib as rl
from pyray import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

text_pos_x, text_pos_y = 10, 10

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text('Hello! We\'re about to start a great adventure!', text_pos_x, text_pos_y, 20, DARKGRAY)
    end_drawing()

close_window()