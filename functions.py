"""#simple function
def add_2_number():
    print("function called")
add_2_number()

#parameterized function
number_1 = int(input("ENTER NUMBER 1:- "))
number_2 = int(input("ENTER NUMBER 2:- "))
def add(a,b):
    print("THE ADDITION OF 2 NUMBERS IS ", a+b)
add(number_1,number_2)"""

stng =input("ENTER AN STRING TO CHECK PALANDROM")
def chck_plndro(a):
    lng = len(a)
    new =""
    for i in range(lng-1,-1,-1):
        new+=a[i]
    if new == a:
        print("STRING IS PALANDROM")
        
    else:
        print("STRING IS NOT PALANDROM")
chck_plndro(stng)
