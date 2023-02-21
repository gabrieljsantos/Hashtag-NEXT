import random
import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import VerticalSeparator
sg.theme('darkAmber')
class TelaPython:
    def __init__(self):
        layout = [
            [sg.Output(size=(90,5))]
        ]
        self.janela = sg.Window("INFINITY KEY").layout(layout)

    def Iniciar(self):
        while True :
            evento, values = self.janela.Read()
            if evento == sg.WINDOW_CLOSED:
                break


            
    
tela = TelaPython()
tela.Iniciar()

