import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')
sky_surface = pygame.image.load("assets/graphics/Sky.png").convert()
ground_surface = pygame.image.load("assets/graphics/ground.png").convert()
score_surface = test_font.render("My game", False, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))
snail_surface = pygame.image.load("assets/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))
snail_speed = -4

player_surface = pygame.image.load(
    "assets/graphics/Player/player_walk_1.png"
).convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print("Space pressed")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_surface, score_rect)
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    snail_rect.left += snail_speed

    if snail_rect.left < -100:
        snail_rect.left = 800

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump")

    clock.tick(60)
