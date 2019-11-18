import lib.cfg

lib.cfg.faceitLogin = str(input("Insert your faceit login: "))
lib.cfg.CHANN = str(input("Insert your channel name: "))

if (str(input("Start bot with windows\n[y/n]: ")) == "y"):
    lib.cfg.onstartup = True

