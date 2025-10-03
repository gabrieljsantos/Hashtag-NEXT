from All_LIBS import *

config = configparser.ConfigParser()
config.read('config.ini')

######## Configurações de tamanhos ########
line_size = int(config.get('sizes', 'line_size')) ## Espessura das linhas do tabuleiro
tabu_size = tuple(int(c) for c in config.get('sizes', 'tabu_size').split(',')) ## Tamanho do tabuleiro
line_spacing_x = tabu_size[0]/3 ## Espeçamento horizontal entre as linhas do tabuleiro
line_spacing_y = tabu_size[1]/3 ## Espaçamento vertiical entre as linha do tabuleiro
window_status_size = tuple(int(c) for c in config.get('sizes', 'window_status_size').split(',')) ## Tamanho da aba a lado do tabuleiro, ou seja, a aba de Status.

######## Variáveis Globais ########
debug = config.getboolean('global_variables', 'debug')
tempo_debug = float(config.get('global_variables', 'tempo_debug'))
modo_de_jogo = int(config.get('global_variables', 'modo_de_jogo')) ## Variavel que guarda o modo de jogo
vez_de_jogar = int(config.get('global_variables', 'vez_de_jogar')) ## variavel que define quem começa
win_n_o = int(config.get('global_variables', 'win_n_o')) ## Variável que armazenam o score do o
win_n_x = int(config.get('global_variables', 'win_n_x')) ## Variável que armazenam o score do x
finalizado = config.getboolean('global_variables', 'finalizado')

jogadas=[ ## Valores para o tabuleiro limpo
    ' ' , ' ' , ' ',
    ' ' , ' ' , ' ',
    ' ' , ' ' , ' '
    ]

### Combinações para ganhar
x_win = [tuple(pos.split(',')) for pos in config.get('posi_win', 'x_win').split(';')]
o_win = [tuple(pos.split(',')) for pos in config.get('posi_win', 'o_win').split(';')]
