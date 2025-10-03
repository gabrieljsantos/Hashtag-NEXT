from pygame_Master import *

def desenhar_x (posx,posy): ## Desenhar o X
    debug_function(('desenhar_x ', str(posx), str(posy)), tempo_debug)
    posx = posx - 100
    posy = posy - 100
    pygame.draw.polygon(tela, x_color, ((22+posx,38+posy), (38+posx,22+posy) , (178+posx,162+posy) , (162+posx,178+posy)))
    pygame.draw.polygon(tela, x_color, ((22+posx,162+posy), (38+posx,178+posy) , (178+posx,38+posy) , (162+posx,22+posy)))

def desenhar_o (posx,posy): ## Desenhar o circulo/bola
    debug_function(('desenhar_o ', str(posx), str(posy)), tempo_debug)
    pygame.draw.circle(tela, circle_color, (posx,posy), 79, width=24)

def desenhar_score(): ## Desenhar a janela de Score
    debug_function('desenhar_score()', tempo_debug)
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
    debug_function('desenhar_aba_status()', tempo_debug)
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
    

def desenhar_selecao(index):
    """
    Usa o índice retornado pela função selecionar para desenhar a seleção na tela.
    """
    if index != 'null':
        selecion_x = index % 3
        selecion_y = index // 3
        lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_color, (selecion_x * line_spacing_x, selecion_y * line_spacing_y, line_spacing_x, line_spacing_y))

def selecionar_vitoria(positions=[]): ## Marcar as posições de vitória
    positions= (int(positions[0][0]),int(positions[1][0]),int(positions[2][0]))
    selecion_x = 0
    for n in range (3) :
        selecion_y = int(positions[n]/3)
        selecion_x = (positions[n])%3
        lugar_selecionado = pygame.draw.rect(tela, retangulo_sele_vitoria, (selecion_x * line_spacing_x, selecion_y  * line_spacing_y, line_spacing_x, line_spacing_y))


def draw_board_line(): ## Desenhar linhas do tabuleiro
    debug_function('desenhar_tabu()', tempo_debug)
    for i in range (4):
        pygame.draw.line(tela, line_color, (i*line_spacing_x, 0), (i*line_spacing_x, tabu_size[1]), line_size)
        pygame.draw.line(tela, line_color, (0, i*line_spacing_y), (tabu_size[0], i*line_spacing_y), line_size)