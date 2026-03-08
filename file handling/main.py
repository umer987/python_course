import os
print("PRESS 1 FOR CREATE A FILE")
print("PRESS 2 FOR READ A FILE")
print("PRESS 3 FOR UPDATE A FILE")
print("PRESS 4 FOR DELETE A FILE")
check = int(input("PLEASE ENTER THE NUMBER"))

def create():
    filename = input("ENTER FILE NAME")
    filecontent= input("ENTER FILE CONTENT")
    f =open(f"{filename}.txt",'w') 
    f.write(filecontent)
    f.close()

def read():
    filename = input("ENTER FILE NAME TO READ")
    f = open(rf"{filename}.txt")
    print(f.read())

def update():
    filename = input("ENTER FILE NAME")
    filecontent= input("ENTER FILE CONTENT")
    f =open(f"{filename}.txt",'a') 
    f.write(filecontent)
    f.close()

def delete():
    filename = input("ENTER FILE NAME")
    os.remove(f"{filename}.txt")
    print(f"File {filename} deleted successfully")

if check == 1:
    create()
elif check == 2:
    read()
elif check == 3:
    update()
elif check == 4:
    delete()
elif check >=4:
    print("YOU ENTER THE WRONG NUMBER CHOICE SHOULD BE 1,2,3,4")