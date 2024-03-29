vesion = 'v1.0.1'

# -*- coding: utf-8 -*-
######## Impotação de bibliotecas ########
from functools import partial
from telnetlib import LOGOUT
from base64 import b16encode
from pygame.locals import * # MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from PySimpleGUI.PySimpleGUI import VerticalSeparator
from time import sleep
from load_config_ini import *
from load_themes_ini import *
#from tkinter import*

import random
import os
import pygame
import re
import win32api
import win32con
import win32gui
import datetime

# Obtenha a data e hora atuais
agora = datetime.datetime.now()
with open('output.txt','a',newline='') as arquivo:
    arquivo.write('\n')
    arquivo.write('\n')
    arquivo.write('****************************************************' + '\n')
    arquivo.write(str(vesion) + '\n')
    arquivo.write('excutado em '+ str(agora) + "\n")

'''
# Acesse os atributos da data e hora para obter as informações desejadas
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second
'''
historico_output = ['Hashtag NEXT', vesion ,'Developed by Gabriel J Santos','iniciado em ' + str(agora)]
finalizado = False
######## Iniciar Tela Pygame ########
pygame.init()
tela = pygame.display.set_mode((tabu_size[0] + window_status_size[0], tabu_size[1] + window_status_size[1]), 0, 32)
#icone_path = os.path.abspath("C:\\Users\\seu_nome_de_usuario\\Documents\\Imagens\\icone.png")/
pygame.display.set_caption('# NEXT')
icone = pygame.image.load(os.path.abspath(r'Imagens\icon.png'))
pygame.display.set_icon(icone)
hwnd = pygame.display.get_wm_info()["window"]
#hicon = win32gui.LoadImage(0, os.path.abspath(r'Imagens\icon.png'), win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
#win32api.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, hicon)
tela.fill(bg_color)
pygame.font.init() 

######## Funções ########
def output(texto):
    global historico_output
    if texto != 'null':
        historico_output.append(texto)
        with open('output.txt','a',newline='') as arquivo:
            arquivo.write(str(texto) + "\n")
    if len(historico_output) >= 10:
        # usa slicing para obter os últimos 4 elementos da lista
        recente_output = historico_output[-10:]
    else:
        # se a lista tiver menos de 4 elementos, usa a lista inteira
         recente_output = historico_output
    folder_fonts = os.path.abspath("fonts")
    fonte= os.path.join(folder_fonts, "consolas.ttf")
    fontesys=pygame.font.SysFont(fonte, 18)
    posy_output = 440
    for string in recente_output:
        output = fontesys.render(string , 1, (150, 150, 150))
        tela.blit(output,(610,posy_output))
        posy_output += 15  # incrementa a posição vertical para a próxima string  

def debug_funcion(texto,time):
    global debug
    if debug == True:
        print (texto)
        with open('Debug.txt','a',newline='') as arquivo:
            arquivo.write(str(texto) + "\n")
        sleep(time)

def rgb_color(rgb): ## Converter RGB para HEX
    debug_funcion('rgb_color(rgb)', tempo_debug)
    return(b'#' + b16encode(bytes(rgb)))
    
def desenhar_tabu(): ## Desenhar linhas do tabuleiro
    debug_funcion('desenhar_tabu()', tempo_debug)
    for i in range (4):
        pygame.draw.line(tela, line_color, (i*line_spacing_x, 0), (i*line_spacing_x, tabu_size[1]), line_size)
        pygame.draw.line(tela, line_color, (0, i*line_spacing_y), (tabu_size[0], i*line_spacing_y), line_size)

def limpar_tabu(): ## limpar o tabuleiro
    debug_funcion('limpar_tabu()', tempo_debug)
    output('Tabuleiro limpo')
    global jogadas
    jogadas=[
    ' ' , ' ' , ' ',
    ' ' , ' ' , ' ',
    ' ' , ' ' , ' '
    ]
    


def desenhar_x (posx,posy): ## Desenhar o X
    debug_funcion(('desenhar_x ', str(posx), str(posy)), tempo_debug)
    posx = posx - 100
    posy = posy - 100
    pygame.draw.polygon(tela, x_color, ((22+posx,38+posy), (38+posx,22+posy) , (178+posx,162+posy) , (162+posx,178+posy)))
    pygame.draw.polygon(tela, x_color, ((22+posx,162+posy), (38+posx,178+posy) , (178+posx,38+posy) , (162+posx,22+posy)))

def desenhar_o (posx,posy): ## Desenhar o circulo/bola
    debug_funcion(('desenhar_o ', str(posx), str(posy)), tempo_debug)
    pygame.draw.circle(tela, circle_color, (posx,posy), 79, width=24)

