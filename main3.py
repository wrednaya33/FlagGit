import pygame

pygame.init()

scr = pygame.display.set_mode((300, 300))
scr.fill(pygame.Color('green'))

def draw():
    pygame.draw.rect(scr, pygame.Color('black'), [(10, 10), (20, 260)], 0)
    pygame.draw.rect(scr, pygame.Color('white'), [(30, 70), (170, 60)], 0)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()