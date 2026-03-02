#exception handling file
number =  int(input("ENTER THE NMBER TO DIVIDE"))
try:
    print(10/ number)
except ZeroDivisionError:
    print("PLEASE DONT ENTER ZERO")

