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
        # string = str(re.sub(r"\n", "", string)) work in progress
        string = string.replace(" ", "")
        string = re.sub("<.*?>", "", string)
        eloIndex = string.find("ELOis")
        elo = string[eloIndex + 9 : eloIndex + 13]
        lib.cfg.elo = elo
        sleep(300)
