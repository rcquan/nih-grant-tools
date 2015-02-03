#!/usr/bin/python

import pandas as pd
from bs4 import BeautifulSoup
import re

pattern = re.compile('(?<=PMid:)[0-9]+')

doc = open("references_results.html").read()
soup = BeautifulSoup(doc)

table = soup.find("table", attrs={'class':'resultB'})

rows = table.findAll('td', attrs={'class': 'resultB', 'colspan': "4"})
for row in rows:
    match = pattern.search(row.text)
    if match:
        print match.group()
    print "No match found!"
