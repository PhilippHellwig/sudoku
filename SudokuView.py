import tkinter as tk
from SudokuController import SudokuController


class SudokuView:

    def __init__(self):
        self.sudokuController = SudokuController()
        self.master = tk.Tk()
        print('init')

    def generate_board(self):
        self.sudokuController.generate_game()
        print('sudoku')
        self.cells = {}
        game = self.sudokuController.generate_game()
        for row in game:
            for column in row:
                if (row in (0, 1, 2, 6, 7, 8) and column in (3, 4, 5)) or (row in (3, 4, 5) and column in (0, 1, 2, 6, 7, 8)):
                    color = "grey"
                else:
                    color = "white"
                self.cells[(row, column)] = tk.Label(self.master, width=4, height=2, font=("Helvetica", 20), bg=color,
                                           relief="raised")
                self.cells[(row, column)].grid(row=row, column=column)


        self.master.mainloop()