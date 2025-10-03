import configparser

themes = configparser.ConfigParser()
themes.read('themes.ini')

######## themesurações de cores ########
theme = str(themes.get('set_theme', 'theme')) 

bg_color = tuple(int(c) for c in themes.get(theme, 'bg_color').split(','))
line_color = tuple(int(c) for c in themes.get(theme, 'line_color').split(','))
retangulo_sele_color = tuple(int(c) for c in themes.get(theme, 'retangulo_sele_color').split(','))
retangulo_sele_vitoria = tuple(int(c) for c in themes.get(theme, 'retangulo_sele_vitoria').split(','))
x_color = tuple(int(c) for c in themes.get(theme, 'x_color').split(','))
circle_color = tuple(int(c) for c in themes.get(theme, 'circle_color').split(','))
score_value_color = tuple(int(c) for c in themes.get(theme, 'score_value_color').split(','))
score_title_color = tuple(int(c) for c in themes.get(theme, 'score_title_color').split(','))

