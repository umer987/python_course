#number guessing game
# import random

# number = random.randint(1, 100)
# attempts = 0

# print("Guess the number between 1 and 100!")

# while True:
#     try:
#         guess = int(input("Enter your guess: "))
#         attempts += 1
        
#         if guess < number:
#             print("Too low!")
#         elif guess > number:
#             print("Too high!")
#         else:
#             print(f"Correct! You guessed it in {attempts} attempts!")
#             break
#     except ValueError:
#         print("Please enter a valid number!")


#simple calculator
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Invalid operation!")
            return
            
        print(f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Please enter valid numbers!")

calculator()