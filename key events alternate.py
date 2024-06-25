import pygame

w=700
h=500
screen=pygame.display.set_mode((w,h))


bg=pygame.image.load("kspace.png")
rocket=pygame.image.load("krocket.png")


rec=pygame.Rect(300,300,20,70)

run=True  
while run:
    pygame.draw.rect(screen,"white",rec)
    screen.blit(bg,(0,0)) 
    screen.blit(rocket,(rec.x,rec.y))  
    pygame.display.update()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit() 

    press_key=pygame.key.get_pressed()   
    print(press_key)
    if press_key[pygame.K_UP]:
        rec.y=rec.y-2

