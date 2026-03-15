import json 
import random
import string
from pathlib import Path

#class bank
class Bank:
    #create account
    database = 'data.json'
    data =[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                 data = json.loads(fs.read())
