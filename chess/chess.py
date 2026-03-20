import pygame
import sys
pygame.init()
pygame.display.set_caption("Chess")

screen = pygame.display.set_mode((512,512))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(8):
         for col in range(8):
             if (row + col) % 2 == 0:
                 color = (255, 206, 158)
             else:
                 color = (111, 78, 55)
          

             pygame.draw.rect(screen, color, (col * 64, row * 64, 64, 64)) 

             pygame.display.flip()     


 