def desenhar_score(): ## Desenhar a janela de Score
    debug_funcion('desenhar_score()', tempo_debug)
    global win_n_o
    global win_n_x

    fonte=pygame.font.get_default_font()
    ## definindo tamanho da fonte em função do valor de win_n_
    if win_n_o >= 1000:
        size_fonte = 55
    elif win_n_o >= 100:
        size_fonte = 75
    elif win_n_o >= 10:
        size_fonte = 100
    else:
        size_fonte = 150

    fontesys=pygame.font.SysFont(fonte, size_fonte)
    score_o = fontesys.render(str(win_n_o) , 1, (score_value_color)) 
    largura_texto, altura_texto = score_o.get_size() # Obtenha as dimensões do texto
    rect_texto = score_o.get_rect(centerx=650, centery=250)# Crie um objeto Rect para centralizar o texto na posição
    tela.blit(score_o,rect_texto)

    ## definindo tamanho da fonte em função do valor de win_n_
    if win_n_x >= 1000:
        size_fonte = 55
    elif win_n_x >= 100:
        size_fonte = 75
    elif win_n_x >= 10:
        size_fonte = 100
    else:
        size_fonte = 150
    
    fontesys=pygame.font.SysFont(fonte, size_fonte)
    score_x = fontesys.render(str(win_n_x) , 1, (score_value_color)) 
    largura_texto, altura_texto = score_x.get_size() # Obtenha as dimensões do texto
    rect_texto = score_x.get_rect(centerx=950, centery=250)# Crie um objeto Rect para centralizar o texto na posição
    tela.blit(score_x,rect_texto)

def desenhar_aba_status(): ## Desenha a Aba de Status lateral
    global vez_de_jogar
    debug_funcion('desenhar_aba_status()', tempo_debug)
    LOGO_FILE = os.path.abspath(r'Imagens\LOGO3.png')
    LOGO = pygame.image.load(LOGO_FILE).convert_alpha()
    tela.blit(LOGO,(600,0))
    
    pygame.font.init() 

    txt_Developed_by= ('Developed by')
    txt_Gabriel_J_Santos= ('Gabriel J Santos')
    
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 26)
    Developed_by = fontesys.render(txt_Developed_by , 1, (0, 0, 0)) 
    Gabriel_J_Santos = fontesys.render(txt_Gabriel_J_Santos , 1, (255, 0, 0)) 
    posx = 612
    posy = 106
    tela.blit(Developed_by,(posx,posy))
    tela.blit(Gabriel_J_Santos,(posx+117,posy))

    fonte=pygame.font.get_default_font()
    txt_vesion= (vesion) ## terxo titulo da região score
    fontesys=pygame.font.SysFont(fonte, 50)
    vesion_pygame = fontesys.render(txt_vesion , 1, (score_title_color)) 
    largura_texto, altura_texto = vesion_pygame.get_size()
    rect_texto = vesion_pygame.get_rect(centerx=936, centery=120)
    tela.blit(vesion_pygame, rect_texto)

    fonte=pygame.font.get_default_font()
    txt_score_title= ('*********** SCORE ***********') ## terxo titulo da região score
    fontesys=pygame.font.SysFont(fonte, 40)
    score_title = fontesys.render(txt_score_title , 1, (score_title_color)) 
    largura_texto, altura_texto = score_title.get_size()
    rect_texto = score_title.get_rect(centerx=800, centery=175)
    tela.blit(score_title, rect_texto)
    
    ### seleciona na aba de status de quem será a jogada
    if vez_de_jogar == 1: 
        lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (800, 200, 100, 100))
    if vez_de_jogar == -1:
        lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (700, 200, 100, 100))
        
    ## desenhar circulo da aba de status
    pygame.draw.circle(tela, circle_color, (750,250), 34, width=12)
    ## desenhar o x da aba de status
    pygame.draw.polygon(tela, x_color, ((810,281), (819,290) , (890,219) , (881,210)))
    pygame.draw.polygon(tela, x_color, ((819,210), (810,219) , (881,290) , (890,281)))

    desenhar_score() 

def selecionar(): ## Marcar a seleção e retorna o bloco selecionado
    
    debug_funcion('selecionar()', tempo_debug)
    global jogadas
    posision = pygame.mouse.get_pos()
    selecion_x=posision[0]//line_spacing_x
    selecion_y=posision[1]//line_spacing_y
    tela.fill(bg_color)
    if selecion_x > 2:
        return 'null'
    if (pygame.mouse.get_focused() == True) :
        if (posision[0] <= tabu_size[0]):
            if jogadas[int(selecion_x+ selecion_y*3)] == ' ':
                lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (selecion_x * line_spacing_x, selecion_y  * line_spacing_y, line_spacing_x, line_spacing_y))
                return int(selecion_x+ selecion_y*3)
            if jogadas[int(selecion_x+ selecion_y*3)] != ' ':
                return 'null'

