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


def open_file():
    root.file_name = filedialog.askopenfilename(parent=root, initialdir="/")


b_chooseFile = ttk.Button(root, text="Chose File", width=20, command=open_file)
b_chooseFile.place(x=90, y=100)



def timestamp_cov(date):
    try:
        datetime.strptime(date, "%m/%d/%Y %I:%M %p")
        data = "%m/%d/%Y %I:%M %p"
    except:
        data = "%m/%d/%y %H:%M"

    return calendar.timegm(time.strptime(date, data))


def ts_2_hrd(date):
    return datetime.utcfromtimestamp(date)


root.file_name = ''


def main():

    df = pd.read_csv(root.file_name)

    df = df[df['Tested On'].notna()]

    df['Timestamp'] = df.apply(lambda row: timestamp_cov(row['Tested On']), axis=1)

    df['Human read datetime'] = df.apply(lambda row: ts_2_hrd(row['Timestamp']), axis=1)

    filtered_df = df.loc[(df['Human read datetime'] >= '2022-05-16' ) & (df['Human read datetime'] < '2022-05-17')]

    sort = pd.DataFrame(filtered_df)
    print(sort.groupby(['Tested By']).count())


b_chooseFile = ttk.Button(root, text="Run", width=10, command=main)
b_chooseFile.place(x=130, y=220)

root.mainloop()

