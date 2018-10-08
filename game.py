import pygame

pygame.init()

SCALE = 100
WHITE = (255, 255, 255)
PURPLE = (204, 153, 255)

WIDTH = 400
HIGHT = 400

img = pygame.transform.scale(pygame.image.load('easterEgg.png'), (SCALE, SCALE))

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Recty')

gameExit = False

rect_size = 60
pos_x = WIDTH / 2 - rect_size / 2
pos_y = HIGHT / 2 - rect_size / 2
x_change = 0
y_change = 0
d_move = 5

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -d_move
            elif event.key == pygame.K_RIGHT:
                x_change = d_move
            elif event.key == pygame.K_UP:
                y_change = -d_move
            elif event.key == pygame.K_DOWN:
                y_change = d_move
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    if pos_x + rect_size + x_change < WIDTH and pos_x + x_change > 0:
        pos_x += x_change
    if pos_y + rect_size + y_change < HIGHT and pos_y + y_change > 0:
        pos_y += y_change

    gameDisplay.fill(WHITE)
    gameDisplay.blit(img, (WIDTH / 2 - SCALE / 2, rect_size / 2))

    pygame.draw.rect(gameDisplay, PURPLE, [pos_x, pos_y, rect_size, rect_size])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()