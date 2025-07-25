# src/gui/map_grid.py

import tkinter as tk

class MapGrid(tk.Frame):
    def __init__(self, master, rows=8, cols=14):
        super().__init__(master)
        self.master = master
        self.rows = rows
        self.cols = cols
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.is_horizontal = True
        self.create_grid()

    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.master, text='', command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, sticky='nsew')
                self.buttons[row][col] = button
        for i in range(self.rows):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.master.grid_columnconfigure(j, weight=1)

    def on_button_click(self, row, col):
        current_text = self.buttons[row][col]['text']
        new_text = 'X' if current_text == '' else ''
        self.buttons[row][col]['text'] = new_text
        # Additional functionality for recording data can be added here