import pygame

w=700
h=500
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
            if event.key==pygame.K_DOWN:
                arrow["down"]=True 
            if event.key==pygame.K_RIGHT:
                arrow["right"]=True
            if event.key==pygame.K_LEFT:
                arrow["left"]=True    

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                arrow["up"]=False
            if event.key==pygame.K_DOWN:
                arrow["down"]=False
            if event.key==pygame.K_RIGHT:
                arrow["right"]=False  
            if event.key==pygame.K_LEFT:
                arrow["left"]=False                
                  
    if  arrow["up"]==True:
        y=y-2
    if  arrow["down"]==True:
        y=y+2
    if  arrow["right"]==True:
        x=x+2
    if  arrow["left"]==True:
        x=x-2
        
