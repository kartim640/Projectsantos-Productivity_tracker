# on Button click reading and displaying date selection
import tkinter as tk
from tkcalendar import DateEntry

my_w = tk.Tk()
my_w.geometry("380x220")


cal = DateEntry(my_w, selectmode='day')
cal.grid(row=1, column=1, padx=20, pady=30)

test1 = cal.get_date()
print(test1)
b1 = tk.Button(my_w, text='Read')
b1.grid(row=1, column=2)
print(test1)

my_w.mainloop()


'''eventtype_var = tk.StringVar()
eventtype_entry = ttk.Combobox(root, width=27, textvariable=eventtype_var)
eventtype_entry['values'] = ('Live', '14 days before', '45 days before')
eventtype_entry.current(0)
eventtype_entry.grid(column=1, row=7)
eventtype_entry.current()'''