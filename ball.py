import pygame

GRAVITY = 0.5

class Ball:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = 5
        self.vel_y = -5

    def update(self, players):
        self.vel_y += GRAVITY
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Collision with screen boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
            self.vel_x *= -1  # Reverse horizontal direction
        if self.rect.right >= 800:
            self.rect.right = 800
            self.vel_x *= -1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vel_y *= -1  # Reverse vertical direction
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.vel_y *= -0.9  # Simulate bounce with energy loss
            if abs(self.vel_y) < 1:
                self.vel_y = 0  # Stop bouncing if velocity is very low

        # Collision with players
        for player in players:
            if self.rect.colliderect(player.rect):
                # Simple collision response
                if self.rect.centery < player.rect.centery:
                    self.rect.bottom = player.rect.top
                    self.vel_y = -10  # Bounce upwards
                else:
                    self.rect.top = player.rect.bottom
                    self.vel_y = 10  # Bounce downwards
                # Adjust horizontal velocity based on collision side
                if self.rect.centerx < player.rect.centerx:
                    self.vel_x = -5
                else:
                    self.vel_x = 5
