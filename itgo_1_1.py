import pygame
from random import randint
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)

FPS = pygame.time.Clock()

pygame.init()

screen = width, height = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(White)
ball_rect = ball.get_rect()
ball_speed = 3



is_working = True

def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(Red)
    enemy_rect = pygame.Rect(width, randint(0, height), *enemy.get_size())
    enemy_speed = 1

    return [enemy, enemy_rect, randint(2, 5)]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)


enemies = []

while(is_working):
    FPS.tick(130)

    for event in pygame.event.get():
        if event.type == QUIT: 
            is_working= False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())



    pressed_keys = pygame.key.get_pressed()
    
    main_surface.fill(Black)
    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0: 
            enemies.pop(enemies.index(enemy))

        if ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))

    if pressed_keys[K_DOWN] and ball_rect.bottom <= height: 
       ball_rect = ball_rect.move([0, ball_speed])
    
    if pressed_keys[K_UP]: 
       ball_rect = ball_rect.move([0, -ball_speed])

    if pressed_keys[K_RIGHT]: 
       ball_rect = ball_rect.move([ball_speed, 0])
    
    if pressed_keys[K_LEFT]: 
       ball_rect = ball_rect.move([-ball_speed, 0])

    

    pygame.display.flip()