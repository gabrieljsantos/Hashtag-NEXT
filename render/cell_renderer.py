import pygame
class CellRenderer:
    def __init__(self, screen, board_width, board_height, cell_size, color):
        self.screen = screen
        self.board_width = board_width
        self.board_height = board_height
        self.cell_size = cell_size
        self.color = color

    def render_selection(self, index):
        row = index // self.board_width
        col = index % self.board_width
        pygame.draw.rect(
            self.screen, 
            self.color, 
            (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
        )
