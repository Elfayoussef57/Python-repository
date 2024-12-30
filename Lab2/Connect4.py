def create_board():
    """Creates a 6x7 game board."""
    return [[" " for _ in range(7)] for _ in range(6)]

def print_board(board):
    """Prints the game board."""
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * 15)  # Separator for the bottom

def main():
    board = create_board()
    print_board(board)
    player = ["X", "O"]
    turn = 0
    count = 0
    while count <= 42:
        col = int(input(f"Player {player[turn]}: Enter column (0-7): "))
        line = int(input(f"Player {player[turn]}: Enter line (0-6): "))
        for line in range(0,5, -1):
            for col in range(0,6, -1):
                if board[line][col] == " ":
                    board[line][col] = player[turn]           
                    break
        print_board(board)
        turn = (turn + 1) % 2
        count += 1

if __name__ == "__main__":
    main()