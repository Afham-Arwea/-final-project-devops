import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner - GLM Lab")
clock = pygame.time.Clock()

player_y = 220
player_vel_y = 0
is_jumping = False
obstacle_x = 600
score = 0
game_over = False

font = pygame.font.Font(None, 36)

while True:
    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (34, 139, 34), (0, 250, WIDTH, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                player_vel_y = -12
                is_jumping = True

    if not game_over:
        if is_jumping:
            player_y += player_vel_y
            player_vel_y += 0.8
            if player_y >= 220:
                player_y = 220
                is_jumping = False

        obstacle_x -= 7
        if obstacle_x < -20:
            obstacle_x = 600
            score += 1

        player_rect = pygame.draw.rect(screen, (255, 0, 0), (50, player_y, 30, 30))
        obstacle_rect = pygame.draw.rect(screen, (0, 0, 0), (obstacle_x, 220, 20, 30))

        if player_rect.colliderect(obstacle_rect):
            game_over = True

        txt_score = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(txt_score, (20, 20))
    else:
        txt_over = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(txt_over, (250, 130))

    pygame.display.flip()
    clock.tick(60)
