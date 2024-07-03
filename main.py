from vesion_file import *
from All_LIBS import *

# -*- coding: utf-8 -*-
from load_config_ini import *
from load_themes_ini import *
from pygame_Master import *
from AI_heuristic_game_analysis import*
from output_utils import *



def machine_choice(vez_de_jogar,type): ## Define a jogada da maquina
    debug_function('machine_choice()' , tempo_debug)
    global finalizado 
    if finalizado == False:
        if type == "hga":
            dados, busy = heuristic_game_analysis(jogadas)
            print(dados)
            choice = interpret_HG_analysis(dados)
        if type == "jie":
            choice = jogada_random()
            if jogada_inicial_estrategica() != -1:
                choice = jogada_inicial_estrategica()
        if vez_de_jogar == 1 :
            jogadas[choice] = (str(choice)+'x')
        if vez_de_jogar == -1 :
            jogadas[choice] = (str(choice)+'o')
        mudar_jogador()

def sair(): ## Função que fecha o programa
    debug_function('sair()' , tempo_debug)
    for u in pygame.event.get():
        if u.type == QUIT:
            pygame.quit()
            exit()

def desenhar_jogadas(): ## Desenhar com base nas jogadas já realizadas
    debug_function('desenhar_jogadas()' , tempo_debug)
    global jogadas
    posy = 0
    corretion_x = 0
    for i in range (9):
        
        ### Aqui será definido em qual linha o desenho deve aparecer , basicamente uma quebra de linha
        if i == 3 :
            posy = posy + 200
            corretion_x = corretion_x + 600
        if i == 6:
            posy = posy + 200
            corretion_x = corretion_x + 600

        ### Aqui será feito a escolha de qual desenho deve ser feito com base nos dados da lista "jogadas[]"
        if re.match('[0-9]x$',jogadas[i]):
            desenhar_x(100 - corretion_x + 200*i ,100+posy)
        if re.match('[0-9]o$',jogadas[i]):
            desenhar_o(100 - corretion_x + 200*i ,100+posy)

def veri_win(elementos=[]): ## Verificador de ganhador
    debug_function('veri_win(elementos=[])' , tempo_debug)
    ### Combinações para ganhar
    global x_win
    global o_win
    
    ### Função que testa se existe alguma combinação de vitoria dentro das jogadas
    run_True = True
    for n in range (8) :
        ### Função que verifica se alguém ganhou
        if set(x_win[n])  <= set(elementos):
            run_True = False
            return ('x' , x_win[n])
        if set(o_win[n])  <= set(elementos):
            run_True = False
            return ('o' , o_win[n])
        # Verifica se todas as jogadas foram feitas

    if (run_True) & (' ' in elementos):
        # Se todas as jogadas foram feitas e não houve vencedor, retorna empate        
        run_True = True
    else:
        return ('#', '#')
    # Se o loop terminar sem retornar, não houve vencedor nem empate
    return 'null'
            








def reaction_win(): ## Reação para fim de jogo
    debug_function('reaction_win()' , tempo_debug)
    global jogadas
    global win_n_o
    global win_n_x
    global finalizado
    global vez_de_jogar
    vencendor = veri_win(jogadas)
    if vencendor != 'null':
        if vencendor[0] == 'o':
            win_n_o = win_n_o +1 
            output('O ganhou e esta com '+ str(win_n_o)+ ' pontos')
            selecionar_vitoria(vencendor[1])
            vez_de_jogar = -1
  
        if vencendor[0] == 'x':
            win_n_x = win_n_x +1 
            output('X ganhou e esta com '+ str(win_n_x)+ ' pontos')
            selecionar_vitoria(vencendor[1])
            vez_de_jogar = 1
        finalizado = True

    if vencendor[0] == '#':
        output ('Empate')
        finalizado = True
        sleep(2)  


#def game_routine():
### Loop principal com todas as funções
while True:
    debug_function('while True', tempo_debug)
    
    # Bloco 1 - Lógica do Jogo
    if modo_de_jogo == 1:
        if vez_de_jogar == 1:
            sair()
            clicar()
            selecionar()
            clicar()
            selecionar()
            clicar()
        elif vez_de_jogar == -1:
            sair()
            machine_choice(vez_de_jogar, "hga")
    
    elif modo_de_jogo == 2:
        if vez_de_jogar == 1:
            sair()
            clicar()
            selecionar()
            clicar()
            selecionar()
            clicar()
        elif vez_de_jogar == -1:
            sair()
            machine_choice(vez_de_jogar, "jie")
    
    elif modo_de_jogo == 3:
        sleep(0.2)
        if vez_de_jogar == 1:
            sair()
            machine_choice(vez_de_jogar, "jie")
        elif vez_de_jogar == -1:
            sair()
            machine_choice(vez_de_jogar, "jie")
    
    elif modo_de_jogo == 4:
        clicar()
        sair()
        clicar()
        selecionar()
        clicar()
    
    # Bloco 2 - Renderização Gráfica
    if finalizado:
        pygame.display.update()
        sleep(0.5)
        limpar_tabu()
        finalizado = False
        tela.fill(bg_color)
        output('Finalizado')
    
    tela.fill(bg_color)
    output('null')
    reaction_win()
    desenhar_aba_status()
    desenhar_jogadas()
    desenhar_tabu()
    pygame.display.update()