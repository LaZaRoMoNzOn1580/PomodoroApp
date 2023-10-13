from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_Timer.config(text="Timer")
    label_check_on.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
        window.after(1, lambda: window.focus_force())
        label_Timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
        window.after(1, lambda: window.focus_force())
        label_Timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_Timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
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
        check_on = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check_on += "✔"
        label_check_on.config(text=check_on)


# ---------------------------- UI SETUP ------------------------------- #
# Create to window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canva Widget
canvas = Canvas(width=220, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Button Widget
button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=YELLOW, highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=YELLOW, highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

# Label Widget
label_Timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label_Timer.grid(row=0, column=1)

label_check_on = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
label_check_on.grid(row=3, column=1)

window.mainloop()
