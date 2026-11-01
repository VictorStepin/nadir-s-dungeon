from pyray import *
from player import Player

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WORLD_BOUNDS = Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
TEXTURE_SCALE = 4

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

pos = Vector2(WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2)
player_texture = load_texture('assets\\player.png')

player = Player(player_texture,
                WINDOW_WIDTH / 2 - (player_texture.width / 2) * TEXTURE_SCALE,
                WINDOW_HEIGHT / 2 - (player_texture.height / 2) * TEXTURE_SCALE,
                300, TEXTURE_SCALE)

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

    #draw_texture_ex(player_texture, pos, 0, 4, WHITE)

    player.draw()

    draw_text('Hello! We\'re about to start a great adventure!', 5, 10, 20, DARKGRAY)
    draw_text(f'FPS: {fps}', 5, 35, 20, DARKGRAY)
    draw_text(f'Frame time: {dt}', 5, 60, 20, DARKGRAY)
    
    end_drawing()

close_window()