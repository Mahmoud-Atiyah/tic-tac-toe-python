import random

print("Tic Tac Toe")
print("-----------")

# Game display
def printGameBoard():
    for row in gameBoard:
        print(" | ".join(str(cell) for cell in row))
        print("-" * 9)

# Update game board
def modifyArray(num, turn):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    i, j = mapping[num]
    gameBoard[i][j] = turn

# Check winner
def checkForWinner(board, silent=False):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if not silent:
                print(f"{board[i][0]} has won!")
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if not silent:
                print(f"{board[0][i]} has won!")
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        if not silent:
            print(f"{board[0][0]} has won!")
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if not silent:
            print(f"{board[0][2]} has won!")
        return board[0][2]
    return "none"

# Minimax AI
def get_best_move(board, available):
    best_score = -float('inf')
    best_move = None
    for move in available:
        temp_board = [row.copy() for row in board]
        i, j = divmod(move - 1, 3)
        temp_board[i][j] = 'O'
        score = minimax(temp_board, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(board, is_maximizing):
    winner = checkForWinner(board, silent=True)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif all(isinstance(cell, str) for row in board for cell in row):
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = (i * 3) + j + 1
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = (i * 3) + j + 1
                    best_score = min(score, best_score)
        return best_score

# Play one game round
def play_game():
    global gameBoard, possibleNumbers
    gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turnCounter = 0

    while True:
        if checkForWinner(gameBoard) != "none":
            break
        if len(possibleNumbers) == 0:
            printGameBoard()
            print("It's a draw!")
            break

        # Player's Turn
        if turnCounter % 2 == 0:
            printGameBoard()
            try:
                numberPicked = int(input("\nChoose a number [1-9]: "))
                if 1 <= numberPicked <= 9 and numberPicked in possibleNumbers:
                    modifyArray(numberPicked, 'X')
                    possibleNumbers.remove(numberPicked)
                    turnCounter += 1
                else:
                    print("Invalid or taken input. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        # Computer's Turn
        else:
            cpuChoice = get_best_move(gameBoard, possibleNumbers)
            print("\nCpu choice:", cpuChoice)
            modifyArray(cpuChoice, 'O')
            possibleNumbers.remove(cpuChoice)
            turnCounter += 1

# Game loop with replay
while True:
    play_game()
    replay = input("Play again? (y/n): ").strip().lower()
    if replay != 'y':
        print("Thanks for playing!")
        break
