class Player:
    """
    Representa um jogador no jogo.
    """

    def __init__(self, name, shape, mode='human'):
        """
        name : str -> nome do jogador
        shape : str -> forma geométrica associada, ex: 'triangle', 'circle', 'X', 'square'
        mode : str -> tipo de jogador: 'human', 'AI_minimax', 'AI_heuristic', 'AI_good_sequences', 'AI_random'
        """
        self.name = name
        self.shape = shape
        self.mode = mode
        self.wins = 0          # número de partidas ganhas
        self.losses = 0        # número de partidas perdidas
        self.draws = 0         # número de empates
        self.moves_made = []   # lista de posições jogadas (opcional para análise futura)

    def record_move(self, position):
        """Adiciona uma jogada ao histórico do jogador"""
        self.moves_made.append(position)

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1

    def record_draw(self):
        self.draws += 1

    def reset_moves(self):
        """Limpa o histórico de jogadas"""
        self.moves_made = []

    def __repr__(self):
        return f"<Player {self.name} ({self.shape}, {self.mode}) Wins: {self.wins}>"
