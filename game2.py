# -*- coding: utf-8 -*-
from shapes import Ball
import pygame
import random


#constants
WINDOW_WIDTH=409
WINDOW_HEIGHT = 410
IMAGE = r'C:\Users\kobi\Desktop\project\pp.jpg'

HORAZON_VELOCITY = 1
VERTICAL_VELOCITY = 1
BALL_SIZE = 50


REFRESH_RATE = 60

LEFT = 1
SCROLL = 2
RIGHT = 3

def main():

    #Init screen
    img= pygame.image.load(IMAGE)
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    screen.blit(img, (0, 0))
    #pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    bals_list = pygame.sprite.Group()
    new_bals_list = pygame.sprite.Group()

    finish = False

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = pygame.mouse.get_pos()
                ball = Ball(x, y)
                vx = random.randint(-3, 3)
                vy = random.randint(-3, 3)
                ball.updtae_v(vx, vy)
                bals_list.add(ball)

        for ball in bals_list:
            ball.update_loc2(WINDOW_WIDTH - BALL_SIZE, WINDOW_HEIGHT - BALL_SIZE)

        new_bals_list.empty()
        for ball in bals_list:
            balls_hit_list = pygame.sprite.spritecollide(ball, bals_list, False)
            if len(balls_hit_list) == 1:
                new_bals_list.add(ball)

        bals_list.empty()
        for ball in new_bals_list:
            bals_list.add(ball)

        screen.blit(img, (0, 0))
        bals_list.draw(screen)
        pygame.display.flip()
        clock.tick(REFRESH_RATE)

    pygame.quit()




if __name__ == '__main__':
    main()