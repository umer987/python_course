"""a = range(0 , 20 , 1)
for i in a:
    print(i)"""
"""for i in range(1 , 20 ,2):
    print(i)"""

"""print("::::::::::::::::::::::::::::::::::::::::::::::::SIMPLE TABLE PROGRAM:::::::::::::::::::::::::::::::::::::::::::::")
a= int(input("ENTER NUMBER FOR TABLE"))
for i in range(1 ,11, 1):
    print(f" {a} X {i} = {a*i}" )"""
"""
#reverse loop
for i in range(-5,-15,-1):
    print(i)"""
#TABLE WITH DIRECT LOOP
"""print("::::::::::::::::::::::::::::::::::::::::::::::TABLE WITH DIRECT LOOP:::::::::::::::::::::::::::::::::::::::::::::::::")
a = int(input("ENTER INTEGER FOR MULTIPLICATION TABLE"))
for i in range(a , a*10+1, a):
    print(i)"""

#LOOPS FOR STRINGS
"""a ="SYED MUHAMMAD UMER"
for i in range(0 ,18,1):
    print(a[i])"""

"""a ="SYED MUHAMMAD UMER"
print(len(a))
for i in range(len(a)):
    print(a[i])"""

"""a ="SYED MUHAMMAD UMER"
for i in a:
    print(i)"""
"""#will print tonly till 14 after 14 loop with be exit
for i in range(1,21,1):
    if i ==15:
        break
    print(i)"""
#thil will print all values except 15 bracause on 15 loop is redirecting to 14 to 16 directly
"""for i in range(1,21,1):
    if i == 15:
        continue
    print(i)
"""
#BREAK AND ELSE USE CASE
"""for i in range(1,21,1):
    if i== 15:
        print("BREAK WORKS AND ELSE NOT")
        break
else:
    print("ELSE WORK AND BREAK NOT")"""
"""for i in range(1,21,1):
    if i== 115:
        print("BREAK WORKS AND ELSE NOT")
        break
else:
    print("ELSE WORK AND BREAK NOT")
"""
#for loop question to print left paramid
for i in range(1,10,1):
    for j in range(1,i,1):
        print("*")
    

