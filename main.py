# src/main.py

import tkinter as tk
from tkinter import ttk
from tkinter import font
from gui.map_grid import MapGrid
from gui.time_display import TimeDisplay
from gui.input_forms import Input_form
from gui.text_display import TextDisplay

class DataCollectionApp(tk.Tk):  # Inherit from Tk class
    def __init__(self):
        super().__init__() # inherit from Tk class
        self.title("Data Collection Application")
        
        # Set window size
        # print(tk.font.families(root=None, displayof=None))  # Print available font families for debugging
        width = 770
        height = 440
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        left_top_x = int((window_width - width) / 2)
        left_top_y = int((window_height - height) / 2)
        self.geometry(f'{width}x{height}+{left_top_x}+{left_top_y}') 

        # Create main container frames
        self.left_frame = ttk.Frame(self.root)
        self.right_frame = ttk.Frame(self.root)

        # Position main frames
        self.left_frame.grid(row=0, column=0, pady=5, sticky='nsew')
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Initialize components
        self.map_grid = MapGrid(self.right_frame, rows=8, cols=14)
        self.time_display = TimeDisplay(self.left_frame)
        self.input_forms = Input_form(self.left_frame)
        self.text_display = TextDisplay(self.left_frame)
        # self.select_mark = SelectMark(self.left_frame)

        # Layout left components
        self.time_display.grid(row=0, column=0, pady=5)
        self.input_forms.grid(row=1, column=0, pady=5)
        self.text_display.grid()

        # Layout right components
        self.map_grid.grid()

        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # self.map_grid.pack()
        # self.time_display.pack()
        # self.input_forms.pack()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = DataCollectionApp()
    app.run()