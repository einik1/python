# -*- coding: utf-8 -*-
import pygame

#constants

PINK = (255,128, 255)
MOVING_IMAGE = r'C:\Users\kobi\Desktop\project\ball.png'



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vx = 1, vy = 1):
        super(Ball, self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image.set_colorkey(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = vx
        self.__vy = vy


    def updtae_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def update_loc2(self, wide, high):
            self.rect.x += self.__vx
            self.rect.y += self.__vy
            if self.rect.x < 0 or self.rect.x > wide:
                self.__vx *= (-1)
            if self.rect.y < 0 or self.rect.y > high:
                self.__vy *= (-1)




    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy



def main():

    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()