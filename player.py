import raylib as rl
from pyray import *

class Player:
    def __init__ (self, pos_x, pos_y, radius, color, speed):
        self.pos = Vector2(pos_x, pos_y)
        self.radius = radius
        self.color = color
        self.speed = speed
        self.direction = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def process_input (self):
        self.direction.x = (is_key_down(rl.KEY_RIGHT) - is_key_down(rl.KEY_LEFT))
        self.direction.y = (is_key_down(rl.KEY_DOWN) - is_key_down(rl.KEY_UP))
        self.direction = vector2_normalize(self.direction) if (self.direction.x != 0) or (self.direction.y != 0) else self.direction

    def update (self, dt, world_bounds: Rectangle):
        velocity = vector2_scale(self.direction, self.speed * dt)
        self.pos = vector2_add(self.pos, velocity)
        self.pos.x = clamp(self.pos.x, world_bounds.x + self.radius, world_bounds.x + world_bounds.width - self.radius)
        self.pos.y = clamp(self.pos.y, world_bounds.y + self.radius, world_bounds.y + world_bounds.height - self.radius)

    def draw (self):
        draw_circle_v(self.pos, self.radius, self.color)