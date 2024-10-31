import pygame

GRAVITY = 0.5

class Player:
    def __init__(self, x, y, image_path, left_key, right_key, jump_key):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.left_key = left_key
        self.right_key = right_key
        self.jump_key = jump_key
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def move(self, keys):
        self.vel_x = 0
        if keys[self.left_key]:
            self.vel_x = -5
        if keys[self.right_key]:
            self.vel_x = 5
        if keys[self.jump_key] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Ground collision
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.vel_y = 0
            self.on_ground = True

        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
