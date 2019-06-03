import requests
import lib.cfg
import time
from bs4 import BeautifulSoup
from time import sleep
import re


__author__ = "Munteanu Adrian"
__copyright__ = "Copyright 2019, EloBot"
__credits__ = ["Munteanu Adrian"]

__version__ = "0.1"
__email__ = "adrinarol@gmail.com"


def get_elo():
    while True:
        url = 'https://faceitstats.com/steam,76561198894299878'
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        string = str(soup.prettify().encode("utf-8"))
        string = string.replace(" ", "")
        eloIndex = string.find("ELOis")
        elo = string[eloIndex + 17 : eloIndex + 21]
        lib.cfg.elolist.clear()
        lib.cfg.elolist.append(elo)
        sleep(300)
