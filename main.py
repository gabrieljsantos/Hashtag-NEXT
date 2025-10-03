import pygame
import time
# from multiprocessing import Process, Queue  # desativado por enquanto
from time import sleep

from views.shape_renderer import ShapeRenderer

# ---------- Worker: exemplo comentado para uso futuro ----------
"""
from multiprocessing import Process, Queue

def analysis(queue):
    number = 0
    max_number = 20
    while number <= max_number:
        per = 100 * number / max_number
        print(f"analysis progress {per}%")
        sleep(1)
        number += 1
    if per == 100:
        queue.put("successful")
    else:
        queue.put("fail")

params = {"max_number": 5000, "worker_id": 1}
"""

# ---------- Processo principal ----------
def main():
    # Inicializa Pygame
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Jogo da Velha")

    # Inicializa ShapeRenderer com tabuleiro 6x5 como exemplo
    move_renderer = ShapeRenderer(screen, board_width=5, board_height=3, cell_size=200)

    # Dados de exemplo
    jogadas = ['0a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '14a', '4b', '5b', '6b', '7b', '12b']
    player_shapes = {'a': 'x', 'b': 'circle'}
    colors = {'a': (255, 0, 0), 'b': (0, 0, 255)}

    # Loop principal
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpa a tela
        screen.fill((35, 25, 45))

        # Desenha todas as jogadas
        move_renderer.draw_moves(jogadas, player_shapes, colors)

        # Aqui futuramente você chamará outros renderers:
        # board_renderer.draw_board_line(...)
        # status_renderer.desenhar_score(...)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

# ---------- Início do programa ----------
if __name__ == "__main__":
    main()
