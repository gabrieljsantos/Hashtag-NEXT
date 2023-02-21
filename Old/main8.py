# -*- coding: utf-8 -*-
######## Impotação de bibliotecas ########
from functools import partial
from telnetlib import LOGOUT
from base64 import b16encode
from pygame.locals import * # MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from PySimpleGUI.PySimpleGUI import VerticalSeparator
from time import sleep
#from tkinter import*
import random

import os
import pygame
import re
import win32api
import win32con
import win32gui
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

######## Configurações de cores ########
bg_color = tuple(int(c) for c in config.get('colors', 'bg_color').split(','))
line_color = tuple(int(c) for c in config.get('colors', 'line_color').split(','))
retangulo_sele_color = tuple(int(c) for c in config.get('colors', 'retangulo_sele_color').split(','))
retangulo_sele_vitoria = tuple(int(c) for c in config.get('colors', 'retangulo_sele_vitoria').split(','))
x_color = tuple(int(c) for c in config.get('colors', 'x_color').split(','))
circle_color = tuple(int(c) for c in config.get('colors', 'circle_color').split(','))
score_value_color = tuple(int(c) for c in config.get('colors', 'score_value_color').split(','))
score_title_color = tuple(int(c) for c in config.get('colors', 'score_title_color').split(','))

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


######## Iniciar Tela Pygame ########
pygame.init()
tela = pygame.display.set_mode((tabu_size[0] + window_status_size[0], tabu_size[1] + window_status_size[1]), 0, 32)
icone_path = os.path.abspath("C:\\Users\\seu_nome_de_usuario\\Documents\\Imagens\\icone.png")
pygame.display.set_caption('# NEXT')
icone = pygame.image.load(os.path.abspath(r'Imagens\icon.png'))
pygame.display.set_icon(icone)
hwnd = pygame.display.get_wm_info()["window"]
hicon = win32gui.LoadImage(0, os.path.abspath(r'Imagens\icon.ico'), win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
win32api.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, hicon)
tela.fill(bg_color)
pygame.font.init() 

######## Funções ########
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

def desenhar_aba_score(): ## Desenhar a janela de Score
    debug_funcion('desenhar_aba_score()', tempo_debug)
    global win_n_o
    global win_n_x
    txt_score_title= ('*********** SCORE ***********')
    txt_score_valores=(str(win_n_x)+ ' - ' +  str(win_n_o))
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 40)
    score_title = fontesys.render(txt_score_title , 1, (score_title_color)) 
    tela.blit(score_title,(625,120))

    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 160)
    score_valores = fontesys.render(txt_score_valores , 1, (score_value_color)) 
    tela.blit(score_valores,(700,200))

def desenhar_aba_status(): ## Desenha a Aba de Status lateral
    debug_funcion('desenhar_aba_status()', tempo_debug)
    LOGO_FILE = os.path.abspath(r'Imagens\LOGO.png')
    LOGO = pygame.image.load(LOGO_FILE)
    tela.blit(LOGO,(600,0))
    desenhar_aba_score()

    txt_Developed_by= ('Developed by')
    txt_Gabriel_J_Santos= ('Gabriel J Santos')
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 20)
    Developed_by = fontesys.render(txt_Developed_by , 1, (0, 0, 0)) 
    Gabriel_J_Santos = fontesys.render(txt_Gabriel_J_Santos , 1, (255, 0, 0)) 
    posx = 780
    posy = 580
    tela.blit(Developed_by,(posx,posy))
    tela.blit(Gabriel_J_Santos,(posx+95,posy))

def selecionar(): ## Marcar a seleção e retorna o bloco selecionado
    
    debug_funcion('selecionar()', tempo_debug)
    global jogadas
    posision = pygame.mouse.get_pos()
    selecion_x=posision[0]//line_spacing_x
    selecion_y=posision[1]//line_spacing_y
    tela.fill(bg_color)
    if (pygame.mouse.get_focused() == True) :
        if (posision[0] <= tabu_size[0]):
            if jogadas[int(selecion_x+ selecion_y*3)] == ' ':
                lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (selecion_x * line_spacing_x, selecion_y  * line_spacing_y, line_spacing_x, line_spacing_y))
                return int(selecion_x+ selecion_y*3)
            if jogadas[int(selecion_x+ selecion_y*3)] != ' ':
                return 'null'

