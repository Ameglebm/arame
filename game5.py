import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definindo a velocidade do jogador e do inimigo
PLAYER_SPEED = 5
ENEMY_SPEED = 3

# Definindo o tamanho do jogador e do inimigo
PLAYER_SIZE = 25
ENEMY_SIZE = 15

# Definindo a posição inicial do jogador e do inimigo
player_x = 100
player_y = SCREEN_HEIGHT - PLAYER_SIZE
enemy_x = SCREEN_WIDTH - ENEMY_SIZE - 100
enemy_y = SCREEN_HEIGHT - ENEMY_SIZE

# Criando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Criando o relógio
clock = pygame.time.Clock()

# Criando a fonte para o texto
font = pygame.font.SysFont('Arial', 30)

# Loop principal do jogo
game_running = True
while game_running:

    # Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Movendo o jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - PLAYER_SIZE:
        player_y += PLAYER_SPEED

    # Movendo o inimigo
    if enemy_x > player_x:
        enemy_x -= ENEMY_SPEED
    elif enemy_x < player_x:
        enemy_x += ENEMY_SPEED
    if enemy_y > player_y:
        enemy_y -= ENEMY_SPEED
    elif enemy_y < player_y:
        enemy_y += ENEMY_SPEED

    # Desenhando a tela
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [int(player_x + PLAYER_SIZE / 2), int(player_y + PLAYER_SIZE / 2)], PLAYER_SIZE / 2)
    pygame.draw.circle(screen, BLACK, [int(enemy_x + ENEMY_SIZE / 2), int(enemy_y + ENEMY_SIZE / 2)], ENEMY_SIZE / 2)

    # Verificando se o jogador foi atingido pelo inimigo
    if (enemy_x >= player_x and enemy_x <= player_x + PLAYER_SIZE) or \
            (enemy_x + ENEMY_SIZE >= player_x and enemy_x + ENEMY_SIZE <= player_x + PLAYER_SIZE):
        if (enemy_y >= player_y and enemy_y <= player_y + PLAYER_SIZE) or \
                (enemy_y + ENEMY_SIZE >= player_y and enemy_y + ENEMY_SIZE <= player_y + PLAYER_SIZE):
            game_running = False

    # Atualizando a tela
    pygame.display.update()

    # Definindo a velocidade do jogo
    clock.tick(60)

# Exibindo mensagem de fim de jogo
screen.fill(WHITE)
message = font.render("Game Over! Pressione qualquer tecla para sair", True, BLACK)
message
