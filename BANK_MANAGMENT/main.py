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
        else:
            print("NO SUCH FILE EXISTS")
    except Exception as err:
        print(f"THERE IS AN ERROR {err}")





    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenrate(cls):
        alp = random.choices(string.ascii_letters,k=4)
        num = random.choices(string.digits, k=4)
        spcchar = random.choices("!@#$%^&*",k=1)
        acc_id = num + alp + spcchar
        random.shuffle(acc_id)
        return "".join(acc_id)
 
    def create_account(self):
        datai ={
            "name":input("YOUR NAME:- "),
            "age":int(input("YOUR AGE:- ")),
            "email":input("YOUR EMAIL:- "),
            "pin":int(input("YOUR PIN:- ")),
            "accountNo.":Bank.__accountgenrate(),
            "balance":0
        }
        if datai['age'] < 18 or len(str(datai['pin'])) != 4:
            print("SORRY YOU CANT CREATE ACCOUNT")
        else:
            print("ACCOUNT CREATED SUCCUSS FULLY")
            Bank.data.append(datai)
            Bank.__update()
        for i in datai:
            print(f"{i} {datai[i]}")    
        print("PLEASE NOTE DOWN YOUR ACCOUNT NUMBER")
