import tkinter as tk
from tkinter import W, ttk, END
from tkinter.ttk import Frame, Label

from currency_converter import CurrencyConverter

c = CurrencyConverter()


def get_rates() :
    local_currency = from_space.get()
    foreign_currency = to_space.get()
    first_date, last_date = c.bounds[foreign_currency]
    date_lbl.configure(text=last_date)
    amount = entry_space.get()
    result = c.convert(amount,local_currency,foreign_currency)
    result_space.delete(0,END)
    result_space.insert(0,result)


def clear():
    from_space.delete(0,END)
    to_space.delete(0,END)
    entry_space.delete(0,END)
    result_space.delete(0,END)


currency_exchange = tk.Tk()
currency_exchange.geometry("350x150")
currency_exchange.title('Rachata : Exchange Service')

# Structure
structure = Frame(currency_exchange, borderwidth=4, relief="ridge")
structure.grid(column=0, row=0)

# From
from_lbl = Label(structure, text='From')
from_lbl.grid(column=0, row=0)
from_space = ttk.Combobox(structure, values=list(c.currencies), width=5)
from_space.grid(column=0, row=1,)

# To
to_lbl = Label(structure, text='To')
to_lbl.grid(column=0, row=2)
to_space = ttk.Combobox(structure, values=list(c.currencies), width=5)
to_space.grid(column=0, row=3)

# Entry
entry_space = tk.Entry(structure)
entry_space.grid(column=1, row=1, padx=7)

# Result
result_space = tk.Entry(structure)
result_space.grid(column=1, row=3, padx=7)

# Date
date_lbl = Label(structure, text='Latest Update')
date_lbl.grid(column=1, row=4)

# Button
button = Frame(currency_exchange)
button.grid(column=0, row=4)
convert_button = tk.Button(button, text='convert', command=get_rates, width=10)
convert_button.grid(column=0, row=0, padx=15)

clear_button = tk.Button(button, text='clear', command=clear, width=10)
clear_button.grid(column=2, row=0, padx=20)

currency_exchange.mainloop()




