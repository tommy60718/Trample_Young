import pygame
from player import Player
from ball import Ball

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trample Young Game")

# Load background image
BG = pygame.image.load("assets/background.jpg")

# Game clock
clock = pygame.time.Clock()
FPS = 60

def draw_window(players, ball):
    WIN.blit(BG, (0, 0))
    for player in players:
        WIN.blit(player.image, (player.rect.x, player.rect.y))
    WIN.blit(ball.image, (ball.rect.x, ball.rect.y))
    pygame.display.update()

def main():
    run = True

    # Create players
    player1 = Player(100, HEIGHT - 150, "assets/player1.png", pygame.K_a, pygame.K_d, pygame.K_w)
    player2 = Player(600, HEIGHT - 150, "assets/player2.png", pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
    players = [player1, player2]

    # Create ball
    ball = Ball(WIDTH // 2, HEIGHT // 2, "assets/ball.png")

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Handle player movements
        keys = pygame.key.get_pressed()
        for player in players:
            player.move(keys)

        # Update ball physics
        ball.update(players)

        # Draw everything
        draw_window(players, ball)

    pygame.quit()

if __name__ == "__main__":
    main()
