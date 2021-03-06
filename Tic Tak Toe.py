board = [' ' for x in range(10)]

import random

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, letter2):
    return bo[9] == letter2 and bo[8] == letter2 and bo[7] == letter2 or(
        bo[6] == letter2 and bo[5] == letter2 and bo[4] == letter2) or(
        bo[3] == letter2 and bo[2] == letter2 and bo[1] == letter2) or (
        bo[1] == letter2 and bo[4] == letter2 and bo[7] == letter2) or (
        bo[2] == letter2 and bo[5] == letter2 and bo[8] == letter2) or (
        bo[3] == letter2 and bo[6] == letter2 and bo[9] == letter2) or (
        bo[1] == letter2 and bo[5] == letter2 and bo[9] == letter2) or (
        bo[3] == letter2 and bo[5] == letter2 and bo[7] == letter2)

def isBoardFull(board):
   if board.count(' ') > 1:
        return False
   else:
        return True

def player1Move():
    run = True
    while run:
        playerInput = input("Player 1 Enter your move here: ")
        try:
            playerInput = int(playerInput)
            if playerInput > 0 and playerInput < 10:
                pos = playerInput
                if spaceIsFree(playerInput):
                    run = False
                    insertLetter('X', playerInput)
                else:
                    print("This space is occupied!")
            else:
                print("Type a number between 1-9")
        except:
            print("Please type a number!")

def player2Move():
    run = True
    while run:
        player2Input = input("Player 2 Enter your move here: ")
        try:
            player2Input = int(player2Input)
            if player2Input > 0 and player2Input < 10:
                pos = player2Input
                if spaceIsFree(player2Input):
                    run = False
                    insertLetter('O', player2Input)
                else:
                    print("This space is occupied!")
            else:
                print("Type a number between 1-9")
        except ValueError:
            print("Please type a number!")

def Random_Computer_Move():
    run = True
    already_moved = False
    while run:
        for pos in range(10):
            if spaceIsFree(pos):
                insertLetter('O', pos)
                if isWinner(board,"O"):
                    run = False
                    already_moved = True
                    break
                else:
                    insertLetter(' ', pos)
        if already_moved == False:
            for pos in range(10):
                if spaceIsFree(pos):
                    insertLetter('X', pos)
                    if isWinner(board,"X"):
                        insertLetter('O', pos)
                        run = False
                        already_moved = True
                        break
                    else:
                        insertLetter(' ', pos)
        if already_moved == False:
            pos = random.randrange(1,10)
            if spaceIsFree(pos):
                insertLetter('O', pos)
                run = False



def main():
    print("Welcome to Tic Tak Toe! Win by getting 3 letters in a row!")
    print("Would you like to play single player or two player?")
    players = input("Type 1 for single player and 2 for 2 players!:")
    printBoard(board)
    while players == "1" and not(isBoardFull(board)):

        if not(isWinner(board, "O")):
            player1Move()
            printBoard(board)
        else:
            print('Os Won')
            break
        if isBoardFull(board) and not(isWinner(board, "O")):
            print("Tie game")
            break
        print("__________________________________________")
        if not(isWinner(board, "X")):
            Random_Computer_Move()
            printBoard(board)
        else:
            print('Xs Won')
            break

    while players == "2" and not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            player1Move()
            printBoard(board)
        else:
            print('Os Won')
            break
        if isBoardFull(board) and not(isWinner(board, "O")):
            print("Tie game")
            break
        print("__________________________________________")
        if not(isWinner(board, "X")):
            player2Move()
            printBoard(board)
        else:
            print('Xs Won')
            break

Running = True
while Running:
    main()
    playAgain =input("Type 1 to play again!: ")
    if playAgain == "1":
        board = [' ' for x in range(10)]
        pass
    else:
        Running = False