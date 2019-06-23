import lib.cfg
import urllib, json
import time, threading
from time import sleep


__author__ = "Munteanu Adrian"
__copyright__ = "Copyright 2019, EloBot"
__credits__ = ["Munteanu Adrian"]

__version__ = "0.1"
__email__ = "adrinarol@gmail.com"


def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(lib.cfg.CHANN, msg).encode("utf-8"))


def thread_fill_op_list():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/INSERT NAME CHANNEL/chatters"
            req = urllib.Request(url, header={"accept": "*/*"})
            response = urllib.urlopen(req).read()
            if response.find("502 Bad Gateway") == -1:
                lib.cfg.oplist.clear()
                data = json.loads(response)
                for p in data["chatters"]["moderators"]:
                    cfg.oplist[p] = "mod"
                for p in data["chatters"]["viewers"]:
                    cfg.oplist[p] = "viewers"
        except:
            'do nothing'
        #sleep(5)
        

def isOp(user):
    return user in lib.cfg.oplist