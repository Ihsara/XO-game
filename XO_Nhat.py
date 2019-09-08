#XO

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
    
def printBoardPosition():
    print('1' + '|' + '2' + '|' + '3')
    print('-----')
    print('4' + '|' + '5' + '|' + '6')
    print('-----')
    print('7' + '|' + '8' + '|' + '9')

print('This is the board outlook')
printBoardPosition()

turn = 'O'
all_pos = ['1','2','3','4','5','6','7','8','9']
for i in range(9):
    
    print('This is ' + turn + ' . Which position (1-9)?')
    
    pos = input()
    while pos not in all_pos:
        print('You entered wrong input or that position was already selected. Enter again')
        pos = input()

    all_pos.remove(pos)
    theBoard[pos] = turn


    if turn == 'O':
        turn = 'X'
        win = True
    else:
        turn = 'O'
        win = False

    if theBoard['1'] == theBoard['2'] and theBoard['1'] == theBoard['3'] and theBoard['1'] != ' ':
        break
    elif theBoard['1'] == theBoard['5'] and theBoard['1'] == theBoard['9'] and theBoard['1'] != ' ':
        break
    elif theBoard['1'] == theBoard['4'] and theBoard['1'] == theBoard['7'] and theBoard['1'] != ' ':
        break
    elif theBoard['4'] == theBoard['5'] and theBoard['4'] == theBoard['6'] and theBoard['4'] != ' ':
        break
    elif theBoard['7'] == theBoard['8'] and theBoard['7'] == theBoard['9'] and theBoard['7'] != ' ':
        break
    elif theBoard['2'] == theBoard['5'] and theBoard['2'] == theBoard['8'] and theBoard['2'] != ' ':
        break
    elif theBoard['3'] == theBoard['6'] and theBoard['3'] == theBoard['9'] and theBoard['3'] != ' ':
        break
    elif theBoard['3'] == theBoard['5'] and theBoard['3'] == theBoard['7'] and theBoard['3'] != ' ':
        break

    printBoard(theBoard)

printBoard(theBoard)   
if win == True:
    turn = 'O'
else:
    turn = 'X'
print('Winner: ', turn)
