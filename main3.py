import pygame

pygame.init()

scr = pygame.display.set_mode((300, 300))
scr.fill((255, 255, 255))

def draw():
    pygame.draw.rect(scr, pygame.Color('black'), [(10, 10), (20, 260)], 0)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()