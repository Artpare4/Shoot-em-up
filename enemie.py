import pygame
import random
class Enemie(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.velocity=5
            self.image=pygame.image.load("boule.png")
            self.rect=self.image.get_rect()
            list=[80,120,160,200,240,280,320,360,400,440,480,600,640,680]
            self.rect.x=random.choice(list)
            self.rect.y=-20
            self.bin=random.randint(0,2)
            self.accel=random.randint(0,1)
##            self.rect=self.rect.inflate(0,0)
    def mouvmt(self):
        for i in range(1):
            if self.bin==0:
                self.rect.x=(self.rect.x+self.velocity)
            elif self.bin==1:
                self.rect.x= (self.rect.x-self.velocity)
            elif self.bin==2:
                pass

        if self.rect.x==-30:
            self.bin=0
        elif self.rect.x==745:
            self.bin=1

        self.rect.y=(self.rect.y+self.velocity)

    def respawn(self):
        if self.rect.y==600:
            self.bin=random.randint(0,2)
            self.rect.y=-20

