import numpy as np 

BOARD = np.full((3,3), 'null')
BOARD_INIT = np.reshape(np.arange(1,10), (3,3))
VALID_POS = range(1, 10)
NULL = np.array('null')

def is_move_not_valid(board=BOARD, valid_pos=VALID_POS, board_init=BOARD_INIT, mov=1):
    if mov not in valid_pos or board[np.where(board_init==mov)] == NULL:
        return False
    else: 
        return True

def set_mov(board=BOARD, board_init=BOARD_INIT, pos=1, side='X'):
    board[np.where(board_init==pos)] = side 
    return board 

def is_game_ended(board=BOARD, board_init=BOARD_INIT):
    lines = [[1,2,3], [4, 5, 6], [7,8,9],
                [1,4,7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]
    for line in lines: 
        if board[np.where(board_init== line [0])] ==  board[np.where(board_init==line[1])] == board[np.where(board_init==line[2])] != NULL:
            return board[np.where(board_init==line[1])].item(0)
    
    return NULL

def play_game(board=BOARD, board_init= BOARD_INIT): 
    game_ended = False 

    print('This is the board outlook')
    print(board_init)

    side = 'O'
    all_pos = range(1,10)

    while not game_ended : 
        cur_turn_input = int(input('{} turn. Choose position (1-9): '.format(side)))
        while is_move_not_valid(board= board, mov=cur_turn_input):
            print('Not a valid move. Input again!') 
            cur_turn_input = int(input('{} turn. Choose position (1-9): '.format(side)))
        
        board = set_mov(board=board, pos=cur_turn_input, side=side)

        print(board)
        game_ended = is_game_ended(board=board) != NULL
        side = 'X' if side == 'O' else 'O'

    print('{} is victorious!!'.format(is_game_ended(board=board)))

if __name__ == '__main__': 
    play_game() 
