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
