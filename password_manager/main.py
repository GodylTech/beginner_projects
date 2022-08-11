from tkinter import *
from tkinter import messagebox
import random

# ------------- VARIABLES -------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ------------- INIT WINDOW -------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# ------------- GENERATE PASSWORD -------------
def generate_password():
    password_e.delete(0, END)
    password_list = []
    p_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    p_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    p_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = p_letters + p_numbers + p_symbols
    random.shuffle(password_list)
    password_ = ""
    for char in password_list:
        password_ += char
        
    password_e.insert(0, password_)

# ------------- SAVE DATA -------------
def save_data():
    webside = webside_e.get()
    email = user_e.get()
    password = password_e.get()
    
    if len(webside) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="The fields can't be empty")
    else:
        is_ok = messagebox.askokcancel(title=webside, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}")
    
        if is_ok:
            with open("data/data.txt", "a") as data_file:
                data_file.write(f"{webside}|{email}|{password}\n")
                
                webside_e.delete(0, END)
                user_e.delete(0, END)
                password_e.delete(0, END)
    
        


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="data/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


webside_lb = Label(text="Webside:")
webside_lb.grid(row=1, column=0)

webside_e = Entry(width=44)
webside_e.grid(row=1, column=1, columnspan=2)

user_lb = Label(text="EMail/Username:")
user_lb.grid(row=2, column=0)

user_e = Entry(width=44)
user_e.grid(row=2, column=1, columnspan=2)

password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

password_e = Entry(width=23)
password_e.grid(row=3, column=1)

generate_btn = Button(text="Generate password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=44, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
