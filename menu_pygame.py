import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((640, 480))

def start_the_game():
    print('O jogo está iniciando!')

menu = pygame_menu.Menu('nome', 640, 480)

menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    surface.fill((255, 255, 255))
    menu.update(events)
    menu.draw(surface)
    pygame.display.update()