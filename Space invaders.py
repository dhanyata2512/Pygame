import pygame

pygame.init()

w=1000
h=600
screen=pygame.display.set_mode((w,h))

s_width=72
s_height=72
bg=pygame.image.load("space_invaders_images\\bg.png")
bg=pygame.transform.scale(bg,(w,h))
r_ship=pygame.image.load("space_invaders_images\\red.png")
r_ship=pygame.transform.scale(r_ship,(s_width,s_height))
r_ship=pygame.transform.rotate(r_ship,90)
y_ship=pygame.image.load("space_invaders_images\\yellow.png")
y_ship=pygame.transform.scale(y_ship,(s_width,s_height))
y_ship=pygame.transform.rotate(y_ship,-90)

border=pygame.Rect(w/2-5,0,10,h)

def start ():
    run=True
    while run:
        screen.blit(bg,(0,0))
        screen.blit(r_ship,(50,h/2-s_height/2))
        screen.blit(y_ship,(w-50-s_width,h/2-s_height/2))
        pygame.draw.rect(screen,(0,0,0),border)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
start()