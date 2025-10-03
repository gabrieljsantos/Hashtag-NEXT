vesion = 'v1.0.1'

# -*- coding: utf-8 -*-
######## Impotação de bibliotecas ########
from functools import partial
from telnetlib import LOGOUT
from base64 import b16encode
from pygame.locals import * # MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from time import sleep
from load_config_ini import *
from load_themes_ini import *
from AI_heuristic_game_analysis import*
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

def mudar_jogador(): ## Inverter jogador.
    debug_funcion('mudar_jogador()', tempo_debug)
    global vez_de_jogar
    vez_de_jogar = vez_de_jogar * -1


def sair(): ## Função que fecha o programa
    debug_funcion('sair()' , tempo_debug)
    for u in pygame.event.get():
        if u.type == QUIT:
            pygame.quit()
            exit()


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
 
