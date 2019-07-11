import os
import getpass


def create_shortcut():
    currentpath = os.getcwd()
    currentpath = "\"" + currentpath + "\""
    user = getpass.getuser()
    f = open(".\\bin\createShortcut.vbs", "w")
    f.write("Set oWS = WScript.CreateObject(\"WScript.Shell\")\n"
    + "Set wshShell = CreateObject(\"WScript.Shell\")\n"
    + "homepath=wshShell.ExpandEnvironmentStrings(\"%homepath%\")\n"
    + "sLinkFile = homepath & \"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\bot.lnk\"\n"
    + "Set oLink = oWS.CreateShortcut(sLinkFile)\n"
    + "oLink.TargetPath = " + currentpath + "\\bot.exe\n"
    + "oLink.Save")


create_shortcut()
