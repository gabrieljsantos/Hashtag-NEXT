from Functions import *
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
    
    