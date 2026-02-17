"""#accept an integer and print N number of times hello world
j = int(input("ENTER THE NUMBER OF TIMES YOU WANT TO PRINT HELLO WORLD"))
for i in range(1,j+1,1):
    print("HELLO WORLD")"""

"""#print the natural number upto N
j = int(input("ENTER THE NUMBER TO PRINT"))
for i in range(1,j+1,1):
    print(i)"""

"""#(ENHANCED) print the natural number upto N
l = int(input("ENTER THE NUMBER TO START"))
j = int(input("ENTER THE NUMBER TO STOP"))
for i in range(l,j+1,1):
    print(i)"""

"""#print negative number to N
l = int(input("ENTER THE NUMBER TO START"))
for i in range(l ,0,-1):
    print(i)
"""
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


"""#if number i sperfect or not
number = int(input("ENTER NUMBER TO CHECK IF IT IS PERFECT OR NOT"))
factors = 0 
for i in range(1,number,1):
    if number % i == 0:
        factors+=i

if number == factors:
    print("GIVEN NUMBER IS PERFECT")
else:
    print("GIVEN NUMBER IS NOT PERFECT")"""

"""#check number is prime or composite
count =0
number = int(input("ENTER NUMBER TO CHECK IF IT IS PRIME OR NOT"))
for i in range(1,11,1):
    if number % i == 0:
        count=count+1
if count <= 2:
    print("GIVEN NUMBER IS PRIME")
else:
    print("GIVEN NUMBER IS COMPOSITE") """

"""#reverse the string
rev ="SYED MUHAMMAD UMER"
leng= len(rev)-1
for i in range(leng,-1,-1):
    print(rev[i])"""

"""#check word is palandrom or not
word_one = input("ENTER THE WORD")
word2= ""
l_of_word = len(word_one)-1
for i in range(l_of_word , -1 , -1):
    word2+= word_one[i]
if word_one == word2:
    print("GIVEN WORD IS PALANDROME")
else:
    print("GIVEN WORD IS NOT PALANDROME")"""
      
#check how many characters numbers and characters in the string
abc= input("ENTER THE WORD")
string_count=0
int_count=0
char_count=0
for i in range(0,len(abc),1):
    if abc[i].isalpha():
        string_count+=1
    elif abc[i].isdigit() :
        int_count+=1
    else:
        char_count+=1
print(f"IN GIVEN WORD THERE ARE {string_count} ALPHABATES , {int_count} INTEGER , {char_count} CHARACTERS")



   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
