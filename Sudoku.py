import random


def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    __solve_sudoku(board)
    __remove_values(board, difficulty)
    return board


def __solve_sudoku(board):
    empty_cell = __find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if __is_valid(board, row, col, num):
            board[row][col] = num
            if __solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


def __find_empty_cell(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return None


def __is_valid(board, row, col, num):
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def __remove_values(board, difficulty):
    # Calculate the number of cells to remove based on difficulty
    if difficulty == 'easy':
        cells_to_remove = 40
    elif difficulty == 'medium':
        cells_to_remove = 50
    elif difficulty == 'hard':
        cells_to_remove = 60
    else:
        cells_to_remove = 0

    # Remove cells
    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_to_remove -= 1
