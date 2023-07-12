import tkinter as tk
from SudokuController import SudokuController


class SudokuView:

    def __init__(self):
        self.sudokuController = SudokuController()
        self.master = tk.Tk()
        self.cells = {}

    def generate_board(self):
        self.sudokuController.generate_game()
        print('sudoku')
        game = self.sudokuController.generate_game()
        row_counter = 0
        for row in game:
            column_counter = 0
            for column in row:
                if (row_counter in (0, 1, 2, 6, 7, 8) and column_counter in (3, 4, 5)) or (row_counter in (3, 4, 5) and column_counter in (0, 1, 2, 6, 7, 8)):
                    color = "grey"
                else:
                    color = "white"
                self.cells[(row_counter, column_counter)] = tk.Label(self.master, width=4, height=2, font=("Helvetica", 20), bg=color,
                                           relief="raised")
                self.cells[(row_counter, column_counter)].grid(row=row_counter, column=column) #TODO use actual array values
                column_counter += 1
            row_counter += 1
        self.master.mainloop()
