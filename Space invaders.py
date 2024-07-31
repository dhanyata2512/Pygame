import pygame

pygame.init()

w=1000
h=600
screen=pygame.display.set_mode((w,h))
R_HIT=pygame.USEREVENT+1
Y_HIT=pygame.USEREVENT+2
FPS=60
m_bullet=4

font=pygame.font.SysFont("comicsans",17,True,True)

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

def red_ship_movement(red_rect,keys):
    if keys[pygame.K_a] and red_rect.left>0:
        red_rect.x=red_rect.x-2
    if keys[pygame.K_d] and red_rect.right<border.left:
        red_rect.x=red_rect.x+2
    if keys[pygame.K_s] and red_rect.bottom < h:
        red_rect.y=red_rect.y+2
    if keys[pygame.K_w] and red_rect.top > 0:
        red_rect.y=red_rect.y-2   


def yellow_ship_movement(yellow_rect,keys):
    if keys[pygame.K_LEFT] and yellow_rect.left>border.right:
        yellow_rect.x=yellow_rect.x-2
    if keys[pygame.K_RIGHT] and yellow_rect.right< w :
        yellow_rect.x=yellow_rect.x+2
    if keys[pygame.K_DOWN] and yellow_rect.bottom < h:
        yellow_rect.y=yellow_rect.y+2
    if keys[pygame.K_UP] and yellow_rect.top > 0:
        yellow_rect.y=yellow_rect.y-2   


def bullet_movmment(r_bullets,y_bullets,r_rect,y_rect):
    for y_bullet in y_bullets:
        y_bullet.x=y_bullet.x-7
        if y_bullet.colliderect(r_rect):
            pygame.event.post(pygame.event.Event(R_HIT))
            y_bullets.remove(y_bullet)
        elif y_bullet.x < 0:
            y_bullets.remove(y_bullet)
def start ():
    r_rect=pygame.Rect(50,h/2-s_height/2,s_width,s_height)
    y_rect=pygame.Rect(w-50-s_width,h/2-s_height/2,s_width,s_height)
    r_bullets=[]
    y_bullets=[]
    r_health=7
    y_health=7
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        screen.blit(bg,(0,0))
        screen.blit(r_ship,(r_rect.x,r_rect.y))
        screen.blit(y_ship,(y_rect.x,y_rect.y))
        pygame.draw.rect(screen,(0,0,0),border)
        for bullet in r_bullets:
            pygame.draw.rect(screen,"white",bullet)

        for bullet in y_bullets:
            pygame.draw.rect(screen,"white",bullet)    

        r_text=font.render("Health:"+str(r_health),True,"white")
        screen.blit(r_text,(20,20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c and len(r_bullets) < m_bullet:
                    bullet=pygame.Rect(r_rect.left,y_rect.top+s_height/2,17,3)
                    r_bullets.append(bullet)

                if event.key==pygame.K_l and len(y_bullets) < m_bullet:
                    bullet=pygame.Rect(y_rect.left,y_rect.top+s_height/2,17,3)
                    y_bullets.append(bullet) 

            if event.type==R_HIT:
                r_health=r_health-1
                print(r_health)       

        pressed_key=pygame.key.get_pressed()
        red_ship_movement(r_rect,pressed_key)
        yellow_ship_movement(y_rect,pressed_key)
        bullet_movmment(r_bullets,y_bullets,r_rect,y_rect)
start()
