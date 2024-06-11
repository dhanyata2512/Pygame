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
cake=pygame.image.load("cake.jpg")
cake=pygame.transform.scale(cake,(w,h))
gif=pygame.image.load("gif.gif")
#gif=pygame.transform.scale(gif,(w,h))

font=pygame.font.SysFont("comic sans",27)
text1=font.render("HAPPY BIRTHDAY!!!",True,"magenta")
text2=font.render("Wish you a happy day!",True,"blue")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()        

    screen.fill("light blue")
    screen.blit(ballon,(0,0))
    screen.blit(text1,(200,300))
    pygame.display.update()
    time.sleep(2)
    screen.blit(box,(0,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(cake,(0,0))
    screen.blit(text2,(100,70))
    pygame.display.update()
    time.sleep(2)
    screen.blit(gif,(0,0))
    pygame.display.update()
    time.sleep(5)
    
