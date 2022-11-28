import tkinter.messagebox
from tkinter import *
import time
import mp3play

'''
Initialize window w/ label, inputs, buttons
'''
# initializare window pt interfata
root = Tk()
# set titlu, dimensiuni, culoare background, not resizable
root.title("Temporizer")
root.geometry("400x500")  # WxH
root.config(bg="grey")
root.resizable(False, False)

# text sub forma de label
heading = Label(root, text="Temporizer", font="arial 25 bold", bg="grey", fg="black")
heading.pack(pady=10)

# clock timestamp curent sub forma de text label
Label(root, font=("arial", 15, "bold"), text="current time:", bg="white").place(x=65, y=70)

current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#000", bg="yellow")
current_time.place(x=190, y=70)

# elemente pt timer
# hrs -> nr ore, stringvar - variabila legata de entitatea Entry
hrs = StringVar()
hrs_entry = Entry(root, textvariable=hrs, width=2, font="arial 50", bd=0)
hrs_entry.place(x=40, y=155)
hrs.set("00")

minutes = StringVar()
minutes_entry = Entry(root, textvariable=minutes, width=2, font="arial 50", bd=0)
minutes_entry.place(x=160, y=155)
minutes.set("00")

sec = StringVar()
sec_entry = Entry(root, textvariable=sec, width=2, font="arial 50", bd=0)
sec_entry.place(x=280, y=155)
sec.set("00")

Label(root, text="HOURS", font="arial 12 bold", bg="grey", fg="Black").place(x=45, y=125)
Label(root, text="MINUTES", font="arial 12 bold", bg="grey", fg="Black").place(x=160, y=125)
Label(root, text="SECONDS", font="arial 12 bold", bg="grey", fg="Black").place(x=275, y=125)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(100, clock)


# seteaza current timestamp
clock()

# da play la sunet cand expira timpul (prin fct lambda 'play')

f = mp3play.load('time.mp3')
play = lambda: f.play()

# variabila care ajuta la stop-reset timer on=True (enable start) on=False (freeze countdown sau reset)
on = True


def start():
    times = int(hrs.get()) * 3600 + int(minutes.get()) * 60 + int(sec.get())
    global hrs_entry
    global on
    global minutes_entry
    global sec_entry

    hrs_entry.configure(state="readonly")
    minutes_entry.configure(state="readonly")
    sec_entry.configure(state="readonly")
    on = True

    while times > -1 and on is True:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(str(second))
        minutes.set(str(minute))
        hrs.set(str(hour))

        root.update()
        time.sleep(1)

        if times == 0:
            play()
            tkinter.messagebox.showinfo(message="Time's up!")
            sec.set("00")
            minutes.set("00")
            hrs.set("00")
            hrs_entry.configure(state="normal")
            minutes_entry.configure(state="normal")
            sec_entry.configure(state="normal")
        times -= 1


def stop():
    global on
    on = False


def reset():
    global on
    on = False
    hrs_entry.configure(state="normal")
    minutes_entry.configure(state="normal")
    sec_entry.configure(state="normal")
    sec.set("00")
    minutes.set("00")
    hrs.set("00")


# poze si butoane
reset_photo = PhotoImage(file="button_reset.png")
button_stop = Button(root, bg="grey", bd=0, fg="grey", width=173, height=80, image=reset_photo, command=reset)
button_stop.pack(padx=0, pady=0, side=BOTTOM)

stop_photo = PhotoImage(file="button_stop.png")
button_stop = Button(root, bg="grey", bd=0, fg="grey", width=173, height=80, image=stop_photo, command=stop)
button_stop.pack(padx=0, pady=0, side=BOTTOM)

start_photo = PhotoImage(file="button_start.png")
button_start = Button(root, bg="grey", bd=0, fg="grey", width=173, height=80, image=start_photo, command=start)
button_start.pack(padx=0, pady=0, side=BOTTOM)

root.mainloop()
