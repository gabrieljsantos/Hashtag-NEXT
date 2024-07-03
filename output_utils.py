from All_LIBS import *
from load_config_ini import *


historico_output = []  # Variável global para histórico de saída

def start_output_txt(vesion):
    """
    Inicia ou atualiza o arquivo 'output.txt' com informações de versão e timestamp.
    """
    global historico_output
    agora = datetime.datetime.now()

    # Verifica se o arquivo existe; se não, cria-o
    nome_arquivo = 'output.txt'
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w'):  # 'w' para criar o arquivo se não existir
            pass

    # Escreve no arquivo
    with open(nome_arquivo, 'a', newline='') as arquivo:
        arquivo.write('\n')
        arquivo.write('\n')
        arquivo.write('****************************************************' + '\n')
        arquivo.write(str(vesion) + '\n')
        arquivo.write('executado em ' + str(agora) + "\n")

    # Atualiza o histórico de saída
    historico_output = ['Hashtag NEXT', vesion, 'Developed by Gabriel J Santos', 'iniciado em ' + str(agora)]

def output(texto):
    """
    Adiciona texto ao histórico de saída e escreve no arquivo 'output.txt'.
    """
    global historico_output
    if texto != 'null':
        historico_output.append(texto)
        with open('output.txt', 'a', newline='') as arquivo:
            arquivo.write(str(texto) + "\n")
    if len(historico_output) >= 10:
        recente_output = historico_output[-10:]  # Obtém os últimos 10 elementos da lista
    else:
        recente_output = historico_output[:]  # Usa a lista inteira se tiver menos de 10 elementos

def render_console(tela):
    """
    Renderiza o histórico de saída na tela do console.
    """
    global historico_output
    folder_fonts = os.path.abspath("fonts")
    fonte = os.path.join(folder_fonts, "consolas.ttf")
    fontesys = pygame.font.SysFont(fonte, 18)
    posy_output = 440
    for string in historico_output:
        output = fontesys.render(string, 1, (150, 150, 150))
        tela.blit(output, (610, posy_output))
        posy_output += 15  # Incrementa a posição vertical para a próxima string

def debug_function(texto, time):
    global debug
    if debug:  # Verifica se a variável global debug é True
        print(texto)
        nome_arquivo = 'Debug.txt'
        if not os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'w'):  # 'w' para criar o arquivo se não existir
                pass
        with open(nome_arquivo, 'a', newline='') as arquivo:
            arquivo.write(str(texto) + "\n")
        sleep(time)