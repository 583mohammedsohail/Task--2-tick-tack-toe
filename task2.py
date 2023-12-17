import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board):
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            return 'X'
        elif all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            return 'O'
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'
    return None
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
def player_move(board, row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        return True
    else:
        print("Cell already occupied. Try again.")
        return False
def ai_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        row, col = minimax(board, 'O')['position']
        board[row][col] = 'O'
def minimax(board, player):
    available_moves = get_empty_cells(board)
    if check_winner(board) == 'X':
        return {'score': -1}
    elif check_winner(board) == 'O':
        return {'score': 1}
    elif not available_moves:
        return {'score': 0}
    moves = []
    for move in available_moves:
        new_board = [row[:] for row in board]
        new_board[move[0]][move[1]] = player
        if player == 'O':
            result = minimax(new_board, 'X')
        else:
            result = minimax(new_board, 'O')
        move_object = {
            'position': move,
            'score': result['score']
        }
        moves.append(move_object)
    if player == 'O':
        best_move = max(moves, key=lambda x: x['score'])
    else:
        best_move = min(moves, key=lambda x: x['score'])
    return best_move
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if player_move(board, row, col):
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        ai_move(board)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
if __name__ == "__main__":
    play_game()
