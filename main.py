import raylib as rl
from pyray import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

while not window_should_close():
    dt = get_frame_time()
    
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text('Hello! We\'re about to start a great adventure!', 5, 10, 20, DARKGRAY)
    draw_text(f'FPS: {get_fps()}', 5, 35, 20, DARKGRAY)
    draw_text(f'Frame time: {dt}', 5, 60, 20, DARKGRAY)
    end_drawing()

close_window()