def selecionar_vitoria(positions=[]): ## Marcar as posições de vitória
    positions= (int(positions[0][0]),int(positions[1][0]),int(positions[2][0]))
    selecion_x = 0
    for n in range (3) :
        selecion_y = int(positions[n]/3)
        selecion_x = (positions[n])%3
        lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_vitoria, (selecion_x * line_spacing_x, selecion_y  * line_spacing_y, line_spacing_x, line_spacing_y))

def mudar_jogador(): ## Inverter jogador.
    debug_funcion('mudar_jogador()', tempo_debug)
    global vez_de_jogar
    vez_de_jogar = vez_de_jogar * -1

def clicar(): ## Gerencia o processo de clique no tabuleiro
    debug_funcion('clicar()' , tempo_debug)
    global jogadas
    global vez_de_jogar
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and selecionar() != 'null':

            ### verificador de quem está jogando
            if vez_de_jogar == 1 :
                seletion = selecionar()
                jogadas[seletion] = (str(seletion)+'x')
            if vez_de_jogar == -1 :
                seletion = selecionar()
                jogadas[seletion] = (str(seletion)+'o')
            mudar_jogador()

def machine_choice(vez_de_jogar): ## Define a jogada da maquina
    debug_funcion('machine_choice()' , tempo_debug)
    global finalizado 
    if finalizado == False:
        choice = jogada_random()
        if jogada_inicial_estrategica() != -1:
            choice = jogada_inicial_estrategica()
        if vez_de_jogar == 1 :
            jogadas[choice] = (str(choice)+'x')
        if vez_de_jogar == -1 :
            jogadas[choice] = (str(choice)+'o')
        mudar_jogador()

def sair(): ## Função que fecha o programa
    debug_funcion('sair()' , tempo_debug)
    for u in pygame.event.get():
        if u.type == QUIT:
            pygame.quit()
            exit()

def desenhar_jogadas(): ## Desenhar com base nas jogadas já realizadas
    debug_funcion('desenhar_jogadas()' , tempo_debug)
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
    debug_funcion('veri_win(elementos=[])' , tempo_debug)
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
            
def jogada_random(): ## Define jogada aleatoria
    debug_funcion('jogada_random()' , tempo_debug)
    if ' ' in jogadas:
        random_value = random.randint(0,8)
        output('Escolhendo aleatoriamente = '+ str(random_value))
        if jogadas[random_value] != ' ' :
            output ('Posição ocupada, corrigindo...')
            while jogadas[random_value] != ' ':
                random_value = random_value + 1
                if random_value >= 9 :
                    random_value = 0
            output('Valor corrigido = '+ str(random_value))
        return random_value

def jogada_inicial_estrategica(): ## Define jogas aleatrias estrategias iniciais
    debug_funcion('jogada_inicial_estrategica()' , tempo_debug)
    melhores_jogadas_iniciais=[0 , 2 , 4 , 6 , 8]
    random_value = melhores_jogadas_iniciais[random.randint(0,4)]
    output('Escolhendo aleatoriamente uma melhor jogada inicial = '+ str(random_value))
    ocupado_completamente = 0
    if jogadas[random_value] != ' ' :
        output ('Posição ocupada, corrigindo...')
        while jogadas[random_value] != ' ' and ocupado_completamente < 6:
            random_value = random_value + 2
            ocupado_completamente = ocupado_completamente + 1
            if random_value >= 9 :
                random_value = 0
        if ocupado_completamente < 6 :
            output('Valor estrategico inicial corrigido = '+ str(random_value))
    if ocupado_completamente > 5 :
        random_value = - 1
        output('Todas as posições estrategicas iniciais estão ocupadas')
    return random_value





def reaction_win(): ## Reação para fim de jogo
    debug_funcion('reaction_win()' , tempo_debug)
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

### Loop principal com todas as funções
while True :
    debug_funcion('while True' , tempo_debug)
    if modo_de_jogo == 1 :
        sair()
    if modo_de_jogo == 2 :
        if vez_de_jogar == 1 :
            sair()
            clicar()
            selecionar()
            clicar()
            selecionar()
            clicar()
        elif vez_de_jogar == -1 :
            sair()
            machine_choice(vez_de_jogar)
    if modo_de_jogo == 3:
        sleep(0.2)
        if vez_de_jogar == 1 :
            sair()
            machine_choice(vez_de_jogar)
        elif vez_de_jogar == -1 :
            sair()
            machine_choice(vez_de_jogar)

    if modo_de_jogo == 4:
        clicar()
        sair()
        clicar()
        selecionar()
        clicar()
    
    if finalizado == False:
        tela.fill(bg_color)
        output('null')
        reaction_win()
        desenhar_aba_status()
        desenhar_jogadas()
        desenhar_tabu()
        pygame.display.update()
        pygame.display.flip()

    if finalizado == True:
        pygame.display.update()
        sleep(0.5)
        limpar_tabu()
        finalizado = False
        tela.fill(bg_color)
        output('Finalizado')
        desenhar_aba_status()
        desenhar_tabu()
        pygame.display.update()
        #pygame.display.flip()
    
    