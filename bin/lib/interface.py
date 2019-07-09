from tkinter import *
#import lib.cfg

box = Tk()
box.geometry("370x220")
box.resizable(False, False)

faceitLogin = ""
channelName = ""
status = BooleanVar()


def quit():
    box.destroy()


def login():
    lib.cfg.faceitLogin = entryLogin.get()


def channel():
    lib.cfg.CHANN = entryChannel.get()


def onstartup():
    pass


###############################################################
saveButton = Button(box, text="SAVE", command=quit)
saveButton.place(x=180, y=200)
###############################################################
onstartupARadiobutton = Radiobutton(box, text="on startup ACTIVATE", command=onstartup, value=True, variable=status).place(x=50, y=100)
onstartupFRadiobutton = Radiobutton(box, text="on startup DISACTIVATE", command=onstartup, value=False, variable=status).place(x=50, y=120)
###############################################################
labelLogin = Label(box, text="INSERT YOUR FACEIT LOGIN")
labelLogin.pack()
labelLogin.place(x=135, y=5)
###############################################################
entryLogin = Entry(box)
entryLogin.pack()
entryLogin.place(x=115, y=25)
###############################################################
labelChannel = Label(box, text="INSERT YOUR CHANNEL NAME")
labelChannel.pack()
labelChannel.place(x=125, y=55)
###############################################################
entryChannel = Entry(box)
entryChannel.pack()
entryChannel.place(x=115, y=75)
###############################################################
insertButtonLogin = Button(box, text="insert", command=login)
insertButtonLogin.place(x=310, y=25)
###############################################################
insertButtonChannel = Button(box, text="insert", command=channel)
insertButtonChannel.place(x=310, y=75)

box.mainloop()
