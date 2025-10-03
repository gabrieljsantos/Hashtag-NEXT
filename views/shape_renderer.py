import pygame
import re

class ShapeRenderer:
    def __init__(self, screen, board_width=3, board_height=3, cell_size=200):
        """
        screen       : superfície pygame onde desenhar
        board_width  : número de colunas do tabuleiro
        board_height : número de linhas do tabuleiro
        cell_width   : largura de cada célula
        cell_height  : altura de cada célula
        """
        self.screen = screen
        self.board_width = board_width
        self.board_height = board_height
        self.cell_size = cell_size
        self.offset_x = cell_size // 2
        self.offset_y = cell_size // 2

    def draw_shape(self, shape_type, pixel_x, pixel_y, color):
        """
        Desenha a forma especificada.
        shape_type : str -> 'x', 'circle', 'triangle', 'square'
        pixel_x/y  : posição central em pixels
        """
        if shape_type == 'x':
            self.draw_x(pixel_x, pixel_y, color)
        elif shape_type == 'circle':
            self.draw_circle(pixel_x, pixel_y, color)
        elif shape_type == 'triangle':
            self.draw_triangle(pixel_x, pixel_y, color)
        elif shape_type == 'square':
            self.draw_square(pixel_x, pixel_y, color)
        else:
            raise ValueError(f"Forma desconhecida: {shape_type}")

    # Métodos internos com offset central
    def draw_x(self, posx, posy, color):
        posx -= self.offset_x
        posy -= self.offset_y
        pygame.draw.polygon(self.screen, color, ((22+posx,38+posy), (38+posx,22+posy), (178+posx,162+posy), (162+posx,178+posy)))
        pygame.draw.polygon(self.screen, color, ((22+posx,162+posy), (38+posx,178+posy), (178+posx,38+posy), (162+posx,22+posy)))

    def draw_circle(self, posx, posy, color):
        pygame.draw.circle(self.screen, color, (posx,posy), 79, width=24)

    def draw_triangle(self, posx, posy, color):
        pygame.draw.polygon(self.screen, color, ((posx, posy-50), (posx-43, posy+25), (posx+43, posy+25)))

    def draw_square(self, posx, posy, color):
        size = 180
        pygame.draw.rect(self.screen, color, (posx - size//2, posy - size//2, size, size))

    # Método principal para desenhar uma lista de jogadas
    def draw_moves(self, jogadas, player_shapes, colors):
        """
        jogadas       : lista de strings '0a', '1b', etc.
        player_shapes : dicionário {'a': 'x', 'b': 'circle'}
        colors        : dicionário {'a': (255,0,0), 'b': (0,0,255)}
        """
        for move in jogadas:
            match = re.match(r'([0-9]+)([a-zA-Z])$', move)
            if match:
                index, player = match.groups()
                index = int(index)
                shape_type = player_shapes.get(player)
                color = colors.get(player)
                # Calcula linha e coluna
                col = index % self.board_width
                row = index // self.board_width
                # Calcula posição central em pixels
                pixel_x = col * self.cell_size + self.offset_x
                pixel_y = row * self.cell_size + self.offset_y
                self.draw_shape(shape_type, pixel_x, pixel_y, color)
