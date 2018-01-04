# tica tac toe
#


def get_printable_symbol(symbol):
    if symbol == 0:
        return ' '
    else:
        return symbol


def print_board(state):
    for row in state:
        print_row = '{first}|{second}|{third}'.format(first=get_printable_symbol(
            row[0]), second=get_printable_symbol(row[1]), third=get_printable_symbol(row[2]))
        print(print_row)
        print('-----')


def get_player(turn):
    return (turn % 2) + 1


def get_player_symbol(player):
    if player == 1:
        return 'X'
    else:
        return 'O'


def set_symbol(state, symbol, coords):
    # Check is symbol already at that place
    if state[coords[0]][coords[1]] != 0:
        print('Those coordinates are already taken. Chose again please')
        return {'success': 0, 'state': state}
    else:
        state[coords[0]][coords[1]] = symbol
        return {'success': 1, 'state': state}


def get_next_play(state, i):
    player = get_player(i)
    symbol = get_player_symbol(player)
    result = {'success': 0}
    while result['success'] == 0:
        print('Player {pl} turn'.format(pl=player))
        print('Enter your symbol coordinates ({pl_sym})'.format(pl_sym=symbol))
        x = int(input('Row Coordinates of your play:')) - 1
        y = int(input('Col Coordinates of your play:')) - 1
        coords = [x, y]
        result = set_symbol(state, symbol, coords)
    return result['state']


def is_the_game_done(state):
    for i in range(0, 3):
        # Check row
        if (len(set(state[i])) == 1 and state[i][0] != 0):
            return 1
        # Check column
        colmn = [state[y][i] for y in range(0, 3)]
        if (len(set(colmn)) == 1 and colmn[0] != 0):
            return 1
    # Check cross
    forw_cross = [state[i][i] for i in range(0, 3)]
    if (len(set(forw_cross)) == 1 and state[1][1] != 0):
        return 1
    back_cross = [state[i][2 - i] for i in range(0, 3)]
    if (len(set(back_cross)) == 1 and state[1][1] != 0):
        return 1
    return 0


def start_game():
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print('Coordinates are in the range of [1,3][1,3]')
    print_board(state)
    for i in range(0, 9):
        state = get_next_play(state, i)
        if (is_the_game_done(state) == 1):
            print('Game is done')
            player = get_player(i)
            print('Player {pl} won !!!!'.format(pl=player))
            print_board(state)
            return
        print_board(state)


start_game()
