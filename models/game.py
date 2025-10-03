class Move:
    def __init__(self, position, player, order):
        self.position = position  # número de 0 até rows*cols-1
        self.player = player      # 'A' ou 'B'
        self.order = order


class Game:
    def __init__(self, rows=3, cols=3, win_length=3):
        self.rows = rows
        self.cols = cols
        self.win_length = win_length
        self.moves = []  # lista de Move
        self.win_combinations = self.generate_win_combinations()

    def add_move(self, move):
        if move.position in [m.position for m in self.moves]:
            return False
        self.moves.append(move)
        return True

    def generate_win_combinations(self):
        combos = []

        # Linhas
        for r in range(self.rows):
            for c in range(self.cols - self.win_length + 1):
                combo = [r*self.cols + c + i for i in range(self.win_length)]
                combos.append(combo)

        # Colunas
        for c in range(self.cols):
            for r in range(self.rows - self.win_length + 1):
                combo = [(r+i)*self.cols + c for i in range(self.win_length)]
                combos.append(combo)

        # Diagonais descendentes (↘)
        for r in range(self.rows - self.win_length + 1):
            for c in range(self.cols - self.win_length + 1):
                combo = [(r+i)*self.cols + (c+i) for i in range(self.win_length)]
                combos.append(combo)

        # Diagonais ascendentes (↗)
        for r in range(self.win_length - 1, self.rows):
            for c in range(self.cols - self.win_length + 1):
                combo = [(r-i)*self.cols + (c+i) for i in range(self.win_length)]
                combos.append(combo)

        return combos

    def check_winner(self):
        a_positions = {m.position for m in self.moves if m.player == 'A'}
        b_positions = {m.position for m in self.moves if m.player == 'B'}

        for combo in self.win_combinations:
            if set(combo) <= a_positions:
                return ('A', combo)
            if set(combo) <= b_positions:
                return ('B', combo)

        if len(self.moves) == self.rows * self.cols:
            return ('#', '#')  # empate

        return None  # ninguém ganhou ainda
