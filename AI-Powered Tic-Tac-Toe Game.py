import math
import time

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i:i + 3] for i in range(0, len(board), 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for a draw
def is_draw(board):
    return ' ' not in board

# Evaluate the board
def evaluate(board):
    if check_winner(board, 'O'):  # AI wins
        return 10
    elif check_winner(board, 'X'):  # Player wins
        return -10
    return 0  # Draw

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = ' '  # Undo move
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = ' '  # Undo move
        return best_score

# Find the best move for AI
def find_best_move(board):
    best_move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_score = minimax(board, 0, False)
            board[i] = ' '  # Undo move
            if move_score > best_score:
                best_score = move_score
                best_move = i
    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe: Player (X) vs AI (O)")
    print_board(board)

    while True:
        # Player's turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'

        # Check for player's win or draw
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn
        print("AI is thinking...")
        time.sleep(2)  # Pause for 2 seconds to simulate AI "thinking"
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print(f"AI chooses position {ai_move}")
        print_board(board)

        # Check for AI's win or draw
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
