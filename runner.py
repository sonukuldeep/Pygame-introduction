import pygame
from random import randint
from sys import exit


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) * 0.001)
    score_surface = test_font.render(f"Score:  {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obsticle_rect in obstacle_list:
            obsticle_rect.x -= 5
            if obsticle_rect.bottom == 300:
                screen.blit(snail_surface, obsticle_rect)
            else:
                screen.blit(fly_surface, obsticle_rect)

        obstacle_list = [obsticle for obsticle in obstacle_list if obsticle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player_rect, obsticles):
    if obsticles:
        for obsticle_rect in obsticles:
            if player_rect.colliderect(obsticle_rect):
                return False
    return True


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
game_is_active = False

sky_surface = pygame.image.load("assets/graphics/Sky.png").convert()
ground_surface = pygame.image.load("assets/graphics/ground.png").convert()

# obsticles
snail_surface_1 = pygame.image.load("assets/graphics/snail/snail1.png").convert_alpha()
snail_surface_2 = pygame.image.load("assets/graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_surface_1, snail_surface_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_surface_1 = pygame.image.load("assets/graphics/Fly/Fly1.png")
fly_surface_2 = pygame.image.load("assets/graphics/Fly/Fly2.png")
fly_frames = [fly_surface_1, fly_surface_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obsticle_rect_list = []

snail_speed = -5
start_time = 0
score = 0

# player
player_walk_1 = pygame.image.load(
    "assets/graphics/Player/player_walk_1.png"
).convert_alpha()
player_walk_2 = pygame.image.load(
    "assets/graphics/Player/player_walk_2.png"
).convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_jump = pygame.image.load("assets/graphics/Player/jump.png").convert_alpha()

player_rect = player_walk_1.get_rect(midbottom=(80, 300))
player_gravity = 0

player_stand = pygame.image.load(
    "assets/graphics/Player/player_stand.png"
).convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand_scaled.get_rect(center=(400, 200))

game_name = test_font.render("Pixel runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 50))
help_text = test_font.render("Press space to start game", False, (111, 196, 169))
help_text_rect = help_text.get_rect(center=(400, 350))

# timer
obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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

            if event.type == obsticle_timer:
                print("test")
                if randint(0, 2):
                    obsticle_rect_list.append(
                        snail_surface.get_rect(bottomright=(randint(900, 1100), 300))
                    )
                else:
                    obsticle_rect_list.append(
                        fly_surface.get_rect(bottomright=(randint(900, 1100), 210))
                    )
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_is_active = True
            start_time = pygame.time.get_ticks()

    if game_is_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()
        # screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        player_animation()
        screen.blit(player_surf, player_rect)

        # obsticle movement
        obsticle_rect_list = obstacle_movement(obsticle_rect_list)

        # Collsion
        # if snail_rect.colliderect(player_rect):
        #     game_is_active = False
        game_is_active = collisions(player_rect, obsticle_rect_list)

        # snail_rect.left += snail_speed

        # if snail_rect.left < -100:
        #     snail_rect.left = 800
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        obsticle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        if score == 0:
            screen.blit(help_text, help_text_rect)
        else:
            score_text = test_font.render(f"Score: {score}", False, (111, 196, 169))
            score_rect = score_text.get_rect(center=(400, 350))
            screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(60)
