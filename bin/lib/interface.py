from tkinter import *
import os
#import lib.cfg

box = Tk()
box.geometry("350x170")
box.resizable(False, False)

faceitLogin = ""
channelName = ""
status = BooleanVar()


def quit():
    box.wm_state('withdraw')
    login()
    channel()
    

def login():
    lib.cfg.faceitLogin = entryLogin.get()


def channel():
    lib.cfg.CHANN = entryChannel.get()


def onstartup():
    currentpath = os.popen('cd')
    cmd = os.popen('')


###############################################################
saveButton = Button(box, text="SAVE", command=quit)
saveButton.place(x=180, y=130)
startButton = Button(box, text="START", command=quit)
startButton.place(x=130, y=130)
###############################################################
onstartupARadiobutton = Radiobutton(box, text="on startup ACTIVATE", command=onstartup, value=True, variable=status).place(x=10, y=30)
onstartupFRadiobutton = Radiobutton(box, text="on startup DISACTIVATE", command=onstartup, value=False, variable=status).place(x=10, y=60)
###############################################################
labelLogin = Label(box, text="FACEIT LOGIN")
labelLogin.pack()
labelLogin.place(x=180, y=5)
###############################################################
entryLogin = Entry(box)
entryLogin.pack()
entryLogin.place(x=185, y=25)
###############################################################
labelChannel = Label(box, text="CHANNEL NAME")
labelChannel.pack()
labelChannel.place(x=180, y=55)
###############################################################
entryChannel = Entry(box)
entryChannel.pack()
entryChannel.place(x=185, y=75)


box.mainloop()
