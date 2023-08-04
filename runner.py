import pygame
from sys import exit


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) * 0.001)
    score_surface = test_font.render(f"Score:  {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
game_is_active = True

sky_surface = pygame.image.load("assets/graphics/Sky.png").convert()
ground_surface = pygame.image.load("assets/graphics/ground.png").convert()
snail_surface = pygame.image.load("assets/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))
snail_speed = -5
start_time = 0

player_surface = pygame.image.load(
    "assets/graphics/Player/player_walk_1.png"
).convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_is_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            snail_rect.left = 800
            game_is_active = True
            start_time = pygame.time.get_ticks()

    if game_is_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        display_score()
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # Collsion
        if snail_rect.colliderect(player_rect):
            game_is_active = False

        snail_rect.left += snail_speed

        if snail_rect.left < -100:
            snail_rect.left = 800
    else:
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)
