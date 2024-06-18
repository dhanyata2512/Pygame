import pygame
import time

pygame.init()

w=300
h=400
screen=pygame.display.set_mode((w,h))

loff=pygame.image.load("lof.png")
l_on=pygame.image.load("lon.png")

current="off"

def change():
    global current
    if current=="off":
        screen.blit(l_on,(0,0))
        current="on"
        
    else:
        screen.blit(loff,(0,0)) 
        current="off"
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            change()
            pygame.display.update()       

   # pygame.display.update()
    #time.sleep(2)
    #screen.blit(l_on,(0,0))
    #pygame.display.update()
    #time.sleep(2)

   



