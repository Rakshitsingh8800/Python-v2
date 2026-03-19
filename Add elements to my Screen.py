import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game Screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
text = font.render("Hello Pygame!", True, BLACK)

running = True
while running:
    screen.fill(WHITE) 

    pygame.draw.rect(screen, BLUE, (200, 150, 200, 100))

    screen.blit(text, (220, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()