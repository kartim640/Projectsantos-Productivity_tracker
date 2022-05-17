import calendar
import time
from datetime import datetime, date, timedelta
import pandas as pd
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, filedialog

root = tk.Tk()

root.geometry("400x300")  # size of the widget
root.title('Santos Productivity')  # widget title
Label(root, text="Click the Button to browse the files", font='Georgia 13').pack(pady=25)  # label in the widget


startdate = DateEntry(root, background='white', foreground='black', borderwidth=2)
startdate.place(x=40, y=140)



def main():
    date1 = (startdate.get_date())
    print(date1)


b_chooseFile = ttk.Button(root, text="Run", width=10, command=main)
b_chooseFile.place(x=130, y=220)




root.mainloop()