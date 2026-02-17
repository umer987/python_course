"""print("::::::::::::::::::::::::::::::::::TABLE PROGRRAM:::::::::::::::::::::::::::::::::::")
number = int(input("ENTER NUMBER FOR TABLE"))
for i in range(1,11,1):
    print(f"{number} X {i} = {number*i}")"""

"""#sum up to n numbers
number = int(input("ENTER NUMBER TO SUM"))
add=0
for i in range(1,number+1,1):
    print(i)
    add += i
    print("ADDITON ",add)"""
#factorial program
"""number = int(input("ENTER NUMBER TO FACRORIAL"))
fact=1
for i in range(1,number+1,1):
  fact*=i
print(fact)"""


#if number i sperfect or not
number = int(input("ENTER NUMBER TO CHECK IF IT IS PERFECT OR NOT"))
factors = 0 
for i in range(1,number,1):
    if number % i == 0:
        factors+=i

if number == factors:
    print("GIVEN NUMBER IS PERFECT")
else:
    print("GIVEN NUMBER IS NOT PERFECT")