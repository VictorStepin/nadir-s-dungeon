from pyray import *
from player import Player

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
PADDING = 5
WORLD_BOUNDS = Rectangle(PADDING, PADDING, WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 50, MAROON, 250.0)

while not window_should_close():
    fps = get_fps()
    dt = get_frame_time()

    # handle input
    player.process_input()
    
    # update
    player.update(dt, WORLD_BOUNDS)

    # draw
    begin_drawing()
    
    clear_background(RAYWHITE)

    player.draw()

    draw_text('Hello! We\'re about to start a great adventure!', 5, 10, 20, DARKGRAY)
    draw_text(f'FPS: {fps}', 5, 35, 20, DARKGRAY)
    draw_text(f'Frame time: {dt}', 5, 60, 20, DARKGRAY)
    
    end_drawing()

close_window()