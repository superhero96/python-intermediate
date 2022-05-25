import pygame
import sys
#innitalize pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()