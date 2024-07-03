from main import *
from All_LIBS import *


for N in range(10) :
    permsNthMoveNumeric = list(permutations(range(9), N))
    permsNthMove = []
    for perm in permsNthMoveNumeric:
        vez_de_jogar = -1
        permutaDeJogadas = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '
        ]
        
        for choice in perm:
            if vez_de_jogar == 1:
                permutaDeJogadas[choice] = str(choice) + 'x'
            elif vez_de_jogar == -1:
                permutaDeJogadas[choice] = str(choice) + 'o'
            vez_de_jogar *= -1
        resultado = veri_win(permutaDeJogadas)
        if isinstance(resultado, tuple) and resultado[0] == 'o':
            permsNthMove.append(permutaDeJogadas)
            # print(permutaDeJogadas)


    filename = 'AI_data/{}th_move_permutation_win.csv'.format(N)
    # Escrevendo os dados no arquivo CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(permsNthMove)

from collections import defaultdict

def clean_csv_duplicates(filename):
    unique_combinations = defaultdict(set)
    
    # Ler o arquivo CSV e armazenar combinações únicas em um dicionário
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Converter a linha em uma tupla para facilitar a comparação e armazenamento
            combination = tuple(row)
            unique_combinations[len(combination)].add(combination)
    
    # Escrever as combinações únicas de volta para o arquivo CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for combinations_set in unique_combinations.values():
            for combination in combinations_set:
                writer.writerow(combination)

# Exemplo de uso:
for N in range(10):
    filename = f'AI_data/{N}th_move_permutation_win.csv'
    clean_csv_duplicates(filename)




