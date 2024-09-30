import random

print("Tic Tac Toe")
print("-----------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    print(gameBoard)

def modifyArray(num, turn):
    if (num == 1):
        gameBoard[0][0] = turn
    elif (num == 2):
        gameBoard[0][1] = turn
    elif (num == 3):
        gameBoard[0][2] = turn
    elif (num == 4):
        gameBoard[1][0] = turn
    elif (num == 5):
        gameBoard[1][1] = turn
    elif (num == 6):
        gameBoard[1][2] = turn
    elif (num == 7):
        gameBoard[2][0] = turn
    elif (num == 8):
        gameBoard[2][1] = turn
    elif (num == 9):
        gameBoard[2][2] = turn
        
def checkForWinner(gameBoard):
    ### X axis
    if(gameBoard[0][0] == 'X' and gameBoard [0][1] == 'X' and gameBoard[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard [0][1] == 'O' and gameBoard[0][2] == 'O'):
        print("O has won!")
        return "O"
    if(gameBoard[1][0] == 'X' and gameBoard [1][1] == 'X' and gameBoard[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[1][0] == 'O' and gameBoard [1][1] == 'O' and gameBoard[1][2] == 'O'):
        print("O has won!")
        return "O"
    if(gameBoard[2][0] == 'X' and gameBoard [2][1] == 'X' and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard [2][1] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Y axis
    elif(gameBoard[0][0] == 'X' and gameBoard [1][0] == 'X' and gameBoard[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard [1][0] == 'O' and gameBoard[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][1] == 'X' and gameBoard [1][1] == 'X' and gameBoard[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][1] == 'O' and gameBoard [1][1] == 'O' and gameBoard[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == 'X' and gameBoard [1][2] == 'X' and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2] == 'O' and gameBoard [1][2] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Cross
    elif(gameBoard[0][0] == 'X' and gameBoard [1][1] == 'X' and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2] == 'X' and gameBoard [1][1] == 'X' and gameBoard[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard [1][1] == 'O' and gameBoard[2][2] == 'O'):
        print("X has won!")
        return "O"
    elif(gameBoard[0][2] == 'O' and gameBoard [1][1] == 'O' and gameBoard[2][0] == 'O'):
        print("O has won!")
        return "O"
    return "none"

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
    if(checkForWinner(gameBoard) != "none"):
        break
    ### Player's Turn
    if(turnCounter % 2 == 0):
        printGameBoard()
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if (numberPicked >= 1 or numberPicked <= 9):
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
        else:
            print("Invalid input. Please try again.")
        turnCounter += 1
    ### Computer's Turn
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers)
            print("\nCpu choice: ", cpuChoice)
            if(cpuChoice in possibleNumbers):
                modifyArray(cpuChoice, 'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break
