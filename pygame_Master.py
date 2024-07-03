from vesion_file import *
from All_LIBS import *
from load_config_ini import *
from load_themes_ini import *
from output_utils import *
######## Iniciar Tela Pygame ########
pygame.init()
tela = pygame.display.set_mode((tabu_size[0] + window_status_size[0], tabu_size[1] + window_status_size[1]), 0, 32)
#icone_path = os.path.abspath("C:\\Users\\seu_nome_de_usuario\\Documents\\Imagens\\icone.png")/
pygame.display.set_caption('# NEXT')
icone = pygame.image.load(os.path.abspath(r'Imagens\icon.png'))
pygame.display.set_icon(icone)
hwnd = pygame.display.get_wm_info()["window"]
tela.fill(bg_color)
pygame.font.init() 

