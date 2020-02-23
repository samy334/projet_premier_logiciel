import pygame
from game import Game
pygame.init()






pygame.display.set_caption("bomberman")
screen = pygame.display.set_mode((715,520))

background = pygame.image.load('img/bg_game.png')

game = Game()

running = True

while running:

    screen.blit(background, (0, 0))

    screen.blit(game.player1.image, game.player1.rect)

    game.player1.all_bombe.draw(screen)

    if game.pressed.get(pygame.K_d):
        game.player1.move_right()
    elif game.pressed.get(pygame.K_a):
        game.player1.move_left()
    elif game.pressed.get(pygame.K_w):
        game.player1.move_up()
    elif game.pressed.get(pygame.K_s):
        game.player1.move_down()

    print(game.player1.rect.x)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player1.put_bombe()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False