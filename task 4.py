def print_board(board):
    """Function to display the Sudoku board."""
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)  # Add horizontal separators every 3 rows
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")  # Add vertical separators every 3 columns
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()

def find_empty(board):
    """Find an empty space on the board (denoted by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Check if a number can be placed at the given position."""
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    """Solve the Sudoku board using backtracking."""
    empty_pos = find_empty(board)
    if not empty_pos:
        return True  # Puzzle solved
    row, col = empty_pos

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Undo move if solution not found

    return False

# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Display the unsolved board
print("Unsolved Sudoku Puzzle:")
print_board(board)

# Solve the puzzle and display the result
if solve(board):
    print("\nSolved Sudoku Puzzle:")
    print_board(board)
else:
    print("No solution exists for this puzzle.")
