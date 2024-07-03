def jogada_inicial_estrategica(): ## Define jogas aleatrias estrategias iniciais
    debug_function('jogada_inicial_estrategica()' , tempo_debug)
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