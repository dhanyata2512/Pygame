import pygame
import time

pygame.init()
w=700
h=700
screen=pygame.display.set_mode((w,h))

ballon=pygame.image.load("ballons.jpg")
ballon=pygame.transform.scale(ballon,(w,h))
box=pygame.image.load("box.jpg")
box=pygame.transform.scale(box,(w,h))






run=True
while run:
    screen.fill("light blue")
    screen.blit(ballon,(0,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(box,(0,0))
    pygame.display.update()
    time.sleep(2)