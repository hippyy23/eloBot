from tkinter import *
import lib.cfg

box = Tk()
box.geometry("250x130")
box.resizable(False, False)

faceitLogin = ""
channelName = ""


def quit():
    box.destroy()


def login():
    lib.cfg.NAME = entryLogin.get()


def channel():
    lib.cfg.CHANNEL = entryChannel.get()


startButton = Button(box, text="START", command=quit)
startButton.place(x=100, y=90)

labelLogin = Label(box, text="INSERT YOUR FACEIT LOGIN")
labelLogin.pack()

entryLogin = Entry(box)
entryLogin.pack()

labelChannel = Label(box, text="INSERT YOUR CHANNEL NAME")
entryChannel = Entry(box)

labelChannel.pack()
entryChannel.pack()

checkButtonLogin = Button(box, text="check", command=login)
checkButtonLogin.place(x=200, y=17)

checkButtonChannel = Button(box, text="check", command=channel)
checkButtonChannel.place(x=200, y=57)


box.mainloop()
