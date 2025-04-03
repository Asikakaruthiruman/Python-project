import random

def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Function to check if a player has won"""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Check if the board is full (tie condition)"""
    return all(all(cell != " " for cell in row) for row in board)

def bot_move(board):
    """Simple bot move - chooses a random empty cell"""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game"""
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        turn = 0

        print("Welcome to Tic-Tac-Toe!")
        mode = input("Choose mode: 1. Play with Friend  2. Play with Bot  (Enter 1 or 2): ")

        if mode not in ["1", "2"]:
            print("Invalid choice! Exiting...")
            return

        print_board(board)

        while True:
            player = players[turn % 2]
            print(f"Player {player}'s turn.")

            if mode == "2" and player == "O":  # Bot's turn
                row, col = bot_move(board)
                print(f"Bot chooses: {row}, {col}")
            else:  # Human's turn
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))

                    if board[row][col] != " ":
                        print("Cell already taken! Try again.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid input! Enter numbers between 0-2.")
                    continue

            board[row][col] = player
            print_board(board)

            if check_winner(board, player):
                print(f"🎉 Player {player} wins! 🎉")
                break
            elif is_full(board):
                print("It's a tie! 🤝")
                break

            turn += 1

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! 🎮")
            break

# Run the game
tic_tac_toe()
