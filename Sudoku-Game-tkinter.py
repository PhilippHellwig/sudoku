

from tkinter import *
import random

class SudokuBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Löser")
        self.create_board()
        self.create_buttons()
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def create_board(self):
        self.cells = {}
        for i in range(9):
            for j in range(9):
                if (i in (0, 1, 2, 6, 7, 8) and j in (3, 4, 5)) or (i in (3, 4, 5) and j in (0, 1, 2, 6, 7, 8)):
                    color = "grey"
                else:
                    color = "white"
                self.cells[(i, j)] = Label(self.master, width=4, height=2, font=("Helvetica", 20), bg=color, relief="raised")
                self.cells[(i, j)].grid(row=i, column=j)

    def create_buttons(self):
        self.generate_button = Button(self.master, text="Generate", font=("Helvetica", 16), command=self.generate_board)
        self.generate_button.grid(row=10, column=1, columnspan=3, padx=5, pady=5)

        self.solve_button = Button(self.master, text="Solve", font=("Helvetica", 16), command=self.solve_board)
        self.solve_button.grid(row=10, column=3, columnspan=3, padx=5, pady=5)

        self.reset_button = Button(self.master, text="Reset", font=("Helvetica", 16), command=self.reset_board)
        self.reset_button.grid(row=10, column=5, columnspan=3, padx=5, pady=5)

    def generate_board(self):
        # Generate a solvable Sudoku board
        while not self.solve_board():
            pass
        self.remove_numbers()  # Remove some numbers to create a puzzle
        self.update_cells()

    def reset_board(self):
        # Reset the board to all zeros
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.update_cells()

    cells_to_remove = 50  # class-level variable

    def remove_numbers(self):
        # Remove numbers from the board to create a puzzle
        cells_removed = 0
        while cells_removed < self.cells_to_remove:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_removed += 1


    def solve_board(self):
        # Solve the Sudoku board using backtracking
        def find_empty():
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        return (i, j)
            return None

        def is_valid(num, pos):
            # Check if num is valid in the given position
            # Check row
            for i in range(9):
                if self.board[pos[0]][i] == num and pos[1] != i:
                    return False
            # Check column
            for i in range(9):
                if self.board[i][pos[1]] == num and pos[0] != i:
                    return False
            # Check 3x3 square
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if self.board[i][j] == num and (i, j) != pos:
                        return False
            return True

        def solve():
            empty = find_empty()
            if not empty:
                return True
            else:
                row, col = empty
                for num in range(1, 10):
                    if is_valid(num, (row, col)):
                        self.board[row][col] = num
                        if solve():
                            return True
                        self.board[row][col] = 0
                return False

        value = solve()
        self.update_cells()
        return value

    def update_cells(self):
        # Update the cells with the current board values
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cells[(i, j)].config(text=self.board[i][j], fg="black")
                else:
                    self.cells[(i, j)].config(text="", fg="black")

root = Tk()
sudoku_board = SudokuBoard(root)
root.mainloop()