import requests
import lib.cfg
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
        url = 'https://faceitstats.com/player,' + lib.cfg.faceitLogin
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for tag in soup.find_all("strong"):
            if (re.match("^[0-9]+$", tag.text)):
                lib.cfg.elo = tag.text
                break
        sleep(300)