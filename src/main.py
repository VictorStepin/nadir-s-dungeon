from pyray import *
from player import Player

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WORLD_BOUNDS = Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
TEXTURE_SCALE = 4

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

pos = Vector2(WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2)
player_textures = {'down': [load_texture(f'assets\\player\\down\\player_down_{i}.png') for i in range(8)],
                   'up': [load_texture(f'assets\\player\\up\\player_up_{i}.png') for i in range(8)],
                   'left': load_texture('assets\\player_left.png'),
                   'right': load_texture('assets\\player_right.png')}

player = Player(player_textures,
                WINDOW_WIDTH / 2 - (player_textures['down'][0].width / 2) * TEXTURE_SCALE,
                WINDOW_HEIGHT / 2 - (player_textures['down'][0].height / 2) * TEXTURE_SCALE,
                200, TEXTURE_SCALE)

while not window_should_close():
    fps = get_fps()
    dt = get_frame_time()

    # handle input
    player.process_input()
    
    # update
    player.update(dt, WORLD_BOUNDS)

    # draw
    begin_drawing()
    
    clear_background(DARKGRAY)

    player.draw()

    draw_text('Never give up, bro!', 5, 10, 20, RAYWHITE)
    draw_text(f'FPS: {fps}', 5, 35, 20, RAYWHITE)
    draw_text(f'Frame time: {dt}', 5, 60, 20, RAYWHITE)
    
    end_drawing()

close_window()