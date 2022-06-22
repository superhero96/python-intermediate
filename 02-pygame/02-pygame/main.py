import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))


# Player variables
playerX = 370
playerY = 480
playerX_change = 0


#bullet variables
bulletX = 0
bulletY = 0
bulletY_change = 4
bullet_state = "ready"

# Enemy variables
enemyX = random.randint(0, 800)
enemyY = random.randint(20, 100)
enemyX_change = 4
enemyY_change = 0
# Importing player image
playerImg = pygame.image.load('player.png')
enemyImg = pygame.image.load('enemy.png')
bulletImg = pygame.image.load('bullet.png')

# Importing backdrop image
backgroundImg = pygame.image.load('background.jpeg')

def fire_bullet(x, y):
    screen.blit(bulletImg, (x, y))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_LEFT:
                playerX_change = -4
        if event.type == pygame.KEYUP:
            playerX_change = 0

    # Boundary detection
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

    #enemy boundry detection
    if enemyX > 736 or enemyX < 0:
        enemyX_change = - enemyX_change
        enemyY +=10

    playerX = playerX + playerX_change
    enemyX = enemyX + enemyX_change



    

    screen.blit(backgroundImg, (0, 0))
    screen.blit(playerImg, (playerX, playerY))
    screen.blit(enemyImg, (enemyX, enemyY))
    screen.blit(bulletImg, (enemyX, enemyY))
    fire_bullet(200, 200)
    pygame.display.update()
