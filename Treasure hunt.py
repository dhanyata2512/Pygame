import pygame
import random

w= 700
h= 700
screen=pygame.display.set_mode((w,h))
bg=pygame.image.load("bg.png")
bg=pygame.transform.scale(bg,(w,h))

class Pirate (pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("pirate.png")
        self.image=pygame.transform.scale(self.image,(50,100))
        self.rect=self.image.get_rect()

class Stone (pygame.sprite.Sprite):

    def __init__(self,gem):
        super().__init__()
        self.image=pygame.image.load(gem)
        self.rect=self.image.get_rect() 
        self.rect.x=random.randint(0,w)
        self.rect.y=random.randint(0,h)      

pirate=Pirate()
pirate_group=pygame.sprite.Group()
pirate_group.add(pirate)


gem_pic=["bgem.png","cgem.png","rgem.png"]
gem_group=pygame.sprite.Group()

for i in range(100):
    stone=Stone(random.choice(gem_pic))
    gem_group.add(stone)

run=True
while run:
    screen.blit(bg,(0,0))
    pirate_group.draw(screen)
    gem_group.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
