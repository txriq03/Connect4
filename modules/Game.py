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

def checkForWin(board, token: str) -> bool:
    rows = 6
    cols = 7
    
     # Check horizontally
    for r in range(rows):
        for c in range(cols - 3):
            if board[r][c] == token and board[r][c+1] == token and board[r][c+2] == token and board[r][c+3] == token:
                return True
    
    # Check vertically
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == token and board[r+1][c] == token and board[r+2][c] == token and board[r+3][c] == token:
                return True
            
    # Check positive diagonal (bottom-left to top-right)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if board[r][c] == token and board[r+1][c+1] == token and board[r+2][c+2] == token and board[r+3][c+3] == token:
                return True
            
    # Check negative diagonal (top-left to bottom-right)
    for r in range(3, rows):
        for c in range(cols - 3):
            if board[r][c] == token and board[r-1][c+1] == token and board[r-2][c+2] == token and board[r-3][c+3] == token:
                return True
            
    return False

def handleGame(board, isMulti):
    turn = 1
    endGame = False

    print("Players need to enter a column between 1 and 7.")
    while not endGame:

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
                
                # doesConnect = checkForWin(board, "🔴")
                
                if checkForWin(board, "🔴"):
                    print("Player One wins!")
                    endGame = True
                elif checkForWin(board, "🔵"):
                    print("Player Two wins!")
                else:
                    printBoard(board)   
                    turn += 1
                
            else:
                print("Column is already filled with tokens.")

        else:
            print("Computer game started.")
            break