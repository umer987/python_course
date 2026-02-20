"""#seprate each digit of a given number and and print it on a new line
number = input("ENTER THE NUMBER")
leno = 0
while leno != len(number):
    print(number[leno])
    leno += 1
print("string to int" , int(number)+1)"""

"""#seprate each digit of a given number and and print it on a new line reverse order
number = input("ENTER THE NUMBER")
leno = len(number)
while leno != 0:
    print(number[leno-1])
    leno -= 1"""

"""#accept the number and print its reverse
number = input("ENTER THE NUMBER")
leno = len(number)
while leno != 0:
    print(number[leno-1])
    leno-=1"""



"""#random number game
import random
number = random.randint(0,11)
guess = int(input("ENTER A NUMBER"))
if guess == number:
    print("YOU ARE RIGHT NUMBER IS ", number )
else:
    print("TRY AGAIN NUMBER WAS ", number)"""

"""import random
number = random.randint(0,11)
count = 1
while count !=4:
    guess = int(input(f"ENTER A NUMBER ATTEMPT# {count}"))
    count += 1
    if guess == number:
        print("ATTEMPT#",count)
        print("YOU ARE RIGHT NUMBER IS ", number )

print("TRY AGAIN NUMBER WAS ", number)"""


#for loop program to make non syymetric paramid
for i in range(1,11,1):
    for j in range(1,i,1):
        print("*")
        print(" ")
