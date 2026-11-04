import raylib as rl
from pyray import *

class Player:
    def __init__ (self, textures, pos_x, pos_y, speed, texture_scale):
        self.textures = textures
        self.texture = textures['down']
        self.pos = Vector2(pos_x, pos_y)
        self.speed = speed
        self.texture_scale = texture_scale
        self.direction = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def process_input (self):
        self.direction.x = (is_key_down(rl.KEY_RIGHT) - is_key_down(rl.KEY_LEFT))
        self.direction.y = (is_key_down(rl.KEY_DOWN) - is_key_down(rl.KEY_UP))
        self.direction = vector2_normalize(self.direction) if (self.direction.x != 0) or (self.direction.y != 0) else self.direction

    def update (self, dt, world_bounds: Rectangle):
        # texture
        if self.direction.x != 0 or self.direction.y != 0:
            if abs(self.direction.y) > abs(self.direction.x):
                if self.direction.y > 0:
                    self.texture = self.textures['down']
                else:
                    self.texture = self.textures['up']
            else:
                if self.direction.x > 0:
                    self.texture = self.textures['right']
                else:
                    self.texture = self.textures['left']

        # position
        velocity = vector2_scale(self.direction, self.speed * dt)
        self.pos = vector2_add(self.pos, velocity)
        self.pos.x = clamp(self.pos.x, world_bounds.x, world_bounds.width - self.texture.width * self.texture_scale)
        self.pos.y = clamp(self.pos.y, world_bounds.y, world_bounds.height - self.texture.height * self.texture_scale)

    def draw (self):
        draw_texture_ex(self.texture, self.pos, 0, self.texture_scale, WHITE)