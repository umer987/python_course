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
# def calculator():
#     print("Simple Calculator")
#     print("Operations: +, -, *, /")
    
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         operation = input("Enter operation (+, -, *, /): ")
        
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 print("Error: Division by zero!")
#                 return
#         else:
#             print("Invalid operation!")
#             return
            
#         print(f"Result: {num1} {operation} {num2} = {result}")
#     except ValueError:
#         print("Please enter valid numbers!")

# calculator()


# Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Invalid choice!")