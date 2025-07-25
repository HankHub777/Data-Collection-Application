import tkinter as tk
from tkinter import ttk

class TextDisplay(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        frame_text = ttk.Frame(self)
        frame_text.pack(side=tk.TOP, fill=tk.BOTH)

        self.text_list = tk.Listbox(frame_text, height=5, bg="darkgrey", fg="white", font=('微軟正黑體', 12))
        self.text_list.pack(side=tk.TOP, anchor=tk.NW)

        self.update_text()

    def update_text(self):
        # Example text to display
        example_text = "這是缺陷紀錄輸入的內容"


