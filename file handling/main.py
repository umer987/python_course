import os
print("PRESS 1 FOR CREATE A FILE")
print("PRESS 2 FOR READ A FILE")
print("PRESS 3 FOR UPDATE A FILE")
print("PRESS 4 FOR DELETE A FILE")
check = int(input("PLEASE ENTER THE NUMBER"))
if check == 1:
    filename = input("ENTER FILE NAME")
    filecontent= input("ENTER FILE CONTENT")
    f =open(f"{filename}.txt",'w') 
    f.write(filecontent)
    f.close()
elif check == 2:
    filename = input("ENTER FILE NAME TO READ")
    f = open(rf"{filename}.txt")
    print(f.read())
elif check == 3:
    filename = input("ENTER FILE NAME")
    filecontent= input("ENTER FILE CONTENT")
    f =open(f"{filename}.txt",'a') 
    f.write(filecontent)
    f.close()
elif check == 4:
     filename = input("ENTER FILE NAME")
     os.remove(f"{filename}.txt")
     print(f"File {filename} deleted successfully")