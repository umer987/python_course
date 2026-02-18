#seprate each digit of a given number and and print it on a new line
number = input("ENTER THE NUMBER")
leno = 0
while leno != len(number):
    print(number[leno])
    leno += 1
print("string to int" , int(number)+1)
