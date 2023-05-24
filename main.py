import tkinter as tk
from tkinter import ttk
# window
window = tk.Tk()
window.title("demo")
window.geometry('600x300')
# title
title_label = ttk.Label(
    master=window, text='miles to kilometers', font='Calibri 24 bold')
title_label.pack()
# input_field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Convert')
entry.pack(side='left')
button.pack(side='left')
input_frame.pack()
# run
window.mainloop()
