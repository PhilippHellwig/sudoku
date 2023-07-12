import tkinter as tk
from SudokuController import SudokuController


class SudokuView:

    def __init__(self):
        self.sudokuController = SudokuController()
        print('init')

    def generate_board(self):
        self.sudokuController.generate_game()
        print('sudoku')

