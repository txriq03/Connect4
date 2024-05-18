import sys
columns: list[str] = ["A", "B", "C", "D", "E", "F", "G"]

def generateBoard():
    board = [
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""]
    ]

    return board

def startGame(isMulti: bool):
    board = generateBoard()
    printBoard(board)
    handleGame(board, isMulti)

def printBoard(board):
    # loop through rows
    for x in range(6):
        print("\n+----+----+----+----+----+----+----+")
        print("|", end="")

        # loop through columns
        for y in range(7):
            # Check if the column is filled with a token
            if (board[x][y] == "🔵" or board[x][y] == "🔴"):
                print(" " + board[x][y], end=" |")
            else:
                print("  " + board[x][y], end="  |")

    print("\n+----+----+----+----+----+----+----+\n")

def isEmpty(col: int, board) -> bool:
    return board[0][col] == ""

# Find the next open slot in the 
def nextOpenSlot(board, col: int) -> int:

    """
    For loop starts at the end of an array,
    and iterates backwards until an empty slot is found
    """
    for row in range(5, -1, -1):
        if board[row][col] == "":
            return row

# Get column from the user
def getCol(playerTurn: int) -> int:
    validCols = ["1", "2", "3", "4", "5", "6", "7"]
    if playerTurn == 1:
        player = "One"
    else:
        player = "Two"

    while True:
        col = input(f"Player {player}: ")
        if (col in validCols):
            col = int(col) - 1
            return col
        else:
            print("Please input a valid column.", file=sys.stderr)
        
# Check which player's turn it is
def playerTurn(turn: int) -> int:
    if (turn % 2 != 0):
        return 1
    else:
        return 2
    
def dropToken(board, player: int, row: int, col: int):
        if (player == 1):
            board[row][col] = "🔴"
        else:
            board[row][col] = "🔵"

def checkForWin(board, token):
    falseConnect = False

    # Check horizontally
    """
    Only 4 horizontal connections can be made
    in the horizontal plane
    In all 6 rows
    """
    for col in range(4):
        for row in range(6):
            doesConnect = board[row][col] == token and board[row][col+1] == token and board[row][col+2] == token and board[row][col+3] == token
            return doesConnect
    
    # Check vertically
    """
    Vertical connections can be made in all 7 columns
    But only 3 possible connections in that column
    """
    for col in range(7):
        for row in range(3):
            doesConnect = board[row][col] and board[row+1][col] and board[row+2][col] and board[row+3][col]
            return doesConnect
    
    # Check positive diagnol
    for col in range(4):
        for row in range(3):
            doesConnect = board[row][col] and board[row-1][col+1] and board[row-2][col+2] and board[row-3][col+3]
            return doesConnect
    
    # Check negative diagnol
    for col in range(4):
        for row in range(3, 6):
            doesConnect = board[row][col] and board[row-1][col+1] and board[row-2][col+2] and board[row-3][col+3]
            return doesConnect

def handleGame(board, isMulti):
    turn = 1
    endGame = False

    print("Players need to enter a column between 1 and 7.")
    while endGame == False:

        # Check if game mode is multiplayer
        if isMulti:
            if (playerTurn(turn) == 1):
                col = getCol(1)
            else:
                col = getCol(2)
        
            # Check if space is empty
            if (isEmpty(col, board)):
                row = nextOpenSlot(board, col)

                # Drop the token and increment turn
                dropToken(board, playerTurn(turn), row, col)
                printBoard(board)
                turn += 1

            else:
                print("Column is already filled with tokens.")

        else:
            print("Computer game started.")
            break