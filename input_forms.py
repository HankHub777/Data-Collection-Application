# src/gui/input_forms.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Input_form(tk.Frame):
    def __init__(self, master):
        super(). __init__(master)
        # self.master = master
        # self.frame = tk.Frame(master)
        # self.frame.grid()

        # place frames in the main frame
        frame2 = ttk.Frame(self)
        frame2.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        frame3 = ttk.Frame(self)
        frame3.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        frame4 = ttk.Frame(self)
        frame4.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        frame5 = ttk.Frame(self)

        label2 = tk.Label(frame2, text="輸入工單SO: ", font=('微軟正黑體', 12))
        label2.grid(row=0, column=0)

        self.entry = ttk.Entry(frame2)
        self.entry.grid(row=0, column=1)

        label3 = tk.Label(frame3, text='選擇矢印:',pady=5, font=('微軟正黑體', 12))
        label3.grid(row=1, column=0)

        self.val = tk.StringVar()
        radio_btn1 = tk.Radiobutton(frame3, text='Blue上面',variable=self.val, value='blue', bg='blue', foreground='white' , font='微軟正黑體 12 bold', command=self.get_mark)
        radio_btn1.grid(row=1, column=1)
        radio_btn1.select() # Default selection

        radio_btn2 = tk.Radiobutton(frame3, text='Red下面', variable=self.val, value='red', bg='red', foreground='white', font='微軟正黑體 12 bold', command=self.get_mark)
        radio_btn2.grid(row=1, column=2)

        self.checkbox1_var = tk.IntVar()
        checkbox1 = ttk.Checkbutton(frame4, text="PD點異物", variable=self.checkbox1_var, command=self.get_checkbox)
        checkbox1.grid(row=0, column=0, sticky='w')

        self.checkbox2_var = tk.IntVar()
        checkbox2 = ttk.Checkbutton(frame4, text="PL線異物", variable=self.checkbox2_var,)
        checkbox2.grid(row=1, column=0, sticky='w')

        self.checkbox3_var = tk.IntVar()
        checkbox3 = ttk.Checkbutton(frame4, text="H壓傷", variable=self.checkbox3_var)
        checkbox3.grid(row=2, column=0, sticky='w')

        self.checkbox4_var = tk.IntVar()
        checkbox4 = ttk.Checkbutton(frame4, text="J摺痕", variable=self.checkbox4_var)
        checkbox4.grid(row=3, column=0, sticky='w')

        self.checkbox5_var = tk.IntVar()
        checkbox5 = ttk.Checkbutton(frame4, text="Z膠痕", variable=self.checkbox5_var)
        checkbox5.grid(row=0, column=1, sticky='w')

        self.checkbox6_var = tk.IntVar()
        checkbox6 = ttk.Checkbutton(frame4, text="N膠塊", variable=self.checkbox6_var)
        checkbox6.grid(row=1, column=1, sticky='w')

        self.checkbox7_var = tk.IntVar()
        checkbox7 = ttk.Checkbutton(frame4, text="MS膜傷", variable=self.checkbox7_var)
        checkbox7.grid(row=2, column=1, sticky='w')

        self.checkbox8_var = tk.IntVar()
        checkbox8 = ttk.Checkbutton(frame4, text="E壓點", variable=self.checkbox8_var)
        checkbox8.grid(row=3, column=1, sticky='w')

        self.checkbox9_var = tk.IntVar()
        checkbox9 = ttk.Checkbutton(frame4, text="A白點", variable=self.checkbox9_var)
        checkbox9.grid(row=0, column=2, sticky='w')

        self.checkbox10_var = tk.IntVar()
        checkbox10 = ttk.Checkbutton(frame4, text="K打痕", variable=self.checkbox10_var)
        checkbox10.grid(row=1, column=2, sticky='w')

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid()

    def submit(self):
        user_input = self.entry.get()
        checkbox_status = self.checkbox1_var.get()
        message = f"Input: {user_input}, Checkbox: {'Checked' if checkbox_status else 'Unchecked'}"
        messagebox.showinfo("User Selection", message)

    def clear(self):
        self.entry.delete(0, tk.END)
        self.checkbox_var.set(False)

    def get_mark(self):
        selected_mark = self.val.get()
        print(f"Selected mark: {selected_mark}")

    def get_checkbox(self):
        check = self.checkbox1_var.get()
        print(f"Checkbox PD點異物 is {'checked' if check else 'unchecked'}")

        
        

