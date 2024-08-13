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
        self.rect=self.image.get_rect()

pirate=Pirate()
pirate_group=pygame.sprite.Group()
pirate_group.add(pirate)



run=True
while run:
    screen.blit(bg,(0,0))
    pirate_group.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
