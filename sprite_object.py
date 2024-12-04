from PIL import Image
import os
from collections import deque
import pygame as pg
import math
from settings import*

class SpriteObject:
    def __init__(self, game, path, pos=(2.5, 2.5), scale=0.5, shift=0.3):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = self.load_image(path)
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def load_image(self, path, res=(64, 64)):
        image = Image.open(path).convert("RGBA")
        return image.resize(res)

    def get_sprite_projection(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist

        sprite_angle = math.atan2(dy, dx) - self.player.angle

        if -HALF_FOV < sprite_angle < HALF_FOV:
            proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
            proj_width, proj_height = proj, proj

            x_offset = math.tan(sprite_angle) * SCREEN_DIST
            x = HALF_WIDTH + x_offset - proj_width / 2
            y = HALF_HEIGHT - proj_height / 2 + proj_height * self.SPRITE_HEIGHT_SHIFT

            self.game.raycasting.objects_to_render.append((self.norm_dist, self.image, (x, y)))

    def update(self):
        self.get_sprite_projection()

class AnimatedSprite(SpriteObject):
    def __init__(self, game, path, pos=(2.5, 2.5), scale=0.5, shift=0.3, animation_time=200):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.images = self.get_images(path)
        self.image = self.images[0]
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        self.check_animation_time()
        if self.animation_trigger:
            self.images.rotate(-1)
            self.image = self.images[0]
        super().update()

    def check_animation_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True
        else:
            self.animation_trigger = False

    def get_images(self, path):
        images = deque()
        directory = os.path.dirname(path)
        for file in os.listdir(directory):
            if file.endswith('.png'):
                img_path = os.path.join(directory, file)
                image = self.load_image(img_path)
                images.append(image)
        return images
