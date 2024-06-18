import pygame

w=700
h=700
screen=pygame.display.set_mode((w,h))

arrow={"up":False,"down":False,"left":False,"right":False}

bg=pygame.image.load("kspace.png")
rocket=pygame.image.load("krocket.png")
x=300
y=300
run=True  
while run:
    screen.blit(bg,(0,0)) 
    screen.blit(rocket,(x,y))  
    pygame.display.update()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit() 

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
               arrow["up"]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                arrow["up"]=False

    if  arrow["up"]==True:
        y=y-2

