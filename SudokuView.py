import tkinter as tk
from SudokuController import SudokuController


def determine_color(row, column):
    if (row in (0, 1, 2, 6, 7, 8) and column in (3, 4, 5)) or (
            row in (3, 4, 5) and column in (0, 1, 2, 6, 7, 8)):
        color = "grey"
    else:
        color = "white"
    return color


class SudokuView:

    def __init__(self, initial_difficulty='easy'):
        self.difficulty = initial_difficulty
        self.sudokuController = SudokuController()
        self.rootView = tk.Tk()
        self.cells = {}
        self.generate_board()
        self.create_buttons()
        self.rootView.mainloop()

    def generate_board(self):
        game = self.sudokuController.generate_sudoku(self.difficulty)
        row = 0
        for rows in game:
            column = 0
            for _ in rows:
                self.generate_cell(game, row, column)
                column += 1
            row += 1

    def generate_cell(self, game, row, column):
        color = determine_color(row, column)
        self.cells[(row, column)] = tk.Label(self.rootView, width=4, height=2, font=("Helvetica", 20), bg=color,
                                             relief="raised")
        if game[row][column] != 0:
            self.cells[(row, column)].config(text=game[row][column], fg="black")
        else:
            self.cells[(row, column)].config(text="", fg="black")
        self.cells[(row, column)].grid(row=row, column=column)

    def create_buttons(self):
        reset_button = tk.Button(self.rootView, text="Reset", font=("Helvetica", 16), command=self.generate_board)
        reset_button.grid(row=10, column=5, columnspan=3, padx=5, pady=5)
