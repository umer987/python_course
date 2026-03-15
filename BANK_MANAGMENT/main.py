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

#create account close        
    
#deposite money

    def deposite(self):
        acc_num = input("PLEASE ENTER YOUR ACCOUNT NUMBER:- ")            
        acc_pin = int(input("PLEASE ENTER 4 DIGIT PIN:- "))
        user_data = [i for i in Bank.data if i['accountNo.'] == acc_num and i['pin'] == acc_pin]            

        if user_data == False:
            print("ACCOUNT NOT FETCH")
        else:
            amount = int(input("how much you want to depoit "))
            if amount  > 100000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")

#deposite account close

#withdrwal open
    def withdrwal(self):
        acc_num = input("PLEASE ENTER YOUR ACCOUNT NUMBER:- ")            
        acc_pin = int(input("PLEASE ENTER 4 DIGIT PIN:- "))
        user_data = [i for i in Bank.data if i['accountNo.'] == acc_num and i['pin'] == acc_pin]            

        if user_data == False:
            print("ACCOUNT NOT FETCH")
        else:
            amount = int(input("how much you want to depoit "))
            if amount > user_data[0]['balance']:
                print("TRANSCTION INCOMPLETE DUE INSUFFICENT BALANCE")

            else:
                user_data[0]['balance'] -= amount
                Bank.__update()
                print("AMOUNT WITHDRWAL SUCCESSFULLY ")

#widthdrawl close

#details open
    def details(self):
        acc_num = input("PLEASE ENTER YOUR ACCOUNT NUMBER:- ")            
        acc_pin = int(input("PLEASE ENTER 4 DIGIT PIN:- "))
        user_info = [i for i in Bank.data if i['accountNo.'] == acc_num and i['pin'] == acc_pin]
        for i in user_info[0]:
            print(f"{i} : {user_info[0][i]}")

#details close

#update details open

    
    def update_details(self):
        acc_num = input("PLEASE ENTER YOUR ACCOUNT NUMBER:- ")            
        acc_pin = int(input("PLEASE ENTER 4 DIGIT PIN:- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == acc_num and i['pin'] == acc_pin]
        print("ENTER UPDATED DETAILS OR JUST PRESS ENTER TO LEVE IT AS IT IS")
        newdata ={
