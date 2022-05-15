import calendar
import time
from datetime import datetime
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import ttk, filedialog

root = tk.Tk()
root.geometry("300x200")
root.title('Santos Productivity')
Label(root, text="Click the Button to browse the files", font='Georgia 13').pack(pady=25)

root.file_name = ''


def open_file():
    root.file_name = filedialog.askopenfilename(parent=root, initialdir="/")


b_chooseFile = ttk.Button(root, text="Chose File", width=20, command=open_file)
b_chooseFile.place(x=40, y=100)

print(root.file_name)

b_chooseFile = ttk.Button(root, text="Run", width=10, command=open_file)
b_chooseFile.place(x=90, y=140)
root.mainloop()
def timestamp_cov(date):
    try:
        datetime.strptime(date, "%m/%d/%Y %I:%M %p")
        data = "%m/%d/%Y %I:%M %p"
    except:
        data = "%m/%d/%y %H:%M"

    return calendar.timegm(time.strptime(date, data))


def ts_2_hrd(date):
    return datetime.utcfromtimestamp(date)


'''
def main():

    df = pd.read_csv(content)

    df = df[df['Tested On'].notna()]

    df['Timestamp'] = df.apply(lambda row: timestamp_cov(row['Tested On']), axis=1)

    df['Human read datetime'] = df.apply(lambda row: ts_2_hrd(row['Timestamp']), axis=1)

    filtered_df = df.loc[(df['Human read datetime'] >= '2022-05-10') & (df['Human read datetime'] < '2022-05-13')]

    sort = pd.DataFrame(filtered_df)
    print(sort.groupby(['Tested By']).count())


if __name__ == '__main__':
    main()

'''
