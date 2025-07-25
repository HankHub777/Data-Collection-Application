import tkinter as tk
from tkinter import ttk
from datetime import datetime

class TimeDisplay(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # self.master = master
        frame1 = ttk.Frame(self)
        frame1.pack(side=tk.TOP, fill=tk.X)

        self.label = ttk.Label(frame1, text='', font=('微軟正黑體',12))
        self.label.pack(side=tk.TOP, anchor=tk.NW)
        # self.label.pack(side=tk.TOP, anchor=tk.NW)
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('現在時間： %Y:%m:%d %H:%M:%S', )
        self.label.config(text=current_time)
        self.master.after(1000, self.update_time)  # Update every second