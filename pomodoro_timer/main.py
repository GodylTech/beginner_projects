from tkinter import *
import math

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
timer_on = False

def reset_timer():
    global timer_on, reps
    if timer_on:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Timer")
        check_mark.config(text="")
        timer_on = False
        reps = 0
    
def start_button():
    global timer_on
    if not timer_on:
        timer_on = True
        start_timer()

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60  
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        print("Long break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        print("Short break")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        print('Work')
        
    if reps == 24:
        global timer_on
        title_label.config(text="Go home!")
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        timer_on = False
        check_mark.config(text="")
    
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)
        
    
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, width=600, height=600)

tomato_img = PhotoImage(file="tomato.png")

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=tomato_img.width(), height=tomato_img.height(), bg=YELLOW, highlightthickness=0)
canvas.create_image(tomato_img.width()/2, tomato_img.height()/2, image=tomato_img)
timer_text = canvas.create_text(tomato_img.width()/2, tomato_img.height()/2+26, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_button)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
