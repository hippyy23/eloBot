import lib.setup
import lib.utils
import lib.cfg
import socket
import re
import time
import threading
import lib.faceitelo
from time import sleep


__author__ = "Munteanu Adrian"
__copyright__ = "Copyright 2019, EloBot"
__credits__ = ["Munteanu Adrian"]

__version__ = "0.1"
__email__ = "adrinarol@gmail.com"


def main():
    s = socket.socket()
    s.connect((lib.cfg.HOST, lib.cfg.PORT))
    s.send("PASS {}\r\n".format(lib.cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(lib.cfg.PASS).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(lib.cfg.CHANN).encode("utf-8"))

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

    threading._start_new_thread(lib.utils.thread_fill_op_list, ())

    threading._start_new_thread(lib.faceitelo.get_elo, ())

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            print(response)

            if message.strip() == "!elo":
                lib.utils.chat(s, "s4tanax's current elo: " +
                               lib.cfg.elo)
        #sleep(1)


if __name__ == "__main__":
    main()
