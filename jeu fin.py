import pygame
from enemie import Enemie
import random
import time

class Player(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("vaisseaux.png")
       self.image=pygame.transform.scale(self.image, (50, 25))
       self.rect=self.image.get_rect()
       self.rect.x=400
       self.rect.y=300

   def gauche(self):
       self.rect.x=self.rect.x-20
   def droite(self):
       self.rect.x=self.rect.x+20
   def haut(self):
       self.rect.y=self.rect.y-20
   def bas(self):
       self.rect.y=self.rect.y+20

class jeu:

    def __init__(self):
        self.run = True
        self.surf = pygame.display.set_mode((800,600))
        self.posX=400
        self.posY=300
        self.vie=1
        self.joueur = Player()
        self.background=pygame.image.load("background2.png")
        self.background=pygame.transform.scale(self.background, (800, 600))
        self.clock=pygame.time.Clock()
        self.all_enemie=pygame.sprite.Group()
        self.players=pygame.sprite.Group()
        self.players.add(self.joueur)
        self.pressed={}
        self.jeu=jeu
        self.colision1=self.all_enemie
        colision=[self.colision1]
        self.spawn(random.randint(1,15))
        self.playlist = list()
        self.playlist.append ( "miami-nights-1984-accelerated.mp3" )
        self.blank=(255,255,255)
        self.fon=pygame.font.SysFont("arial",30)
        self.text=self.fon.render("Vous avez perdu , relancez le jeu pour refaire une partie ",False,self.blank)
    def spawn(self,spipi):
        global enemie
##        self.nb_mob=1
##        for i in range(secs):
##            self.spipi=random.randint(1,15)
##            self.nb_mob+=1
##            time.sleep(secs)

##        if secs==1:
        spipi=random.randint(1,15)
        for i in range(spipi):
            enemie=Enemie()
            self.all_enemie.add(enemie)


    def check_colision(self,sprite,group):
       return pygame.sprite.spritecollide(sprite,group,False)

    def mort(self,sprite,group):
        if self.jeu.check_colision(self,sprite,group):
           self.vie=0


    def start_and_end(self):

        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if event.type==pygame.KEYDOWN:
                    
                if event.key == pygame.K_UP:
                    if 0<self.posY<=600:
                        self.posY=self.posY-20
                        self.joueur.haut()
                elif event.key == pygame.K_DOWN and 0<=self.posY<540:
                        self.posY=self.posY+20
                        self.joueur.bas()
                elif event.key == pygame.K_LEFT :
                    if 0<self.posX<=800:
                        self.posX=self.posX-20
                        self.joueur.gauche()
                elif event.key == pygame.K_RIGHT and 0<=self.posX<720:
                    self.posX=self.posX+20
                    self.joueur.droite()


            self.surf.fill((0,0,0))
            self.surf.blit(self.background,(0,0))
            self.players.draw(self.surf)
            self.all_enemie.draw(self.surf)
            self.mort(self.joueur,self.all_enemie)

            for Enemie in self.all_enemie:
                Enemie.mouvmt()
                Enemie.respawn()

            if self.vie==0:
                self.surf.blit(self.background,(0,0))
                self.surf.blit(self.text,[100,300])

            self.clock.tick(30)
            pygame.display.update()

    def globa(self):
        #pygame.mixer.music.load ( self.playlist.pop())
        #pygame.mixer.music.play()
        self.start_and_end()

pygame.mixer.init()
pygame.init()
a=jeu()
a.globa()
pygame.quit()