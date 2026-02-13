#voting system by using IF-ELSE
print("::::::::::::::::::::::::::::::::::::::::::::::::VOTING SYSTEM::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
age = int(input("ENTER YOUR AGE"))
if age > 18:
    print("YOU ARE ELIGIBLE FOR VOTING")

else:
    print("YOU ARE NOT ELIGBLE FOR VOTING")

print("::::::::::::::::::::::::::::::::::::ELSE ELIF ELSE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
age = int(input("ENTER YOUR AGE"))
if age >= 18:
    print("YOU ARE ELIGIBLE FOR VOTING")
elif age >= 15 or age <18:
    print("VOTE PRACTICE YOU CAN VOTE BUT YOUR VOTE WILL NOT CONSIDER SERIOUS")
else:
    print("YOU ARE NOT ELIGBLE FOR VOTING")
    