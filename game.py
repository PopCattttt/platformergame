import pygame
from pygame.locals import *

pygame.init()

width, height = 1000, 1000

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer")

# Load images
sun_img = pygame.image.load("img/sun.png")
sky_img = pygame.image.load("img/sky.png")

def draw_window():
    window.blit(sky_img, (0, 0))
    window.blit(sun_img, (100, 100))
    
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main()
