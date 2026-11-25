
"""
FOUR IN A ROW - PYTHON MINI PROJECT
A two-player Connect Four game.
"""

import sys

# Game constants
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')


# Create a new empty board
def getNewBoard():
    board = {}

    for column in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT):
            board[(column, row)] = EMPTY_SPACE

    return board


# Display the game board
def displayBoard(board):
    print("\n       1234567")
    print("      +-------+")

    for row in range(BOARD_HEIGHT):
        print("      |", end="")

        for column in range(BOARD_WIDTH):
            print(board[(column, row)], end="")

        print("|")

    print("      +-------+\n")


# Ask the player to enter a column
def askForPlayerMove(playerTile, board):

    while True:
        print("Player " + playerTile +
              ", enter a column (1-7) or QUIT:")

        response = input("> ").upper().strip()

        if response == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print("Invalid input! Enter a number from 1 to 7.")
            continue

        columnIndex = int(response) - 1

        # Check whether the column is full
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("That column is full! Choose another column.")
            continue

        # Find the lowest empty position
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):

            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


# Check whether the board is completely full
def isFull(board):

    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):

            if board[(column, row)] == EMPTY_SPACE:
                return False

    return True


# Check whether a player has four tiles in a row
def isWinner(playerTile, board):

    # Horizontal and vertical directions
    directions = [
        (1, 0),
        (0, 1),
        (1, 1),
        (1, -1)
    ]

    for column in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT):

            if board[(column, row)] != playerTile:
                continue

            for dx, dy in directions:

                count = 1

                for step in range(1, 4):

                    nextColumn = column + dx * step
                    nextRow = row + dy * step

                    if (0 <= nextColumn < BOARD_WIDTH and
                        0 <= nextRow < BOARD_HEIGHT and
                        board[(nextColumn, nextRow)] == playerTile):

                        count += 1
                    else:
                        break

                if count == 4:
                    return True

    return False


# Main game function
def main():

    print("=" * 35)
    print("       FOUR IN A ROW")
    print("       CONNECT FOUR GAME")
    print("=" * 35)

    print("\nTwo players take turns dropping tiles.")
    print("Connect four tiles horizontally,")
    print("vertically or diagonally to win.")
    print("\nPlayer X goes first.")
    print("Player O goes second.")

    while True:

        # Create a new game
        gameBoard = getNewBoard()
        playerTurn = PLAYER_X

        # Main game loop
        while True:

            displayBoard(gameBoard)

            # Get player's move
            playerMove = askForPlayerMove(
                playerTurn, gameBoard
            )

            # Place the player's tile
            gameBoard[playerMove] = playerTurn

            # Check for winner
            if isWinner(playerTurn, gameBoard):

                displayBoard(gameBoard)

                print("=" * 35)
                print(" CONGRATULATIONS!")
                print(" PLAYER " + playerTurn + " HAS WON!")
                print("=" * 35)

                break

            # Check for draw
            if isFull(gameBoard):

                displayBoard(gameBoard)

                print("=" * 35)
                print(" GAME OVER! IT IS A DRAW!")
                print("=" * 35)

                break

            # Switch players
            if playerTurn == PLAYER_X:
                playerTurn = PLAYER_O
            else:
                playerTurn = PLAYER_X

        # Ask whether players want another game
        playAgain = input(
            "\nDo you want to play again? (Y/N): "
        ).upper().strip()

        if playAgain != 'Y':
            print("\nThank you for playing Four in a Row!")
            print("Have a great day!")
            break


# Start the game
if __name__ == "__main__":
    main()
