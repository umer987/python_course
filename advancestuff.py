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