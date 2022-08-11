from tkinter import Tk, Label, Entry, Button

from numpy import pad

window = Tk()
window.title("Mile to Km coverter")
# window.minsize(width=400, height=150) 
window.config(padx=50, pady=20)

def mile_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609, 3)
    equal_lbl.config(text=str(km))

mile_input = Entry(width=5)
mile_input.grid(row=0, column=1)

mile_lbl = Label(text="Miles")
mile_lbl.grid(row=0, column=2)

equal_is_lbl = Label(text="is equal to", width=10)
equal_is_lbl.grid(row=1, column=0)

equal_lbl = Label(text="")
equal_lbl.grid(row=1, column=1)

km_lbl = Label(text="km")
km_lbl.grid(row=1, column=2)

calc_btn = Button(text="Calculate", command=mile_to_km)
calc_btn.grid(row=2, column=1)



window.mainloop()
