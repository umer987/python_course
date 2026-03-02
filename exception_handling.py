#exception handling file
# number =  int(input("ENTER THE NMBER TO DIVIDE"))
# try:
#     print(10/ number)
# except ZeroDivisionError:
#     print("PLEASE DONT ENTER ZERO")

# print("DONE")

#handle exception as error (err) try-except
# number =  int(input("ENTER THE NMBER TO DIVIDE"))
# try:
#     print(10/ number)
# except Exception as err:
#     print(f"ERROR {err}")

# print("DONE")

#handle exception as error (err) try-except-else if except run so else wont and else run except wont run
number =  int(input("ENTER THE NMBER TO DIVIDE"))
try:
    print(10/ number)
except Exception as err:
    print(f"ERROR {err}")
