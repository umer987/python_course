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
    
