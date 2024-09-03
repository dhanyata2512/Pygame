import pygame
import random
import time

pygame.init()

w= 1200
h= 800
screen=pygame.display.set_mode((w,h))
bg=pygame.image.load("bg.png")
bg=pygame.transform.scale(bg,(w,h))

class Pirate (pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("pirate.png")
        self.image=pygame.transform.scale(self.image,(50,100))
        self.rect=self.image.get_rect()

        

    def update (self,keys):
        speed=3
        if keys [pygame.K_UP] and self.rect.top>0:
            self.rect.y=self.rect.y-speed
        if keys [pygame.K_LEFT] and self.rect.left>0:
            self.rect.x=self.rect.x-speed
        if keys [pygame.K_DOWN] and self.rect.bottom<h:
            self.rect.y=self.rect.y+speed
        if keys [pygame.K_RIGHT] and self.rect.right<w:
            self.rect.x=self.rect.x+speed            



class Stone (pygame.sprite.Sprite):

    def __init__(self,gem):
        super().__init__()
        self.image=pygame.image.load(gem)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect() 
        self.rect.x=random.randint(40,w-40)
        self.rect.y=random.randint(40,h-40)      


class Solider (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("enemy.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect() 
        self.rect.x=random.randint(40,w-40)
        self.rect.y=random.randint(40,h-40)


pirate=Pirate()
pirate_group=pygame.sprite.Group()
pirate_group.add(pirate)


gem_pic=["bgem.png","cgem.png","rgem.png"]
gem_group=pygame.sprite.Group()

for i in range(180):
    stone=Stone(random.choice(gem_pic))
    gem_group.add(stone)

solider_group=pygame.sprite.Group()

for i in range(30):
    solider=Solider()
    solider_group.add(solider)      

score=0

start_time=time.time()
font=pygame.font.SysFont("comicsans",17,True,True)
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()    
    time_passed=time.time()-start_time
    if time_passed >= 35:
        screen.fill((22, 106, 242))
        if score >= 800:
            loot_text=font.render("YOU ARE SUCSESSFULL",True,"white")
        else:
            loot_text=font.render("YOU FAILED YOUR QUEST BETTER LUCK NEXT TIME!",True,"red")
        screen.blit(loot_text,(w/2-loot_text.get_width()/2,h/2))
    else:    
        screen.blit(bg,(0,0))
        pirate_group.draw(screen)
        gem_group.draw(screen)
        solider_group.draw(screen)
        

        pressed_keys=pygame.key.get_pressed() 
        pirate.update(pressed_keys)

        soliders_hit=pygame.sprite.spritecollide(pirate,solider_group,True)  
        
        for soliders in soliders_hit:
            score=score-20

        gems_collected=pygame.sprite.spritecollide(pirate,gem_group,True)
        
        for gems in gems_collected:
            score=score+10
        
        text= font.render("Score:"+ str (score),True,"white")
        screen.blit(text,(w-100,50))
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
