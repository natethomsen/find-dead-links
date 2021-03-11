#!/usr/bin/env
import requests
from bs4 import BeautifulSoup
from sys import argv

url = argv[1]
try:
    site = requests.get(url)
    if r.status_code not in [200, 302]:
        print('Bad link')
except:
    print('Bad link')

