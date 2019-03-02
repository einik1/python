# -*- coding: utf-8 -*-
import pygame
import math

#constants
WINDOW_WIDTH=409
WINDOW_HEIGHT = 410

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0,0)
PINK = (255,128, 255)

IMAGE = r'C:\Users\kobi\Desktop\project\pp.jpg'
PLAYER_IMAGE = r'C:\Users\kobi\Desktop\project\plane.png'
SOUND_FILE = r'C:\Users\kobi\Desktop\project\laser.mp3'

REFRESH_RATE = 60

LEFT = 1
SCROLL = 2
RIGHT = 3


#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
pygame.mouse.set_visible(False)


# Fill screen and show
#screen.fill(WHITE)
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))
player_img= pygame.image.load(PLAYER_IMAGE).convert()
player_img.set_colorkey(PINK)
screen.blit(player_img, (200, 200))
#pygame.draw.circle(screen, RED, [150, 150], 100, 20)
#for angle in xrange(101):
   # pygame.draw.line(screen, RED,[203, 205], [203+300*math.cos(3.6*angle), 205+300*math.sin(3.6*angle)], 1)
pygame.display.flip()

clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
mouse_pos_list = []
finish = False
KoM = True
keyboard_point = None
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if KoM:
                mouse_pos_list.append(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                del mouse_pos_list[:]
            elif event.key == pygame.K_m:
                KoM = True
            elif event.key == pygame.K_k:
                KoM = False
                keyboard_point = pygame.mouse.get_pos()
            elif event.key == pygame.K_UP and keyboard_point[1] > 10:
                keyboard_point = (keyboard_point[0], keyboard_point[1]-10)
            elif event.key == pygame.K_DOWN and keyboard_point[1] < 390:
                keyboard_point = (keyboard_point[0], keyboard_point[1]+10)
            elif event.key == pygame.K_LEFT and keyboard_point[0] > 10:
                keyboard_point = (keyboard_point[0]-10, keyboard_point[1])
            elif event.key == pygame.K_RIGHT and keyboard_point[0] < 389:
                keyboard_point = (keyboard_point[0]+10, keyboard_point[1])

    screen.blit(img, (0, 0))
    if KoM:
        mouse_point = pygame.mouse.get_pos()
        screen.blit(player_img, mouse_point)
    else:
        screen.blit(player_img, keyboard_point)
    for place in mouse_pos_list:
        screen.blit(player_img, place)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()