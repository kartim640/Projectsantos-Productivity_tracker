import calendar
import time
from datetime import datetime, timedelta
import pandas as pd
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, filedialog

root = tk.Tk()
root.geometry("400x300")
root.title('Santos Productivity')

Label(root, text="Click the Button to browse the files", font='Georgia 13').pack(pady=25)

startdate = DateEntry(root, width=12, year=2022, month=5, day=15, background='white', foreground='black', borderwidth=2)
startdate.place(x=40, y=140)

enddate = DateEntry(root, width=12, year=2022, month=5, day=15, background='white', foreground='black', borderwidth=2)
enddate.place(x=210, y=140)

root.file_name = ''


def open_file():
    root.file_name = filedialog.askopenfilename(parent=root, initialdir="/")


def timestamp_cov(date):
    try:
        datetime.strptime(date, "%m/%d/%Y %I:%M %p")
        data = "%m/%d/%Y %I:%M %p"
    except:
        data = "%m/%d/%y %H:%M"

    return calendar.timegm(time.strptime(date, data))


def ts_2_hrd(date):
    return datetime.utcfromtimestamp(date)


def main():
    df = pd.read_csv(root.file_name)

    df = df[df['Tested On'].notna()]

    df['Timestamp'] = df.apply(lambda row: timestamp_cov(row['Tested On']), axis=1)

    df['Human read datetime'] = df.apply(lambda row: ts_2_hrd(row['Timestamp']), axis=1)

    start_date = str(startdate.get_date())

    e_date = (enddate.get_date())
    td = timedelta(1)
    end_date = str(e_date + td)

    filtered_df = df.loc[(df['Human read datetime'] >= start_date) & (df['Human read datetime'] < end_date)]

    sort = pd.DataFrame(filtered_df)
    print(sort.groupby(['Tested By']).count())


b_chooseFile = ttk.Button(root, text="Chose File", width=20, command=open_file)
b_chooseFile.place(x=90, y=100)

b_chooseFile = ttk.Button(root, text="Run", width=10, command=main)
b_chooseFile.place(x=130, y=220)

root.mainloop()
