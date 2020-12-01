import random
from IPython.display import clear_output

# tic-tac-toe game 

board = [' ' for x in range(10)] #list for board from 0 to 9 -> 0 is only used to check if there aren't any moves left

def insertLetter(letter, pos): #function for inserting letter into board slot
    board[pos] = letter

def spaceIsFree(pos): #function for checking if a board space is free
    return board[pos] == ' '

def printBoard(board):
    # "board" is a list of strings representing the board 
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def isWinner(b, l): #b = board, l=letter
     # function returns winning combinations
    return (b[7] == l and b[8] == l and b[9] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[1] == l and b[2] == l and b[3] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)

def playerMove():
    # function for inserting player move onto board
    run = True # makes it always start to run
    while run:
        move = input('Please select a position to place an X (1-9 in computer keypad layout): ') 
        try:
            move = int(move) # integerises input, if it raises an error then it goes to the except 
            if move > 0 and move < 10: #doesn't let you input a number that's too high or too low
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Please pick a non-occupied space') # if space isn't free, print that you can't go there
            else:
                print('Please pick a number within 1-9') # if the player tries to pick a number outside of 1 and 9 then they get told they can't
        except:
            print('Please pick an integer number!') # if they type something that isn't an integer then they get told
            

def compMove():
    #function for computer moves, returns a move
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # a list of any empty square still on the board
    #the above works by running a for loop, x=index value and letter=value, 
    #enumerate gives us the index values and actual values for everything in the list
    #checks if there are any blank letters, and excludes 0 because that's always blank
    move = 0 #this is the default move, if we can't do any other move it'll return 0 and say it's a draw

    computerMove = [] #starts off as empty list 

    for i in possibleMoves:
        if i in [1,2,3,4,5,6,7,8,9]:
            computerMove.append(i)
            
    if len(computerMove) > 0:
        #len returns the number of items in an object
        move = selectRandom(computerMove)
        
    return move

def selectRandom(li): 
    ln = len(li)
    r = random.randrange(0,ln) #creates random number within length of list
    return li[r]
    

def isBoardFull(board):
    #helper function to check if the board is full
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    
    printBoard(board)

    while not(isBoardFull(board)): #while the board isn't full
        if not(isWinner(board, 'O')): #while the computer hasn't won
            playerMove() #player is able to move
            printBoard(board) #prints the new board with the player's move
        else:
            print('Computer won :(') #if the computer has won, say it
            break

        if not(isWinner(board, 'X')): #while the player hasn't won
            move = compMove() #computer is able to move, take move from the compMove function
            if move == 0: #if there aren't any available moves left and nobody has won, then it's a tie
                print('The game is a draw')
            else:
                insertLetter('O', move) #put an O wherever the move function returns
                print('Computer placed an O in position', move , ':') #tell us where the computer moved
                printBoard(board) # prints the new board with the computer's move
        else:
            print('You won!') # the player has won
            break

    if isBoardFull(board): #if board is full without any winner then it's a draw
        print('The game is a draw')

while True:
    answer = input('Do you want to play? (Y/N) ') #asks if player wants to play
    if answer.lower() == 'y': #if they say yes then make the board and start the main function
        board = [' ' for x in range(10)]
        main()
    else: #if they don't want to play, clear the console and stop the game :(
        clear_output()
        break