def selecionar_vitoria(positions=[]): ## Marcar as posições de vitória
    debug_funcion('selecionar_vitoria(positions=[])', tempo_debug)
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
            desenhar_tabu()
            desenhar_jogadas()

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
        desenhar_tabu()
        desenhar_jogadas()
        pygame.display.update()
        pygame.display.flip()
        sleep(0.3)

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
    for n in range (8) :
        run_True = True
        ### Função que verifica se alguem ganhou
        if ' ' not in  elementos:
            run_True = False
            return ('#' , '#')
        if set(x_win[n])  <= set(elementos):
            run_True = False
            return ('x' , x_win[n])
        if set(o_win[n])  <= set(elementos):
            run_True = False
            return ('o' , o_win[n])
        
        if run_True == True and n == 7:
            return 'null'
            
def jogada_random(): ## Define jogada aleatoria
    debug_funcion('jogada_random()' , tempo_debug)
    if ' ' in jogadas:
        random_value = random.randint(0,8)
        print('Escolhendo aleatoriamente = ', random_value)
        if jogadas[random_value] != ' ' :
            print ('Posição ocupada, corrigindo...')
            while jogadas[random_value] != ' ':
                random_value = random_value + 1
                if random_value >= 9 :
                    random_value = 0
            print('Valor corrigido = ', random_value)
        return random_value

def jogada_inicial_estrategica(): ## Define jogas aleatrias estrategias iniciais
    debug_funcion('jogada_inicial_estrategica()' , tempo_debug)
    melhores_jogadas_iniciais=[0 , 2 , 4 , 6 , 8]
    random_value = melhores_jogadas_iniciais[random.randint(0,4)]
    print('Escolhendo aleatoriamente uma melhor jogada inicial = ', random_value)
    ocupado_completamente = 0
    if jogadas[random_value] != ' ' :
        print ('Posição ocupada, corrigindo...')
        while jogadas[random_value] != ' ' and ocupado_completamente < 6:
            random_value = random_value + 2
            ocupado_completamente = ocupado_completamente + 1
            if random_value >= 9 :
                random_value = 0
        if ocupado_completamente < 6 :
            print('Valor estrategico inicial corrigido = ', random_value)
    if ocupado_completamente > 5 :
        random_value = - 1
        print('Todas as posições estrategicas iniciais estão ocupadas')
    return random_value

def new_partida(): ## Inicia uma nova partida
    debug_funcion('new_partida()' , tempo_debug)
    desenhar_tabu()
    clicar()
    desenhar_jogadas()
    pygame.display.update()
    pygame.display.flip()   
    sleep(2)
    limpar_tabu()

def reaction_win(): ## Reação para fim de jogo
    debug_funcion('reaction_win()' , tempo_debug)
    global jogadas
    global win_n_o
    global win_n_x
    global finalizado
    vencendor = veri_win(jogadas)
    print(veri_win(jogadas))
    if vencendor != 'null':
        if vencendor[0] == 'o':
            win_n_o = win_n_o +1 
            print ('O ganhou e esta com', win_n_o, 'pontos')
            selecionar_vitoria(vencendor[1])
  
        if vencendor[0] == 'x':
            win_n_x = win_n_x +1 
            print ('X ganhou e esta com', win_n_x, 'pontos')
            selecionar_vitoria(vencendor[1])
        finalizado = True
        new_partida()

    if vencendor[0] == '#':
        print ('#')
        new_partida()

### Loop principal com todas as funções
while True :
    debug_funcion('while True' , tempo_debug)
    if modo_de_jogo == 1 :
        sair()
    if modo_de_jogo == 2 :
        if vez_de_jogar == 1 :
            sair()
        if vez_de_jogar == -1 :
            sair()
    if modo_de_jogo == 3:
        if vez_de_jogar == 1 :
            sair()
            machine_choice(vez_de_jogar)
            desenhar_aba_score()
            desenhar_aba_status()
        if vez_de_jogar == -1 :
            sair()
            machine_choice(vez_de_jogar)
            desenhar_aba_score()
            desenhar_aba_status()
    if modo_de_jogo == 4:
        sair()
        desenhar_aba_score()
        desenhar_aba_status()
        clicar()
        selecionar()
        clicar()
        reaction_win()
    reaction_win()
    desenhar_tabu()
    desenhar_jogadas()
    desenhar_aba_score()
    desenhar_aba_status()

    pygame.display.update()
    pygame.display.flip()
    
    