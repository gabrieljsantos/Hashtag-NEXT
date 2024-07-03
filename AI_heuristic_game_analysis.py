import csv
from copy import deepcopy
import matplotlib.pyplot as plt
import random

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def plot_analysis_results(analysis_results, occupied_positions):
    num_positions = 9  # O número de posições possíveis no jogo da velha
    num_cols = 3  # Número de colunas desejado para os gráficos
    num_rows = (num_positions + num_cols - 1) // num_cols  # Cálculo dinâmico das linhas necessárias

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(9, 9), sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    axs = axs.flatten()

    for pos in range(num_positions):
        data = analysis_results.get(pos, [])  # Dados para a posição pos, se disponíveis
        x = [item[0] for item in data]  # Índice do arquivo
        y = [item[1] for item in data]  # Contador

        if data:
            axs[pos].plot(x, y, marker='o', linestyle='-', label=f'Posição {pos}')
        """       
        # Adicionar movimentos ocupados ao gráfico
        for occupied in occupied_positions:
            if occupied[0] == pos:
                axs[pos].text(6, 25.0, occupied[1], fontsize=150, ha='center', va='center', color='red')
        """
        axs[pos].set_title(f'Posição {pos}')
        axs[pos].set_xlabel('Número de jogadas')
        axs[pos].set_ylabel('Possibilidades de Ganhar')
        #axs[pos].legend("Tabela de possibilidades de ganhar em relação a posições")

    plt.tight_layout()
    plt.show()

def heuristic_game_analysis(current_game_state):
    analysis = {}
    busy = []
    
    # Limpar o estado atual (remover espaços)
    clean_current_state = [move for move in current_game_state if move != ' ']
    num_moves_in_state = len(clean_current_state)
    
    possible_moves = []
    for P in range(9):
        if current_game_state[P] == ' ':
            possible_moves.append(P)
        else:
            busy.append((P , current_game_state[P][1]))
    
    if len(busy) % 2 == 0:
        proximonext_to_play = -1
    else:
        proximonext_to_play= 1
    
    for N in range(num_moves_in_state+1, 10):
        # Nome do arquivo CSV
        csv_filename = 'AI_data/{}th_move_permutation_win.csv'.format(N)

        # Função para carregar o arquivo CSV
        def load_winning_moves(filename):
            winning_moves = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    winning_moves.append(row)
            return winning_moves


        # Carregar as jogadas de vitória do arquivo CSV
        winning_moves = load_winning_moves(csv_filename)
        vez_de_jogar = proximonext_to_play
        for future_movement in possible_moves:
            # Criar uma cópia completa do estado atual do jogo e adicionar o movimento futuro
            possible_state_of_the_game = deepcopy(clean_current_state)
            if vez_de_jogar == 1:
                possible_state_of_the_game.append(str(future_movement) + 'x')
            elif vez_de_jogar == -1:
                possible_state_of_the_game.append(str(future_movement) + 'o')
            vez_de_jogar *= -1
            count_matches = 0

            # Loop sobre cada linha das jogadas de vitória
            for winning_move in winning_moves:
                # Limpar a linha atual (remover espaços)
                clean_winning_move = [move for move in winning_move if move != ' ']
                
                # Verificar se todos os elementos do possible_state_of_the_game estão contidos em clean_winning_move
                match_count = 0
                for move in possible_state_of_the_game:
                    if move in clean_winning_move:
                        match_count += 1
                
                # Se todos os elementos do possible_state_of_the_game foram encontrados em clean_winning_move, incrementar a contagem
                if match_count == len(possible_state_of_the_game):
                    count_matches += 1
            
            if future_movement not in analysis:
                analysis[future_movement] = []
            
            analysis[future_movement].append((N, count_matches))

    return analysis , busy

def interpret_HG_analysis(data):
    # Interpretar o resultado da heuristic_game_analysis()
    integrais = []
    good_choices = []
    for key in data.keys():
        soma = 0
        position_data = data[key]
        for coordinate in position_data:
            soma += coordinate[1]
        integrais.append((key,soma))
    larger_integral = (0,0)
    for position_data in integrais:
        if (position_data[1] > larger_integral[1]): 
            larger_integral = position_data
    for position_data in integrais:
        if position_data[1] == larger_integral[1]:
            good_choices.append(position_data)
    print(good_choices)
    choice = random.choice([item[0] for item in good_choices])
    print(choice)
    return choice

# Teste de exemplo com um estado atual representado como uma lista de strings
"""
teste = [' ', ' ', '2o', '3x', '4o', ' ', ' ', ' ', ' ']
print(teste)
resultado, busy = heuristic_game_analysis(teste)
print(resultado , busy)
plot_analysis_results(resultado , busy)
interpret_HG_analysis(resultado)
"""