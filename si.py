import math
import random
import pygame
import pygame.imageext
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_STARTX = 370
PLAYER_STARTY = 380
E_START_Y_MIN = 50
E_START_Y_MAX = 150
E_SPEED_X = 4
E_SPEED_Y = 40
B_SPEED_Y = 10
CD = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BG = pygame.image.load("/Users/aishwaryaagarwal/Desktop/PYTHON/istockphoto-1403514917-612x612.jpg")
pygame.display.set_caption("SPACE INVADERSSSSSS!")
PI = pygame.image.load("/Users/aishwaryaagarwal/Desktop/PYTHON/player.png")
px = PLAYER_STARTX
py = PLAYER_STARTY
px_CHANGE = 0

enemyi = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyi.append(pygame.image.load("/Users/aishwaryaagarwal/Desktop/PYTHON/pngtree-space-invaders-character-game-play-picture-image_8233346.png")) 
    enemyx.append(random.randint(0,SCREEN_WIDTH-64))
    enemyy.append(random.randint(E_START_Y_MIN,E_START_Y_MAX))
    enemyx_change.append(E_SPEED_X)
    enemyy_change.append(E_SPEED_Y)

BULLETi = pygame.image.load("/Users/aishwaryaagarwal/Desktop/PYTHON/pngtree-bullet-icon-in-cartoon-style-png-image_1823049.jpg") 
bulletX = 0
bulletY = PLAYER_STARTY
BULLETX_CHANGE = 0
BULLETY_CHANGE = B_SPEED_Y
BULLET_S = "ready"
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10
o_font = font = pygame.font.Font("freesansbold.ttf",64)
def show_score(x,y):
    score = font.render("Score :"+ str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    game_over = o_font.render("GAME OVER", True,(255,255,255)) 
    screen.blit(game_over,(200,250))
def player(x,y):
    screen.blit(PI,(x,y)) 
def enemy(x,y,i):
    screen.blit(enemyi[i],(x,y))
def fire_bullet(x,y):
    global BULLET_S
    BULLET_S = "fire"
    screen.blit(BULLETi,(x+16,y+10))  
def isCollision(enemyx,enemyy,bulletX,bulletY):
    distance = math.sqrt((enemyx-bulletX)** 2 + (enemyy-bulletY)**2)
    return distance<CD
running = True
while running:
    screen.fill((0,0,0)) 
    screen.blit(BG,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_CHANGE == -5
            if event.key == pygame.K_RIGHT:
                px_CHANGE == 5
            if event.key == pygame.K_SPACE and BULLET_S == "ready":
                bulletX = px
        if event.type == pygame.KEYUP and event.key in[pygame.K_LEFT,pygame.K_RIGHT]:
            px_CHANGE = 0
    px += px_CHANGE 
    px = max(0, min(px, SCREEN_WIDTH - 64))  
    for i in range(num_of_enemy):
        if enemyy[i] > 340: 
            for j in range(num_of_enemy):
              enemyy[j] = 2000
            game_over_text()
            break            
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= SCREEN_WIDTH - 64:
            enemyx_change[i] *= -1
            enemyy[i] += enemyy_change[i]
        if isCollision(enemyx[i], enemyy[i], bulletX, bulletY):
           bulletY = PLAYER_STARTY
           BULLET_S = "ready"
           score_value += 1
           enemyx[i] = random.randint(0, SCREEN_WIDTH - 64)
           enemyy[i] = random.randint(E_START_Y_MIN, E_START_Y_MAX)
        enemy(enemyx[i], enemyy[i], i)
    if bulletY <= 0:
       bulletY = PLAYER_STARTY
       BULLET_S = "ready"
    elif BULLET_S == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= BULLETY_CHANGE
    player(px, py)
    show_score(textX, textY)
    pygame.display.update()