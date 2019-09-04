import random

wordList = ["umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "lemon", "cabel", "mirror"]

#print out the '-' format of the string.  eg. the word is 'lemon' -> -----
def print_layout(string):
    blank = ''
    for char in string:
        if char.isspace():
            blank += ' '
        else:
            blank += '-'
    return blank

#replace multiple characters at 'list_index' by 'new' of a string, return a new replaced string
def replace_string_index(list_index, new, string):
    list_char = list(string)
    for i in list_index:
        list_char[i] = new

    return ''.join(list_char)

#return the list of all indexs of the duplicate 'letter' in 'word'
def indexes(letter, word):
    listt = []
    for i,x in enumerate(word):
        if x == letter:
            listt.append(i)
    return listt

#random a word in 'wordList'
word = random.choice(wordList)

num_guess = 5

#current layout = word censored by '-'
current_layout = print_layout(word)
print('Here is the word you will guess')
print(current_layout)

win = False

while (num_guess > 0):

    guess = input('Enter your guess: ')

    #get index of 'guess' in 'word', then replace '-' in 'current_layout' based on the 'indexes()' function
    if guess in word:
        print('Correct guess! You have %d left' % num_guess)
        
        index = indexes(guess, word)
        current_layout = replace_string_index(index, guess, current_layout)

    else:
        num_guess -= 1
        print('Wrong guess! You have %d guess left' % num_guess)

    print(current_layout)

    if '-' not in current_layout:
        win = True
        break

if win:
    print('You won the game!')
else:
    print('You lost the game!')    
