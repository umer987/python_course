
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



   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   #decotrators
# def say_hello():
#     print("Hello")

# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

#addition decorator
# def decorator(func):
#     def wrapper(a,b):
#         print("THE TOTAL ADDITION OF YOUR NUMBERS ARE:- ")
#         func(a,b)
#         print("THANK YOU")
#     return wrapper
    
# @decorator
# def add(a,b):
#     print(a+b)

# add(1,2)

# def decorator(func):
#     def wrapper(*args):
#         print("THE TOTAL ADDITION OF YOUR NUMBERS ARE:- ")
#         func(*args)
#         print("THANK YOU")
#     return wrapper
    
# @decorator
# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# add(1,3,7,2)



# *args is used when you dont know the number of aurguments your function is reciving and it stores data in tuple form

# def a(a,b):
#     print(a+b)
# a(1,2) #if we give more than 2 aurguments i will give error


# def a(*args):
#     sum =0
#     print(args)
#     for i in args:
#         sum = sum+i
       
#     print("THE TOTAL ADDITION OF NUMBERS IS " , sum)

# a(1,2,3,4,5,6,7,8,9) #now you can give more than expected aurguments 


# **kwargs is used to get aurguments with key value pair and it saves value in dictonary
# def info(**kwargs):
#     print(kwargs)

# info(name="umer",age="22",gender="male")

# def info(**kwargs):
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# info(name="umer",age="22",gender="male")
