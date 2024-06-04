import pygame
import random
pygame.init()


screen=pygame.display.set_mode((500,500))
class Circle:

  def __init__(self,demension,color):
    self.color=color
    self.demension=demension

  def draw_circ(self):
     pygame.draw.circle(screen, self.color, self.demension[:2], self.demension[2], self.demension[3])

  def change_color(self):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    self.color=r,g,b
    self.draw_circ()
    
    
    
a=Circle((50,15,50,70),"blue")
b=Circle((25,2,37,72),"magenta")
c=Circle((70,268,70,84),"purple")

screen.fill("light blue")

run=True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False
      pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      a.draw_circ()
      b.draw_circ()
      c.draw_circ()
      pygame.display.update()

    if event.type == pygame.MOUSEBUTTONUP:
      a.change_color()
      b.change_color()
      c.change_color()
      pygame.display.update()

    if event.type == pygame.MOUSEMOTION:
      x,y=pygame.mouse.get_pos()
      d=Circle((x,y,16,2),"black")
      d.draw_circ()
      pygame.display.update()