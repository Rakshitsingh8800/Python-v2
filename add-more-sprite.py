import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 1
BULLET_SPEED_Y = 14
COLLISION_DISTANCE = 30

pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound effects

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.music.load('horror.mp3')  # Load background music
pygame.mixer.music.play(-1)  # Play background music on loop
# Background
background = pygame.image.load('nightroad.jpg')
background = pygame.transform.scale(background, (800, 500))

pygame.display.set_caption("Zombie Shooter")

# Icon
icon = pygame.image.load('zombie-remove-bg.png')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

# Player
player_Img = pygame.image.load('army-remove.bg.png')
player_Img = pygame.transform.scale(player_Img, (64, 64))

PlayerX = PLAYER_START_X
PlayerY = PLAYER_START_Y
PlayerX_change = 0

# Enemies
enemy_Img = []
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 5   # reduced for better balance

for i in range(num_of_enemies):
    img = pygame.image.load('ghost.png')
    img = pygame.transform.scale(img, (64, 64))
    enemy_Img.append(img)

    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)

# Bullet
bullet_Img = pygame.image.load('bullet-removebg-preview.png')
bullet_Img = pygame.transform.scale(bullet_Img, (16, 32))

bulletX = 0
bulletY = PLAYER_START_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    score_text = font.render("You killed: " + str(score_value), True, (255, 255, 255))

    screen.blit(over_text, (200, 200))
    screen.blit(score_text, (260, 270))
def player(x, y):
    screen.blit(player_Img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_Img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Img, (x + 24, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

running = True
game_over = False

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    PlayerX_change = -5
                if event.key == pygame.K_RIGHT:
                    PlayerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = PlayerX
                        bulletY = PlayerY
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    PlayerX_change = 0

    if not game_over:
        
        PlayerX += PlayerX_change
        if PlayerX <= 0:
            PlayerX = 0
        elif PlayerX >= 736:
            PlayerX = 736

        # Enemy movement
        for i in range(num_of_enemies):

            # If zombie reaches near player → GAME OVER
            if enemyY[i] > 420:
                game_over = True
                break

            
            enemyY[i] += 0.1

           
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= 736:
                enemyX_change[i] *= -1

            
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1

                
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            
            if enemyY[i] > SCREEN_HEIGHT:
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            enemy(enemyX[i], enemyY[i], i)

        
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= BULLET_SPEED_Y

    else:
        game_over_text()

    player(PlayerX, PlayerY)
    show_score(10, 10)

    pygame.display.update()
