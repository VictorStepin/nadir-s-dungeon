import raylib as rl
from pyray import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Nadir\'s Dungeon')
set_target_fps(60)

ball_pos = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
ball_velocity = Vector2(0, 0)
speed = 250.0
ball_radius = 50

while not window_should_close():
    fps = get_fps()
    dt = get_frame_time()

    # input handling
    ball_velocity.x = (is_key_down(rl.KEY_RIGHT) - is_key_down(rl.KEY_LEFT))
    ball_velocity.y = (is_key_down(rl.KEY_DOWN) - is_key_down(rl.KEY_UP))
    
    # update
    ball_velocity = vector2_clamp_value(ball_velocity, 0.0, 1.0)
    ball_velocity = vector2_scale(ball_velocity, speed * dt)
    ball_pos = vector2_add(ball_pos, ball_velocity)
    ball_pos.x = clamp(ball_pos.x, ball_radius, WINDOW_WIDTH - ball_radius)
    ball_pos.y = clamp(ball_pos.y, ball_radius, WINDOW_HEIGHT - ball_radius)

    # draw
    begin_drawing()
    
    clear_background(RAYWHITE)

    draw_circle_v(ball_pos, ball_radius, MAROON)

    draw_text('Hello! We\'re about to start a great adventure!', 5, 10, 20, DARKGRAY)
    draw_text(f'FPS: {fps}', 5, 35, 20, DARKGRAY)
    draw_text(f'Frame time: {dt}', 5, 60, 20, DARKGRAY)
    end_drawing()

close_window()