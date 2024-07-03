from pygame_Master import *

def selecionar(current_game_state):
    """
    Marca a seleção na tela e retorna o índice do bloco selecionado ou 'null' se nenhum bloco válido for selecionado.
    """
    global jogadas
    posision = pygame.mouse.get_pos()
    selecion_x = posision[0] // line_spacing_x
    selecion_y = posision[1] // line_spacing_y
    tela.fill(bg_color)

    if selecion_x > 2:
        return 'null'
    
    if pygame.mouse.get_focused():
        if posision[0] <= tabu_size[0]:
            index = int(selecion_x + selecion_y * 3)
            if current_game_state[index] == ' ':
                lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (selecion_x * line_spacing_x, selecion_y * line_spacing_y, line_spacing_x, line_spacing_y))
                return index
            else:
                return 'null'
    return 'null'  # Retorna 'null' por padrão se nenhuma condição anterior for atendida

def clicar(seletion,time_to_play): ## Gerencia o processo de clique no tabuleiro
    global jogadas
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and seletion != 'null':
            ### verificador de quem está jogando
            if time_to_play == 1 :
                jogadas[seletion] = (str(seletion)+'x')
            if time_to_play == -1 :
                jogadas[seletion] = (str(seletion)+'o')
            