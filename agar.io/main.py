import sys
import random
from food import *
from player import *

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 950, 540
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
mouse_x = 0
mouse_y = 0
NUM_FOOD = 20
FOOD_SIZE = 15
foods = []

# Creating food items
for i in range(NUM_FOOD):
    food_x = random.randint(FOOD_SIZE, width - FOOD_SIZE)
    food_y = random.randint(FOOD_SIZE, height - FOOD_SIZE)
    food = Food(food_x, food_y)
    foods.append(food)


# C reating player object
player = Player(width/2, height/2)

#loading the img
backdrop = pygame.image.load('baground.jpg')

#loading the sound
chomp = pygame.mixer.Sound('Suction Cup.wav')
# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    player.x += player.x_vel
    player.y += player.y_vel
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.x_vel = (mouse_x - player.x) * 0.1
    player.y_vel = (mouse_y - player.y) * 0.1


   #touching sennsing fooooooood
    for food in foods:    
        if player.touching(food):
            pygame.mixer.Sound.play(chomp)
            player.radius += 2
            foods.remove(food)
       

# Edge sensing
    if player.x < player.radius:
        player.x = player.radius
    if player.x > (width - player.radius):
        player.x = width - player.radius
    if player.y < player.radius:
        player.y = player.radius
    if player.y > (height - player.radius):
        player.y = height - player.radius

    # Draw.
    screen.blit(backdrop, (0, 0))
    pygame.draw.circle(screen, RED, (player.x, player.y), player.radius)
    for food in foods:
        pygame.draw.circle(screen, food.color, (food.x, food.y), food.size)

    pygame.display.flip()
    fpsClock.tick(fps)
