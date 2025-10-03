from All_LIBS import *
def choice_random(current_game_state):
    if ' ' in current_game_state:
        possible_moves = [index for index, value in enumerate(current_game_state) if value == ' ']
        if possible_moves:
            random_value = random.choice(possible_moves)
            return random_value
    return 'null'