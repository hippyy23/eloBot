from tkinter import *
import os
import getpass
import lib.cfg

box = Tk()
box.geometry("350x170")
box.resizable(False, False)

#faceitLogin = ""
#channelName = ""
status = BooleanVar()


def quit():
    lib.cfg.faceitLogin = entryLogin.get()
    lib.cfg.CHANN = entryChannel.get()
    box.destroy()
    #box.wm_state('withdraw')

'''
def onstartupTrue():
    pass


def onstartupFalse():
    user = getpass.getuser()
    if os.path.exists("C:\\Users\\" + user + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\bot.exe"):
        os.remove("C:\\Users\\" + user +
                  "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\bot.exe")
'''


###############################################################
saveButton = Button(box, text="SAVE", command=quit)
saveButton.place(x=180, y=130)
startButton = Button(box, text="START", command=quit)
startButton.place(x=130, y=130)
###############################################################

'''
onstartupARadiobutton = Radiobutton(box, text="on startup ACTIVATE",
                                    command=onstartupTrue, value=True, variable=status).place(x=10, y=30)
onstartupFRadiobutton = Radiobutton(box, text="on startup DISACTIVATE",
                                    command=onstartupFalse, value=False, variable=status).place(x=10, y=60)
'''

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
