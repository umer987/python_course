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


# # Temperature Converter
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print("Temperature Converter")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")

# choice = input("Choose (1/2): ")

# if choice == '1':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius}°C = {fahrenheit}°F")
# elif choice == '2':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print(f"{fahrenheit}°F = {celsius}°C")
# else:
#     print("Invalid choice!")

#pasword genrator 
# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# length = int(input("Enter password length (default 12): ") or 12)
# password = generate_password(length)
# print(f"Generated password: {password}")

#palandrome checker
# def is_palindrome(text):
#     # Remove spaces and convert to lowercase
#     cleaned_text = ''.join(text.lower().split())
#     return cleaned_text == cleaned_text[::-1]

# word = input("Enter a word or phrase: ")
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome!")
# else:
#     print(f"'{word}' is not a palindrome.")

#multiplication table
# def multiplication_table(number, upto=10):
#     print(f"Multiplication Table for {number}")
#     print("-" * 20)
#     for i in range(1, upto + 1):
#         print(f"{number} × {i:2} = {number * i:4}")

# num = int(input("Enter a number: "))
# limit = int(input("Enter limit (default 10): ") or 10)
# multiplication_table(num, limit)

#word counter
# def count_words(text):
#     words = text.split()
#     word_count = {}
    
#     for word in words:
#         word = word.lower().strip('.,!?()[]{}":;')
#         word_count[word] = word_count.get(word, 0) + 1
    
#     return word_count

# text = input("Enter a sentence or paragraph: ")
# word_counts = count_words(text)

# print("\nWord frequencies:")
# for word, count in sorted(word_counts.items()):
#     print(f"'{word}': {count}")

#rock paper secissor
import random

# choices = ['rock', 'paper', 'scissors']
# computer_score = 0
# player_score = 0

# while True:
#     computer = random.choice(choices)
#     player = input("\nEnter rock, paper, scissors (or 'quit'): ").lower()
    
#     if player == 'quit':
#         break
#     if player not in choices:
#         print("Invalid choice!")
#         continue
    
#     print(f"Computer chose: {computer}")
    
#     if player == computer:
#         print("It's a tie!")
#     elif (player == 'rock' and computer == 'scissors') or \
#          (player == 'paper' and computer == 'rock') or \
#          (player == 'scissors' and computer == 'paper'):
#         print("You win!")
#         player_score += 1
#     else:
#         print("Computer wins!")
#         computer_score += 1

# print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")