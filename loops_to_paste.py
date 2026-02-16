"""print("::::::::::::::::::::::::::::::::::TABLE PROGRRAM:::::::::::::::::::::::::::::::::::")
number = int(input("ENTER NUMBER FOR TABLE"))
for i in range(1,11,1):
    print(f"{number} X {i} = {number*i}")"""

#sum up to n numbers
number = int(input("ENTER NUMBER TO SUM"))
add=0
for i in range(1,number+1,1):
    print(i)
    add += i
    print("ADDITON ",add)