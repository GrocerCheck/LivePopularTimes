import crawler
import sqlite3
from sqlite3 import Error
import time

cur = sqlite3.connect('db1.sqlite3').cursor()
cur.execute("SELECT address FROM map_store")
addresslist = cur.fetchall()
addresslist = [addresslist[x][0] for x in range(len(addresslist))]
addresslist = [x+""



(Urban Fare) 305 Bute Street, Vancouver BC, Canada
