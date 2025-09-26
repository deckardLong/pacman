from board import boards
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TIMER = pygame.time.Clock() # Control the speed at which game runs
FPS = 60
FONT = pygame.font.Font('freesansbold.ttf', 20)
LEVEL = boards
COLOR = 'blue'
PI = math.pi

player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45))) 

player_x = 450
player_y = 663 
direction = 0
counter = 0
flicker = False

# Draw each tile type onto the board
def draw_board():
    num_1 = ((HEIGHT - 50) // 32)
    num_2 = (WIDTH // 30)

    for i in range(len(LEVEL)):
        for j in range(len(LEVEL[i])):
            if LEVEL[i][j] == 1:
                pygame.draw.circle(SCREEN, 'white', (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 4)
            if LEVEL[i][j] == 2 and not flicker:
                pygame.draw.circle(SCREEN, 'white', (j * num_2 + (0.5 * num_2), i * num_1 + (0.5 * num_1)), 16)
            if LEVEL[i][j] == 3:
                pygame.draw.line(SCREEN, COLOR, (j * num_2 + (0.5 * num_2), i * num_1), (j * num_2 + (0.5 * num_2), i * num_1 + num_1), 3)
            if LEVEL[i][j] == 4:
                pygame.draw.line(SCREEN, COLOR, (j * num_2, i * num_1 + (0.5 * num_1)), (j * num_2 + num_2, i * num_1 + (0.5 * num_1)), 3)
            if LEVEL[i][j] == 5:
                pygame.draw.arc(SCREEN, COLOR, [(j * num_2 - (num_2 * 0.4)) - 2, (i * num_1 + (0.5 * num_1)), num_2, num_1], 0, PI / 2, 3)
            if LEVEL[i][j] == 6:
                pygame.draw.arc(SCREEN, COLOR, [(j * num_2 + (num_2 * 0.5)), (i * num_1 + (0.5 * num_1)), num_2, num_1], PI / 2, PI, 3)
            if LEVEL[i][j] == 7:
                pygame.draw.arc(SCREEN, COLOR, [(j * num_2 + (num_2 * 0.5)), (i * num_1 - (0.4 * num_1)), num_2, num_1], PI, 3 * PI / 2, 3)
            if LEVEL[i][j] == 8:
                pygame.draw.arc(SCREEN, COLOR, [(j * num_2 - (num_2 * 0.4)) - 2, (i * num_1 - (0.4 * num_1)), num_2, num_1], 3 * PI / 2, 2 * PI, 3)
            if LEVEL[i][j] == 9:
                pygame.draw.line(SCREEN, 'white', (j * num_2, i * num_1 + (0.5 * num_1)), (j * num_2 + num_2, i * num_1 + (0.5 * num_1)), 3)

# Drawing and Animating the Player
def draw_player():
    # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN
    if direction == 0:
        SCREEN.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        SCREEN.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        SCREEN.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        SCREEN.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


run = True

while run:
    TIMER.tick(FPS) 
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    SCREEN.fill('black')
    draw_board()
    draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
    
    pygame.display.update()

pygame.quit()