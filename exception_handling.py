#exception handling file
# number =  int(input("ENTER THE NMBER TO DIVIDE"))
# try:
#     print(10/ number)
# except ZeroDivisionError:
#     print("PLEASE DONT ENTER ZERO")

# print("DONE")

#handle exception as error (err) try-except
# number =  int(input("ENTER THE NMBER TO DIVIDE"))
# try:
#     print(10/ number)
# except Exception as err:
#     print(f"ERROR {err}")

# print("DONE")

#handle exception as error (err) try-except-else if except run so else wont and else run except wont run
# number =  int(input("ENTER THE NMBER TO DIVIDE"))
# try:
#     print(10/ number)
# except Exception as err:
#     print(f"ERROR {err}")
# else:
#     print("OK DONE SYED MUHAMMMAD UMER")
# print("DONE")


"""
EXCEPTION FUN HOUSE - Small but Complete!
A mini program showing 5 different exception types in action
"""

def exception_fun_house():
    print("🎪 WELCOME TO THE EXCEPTION FUN HOUSE! 🎪")
    print("Where errors become entertainment!\n")
    
    while True:
        print("\n" + "="*40)
        print("Choose your adventure:")
        print("1. 🧮 Math Disaster (ZeroDivisionError)")
        print("2. 📝 Text Trap (ValueError)")
        print("3. 📋 List Labyrinth (IndexError)")
        print("4. 🔑 Key Chaos (KeyError)")
        print("5. 📁 File Funhouse (FileNotFoundError)")
        print("6. 🚪 Exit")
        
        choice = input("\nYour choice (1-6): ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter a number to divide 10 by: "))
                result = 10 / num
                print(f"✅ 10 ÷ {num} = {result}")
            except ZeroDivisionError:
                print("❌ BOOM! Can't divide by zero, genius!")
            except ValueError:
                print("❌ That's not even a number!")
                
        elif choice == '2':
            try:
                age = int(input("Enter your age: "))
                if age < 0:
                    raise ValueError("Age can't be negative!")
                print(f"✅ You are {age} years old")
            except ValueError as e:
                print(f"❌ Oops! {e}")
        elif choice == '3':
            my_list = ['🐶', '🐱', '🐭', '🐹']
            print(f"Animal list: {my_list}")
            try:
                index = int(input("Enter index (0-3): "))
                print(f"You got: {my_list[index]}")
            except IndexError:
                print(f"❌ No animal at index {index}! Try 0-3")
            except ValueError:
                print("❌ That's not a number!")
                
        elif choice == '4':
            my_dict = {'apple': '🍎', 'banana': '🍌', 'cherry': '🍒'}
            print(f"Fruits: {my_dict}")
            try:
                fruit = input("Enter fruit name: ").lower()
                print(f"Here's your fruit: {my_dict[fruit]}")
            except KeyError:
                print(f"❌ Sorry, no {fruit} here! Try apple, banana, or cherry")
                
        elif choice == '5':
            filename = input("Enter filename to read: ")
            try:
                with open(filename, 'r') as f:
                    print(f"📄 First line: {f.readline().strip()}")
            except FileNotFoundError:
                print(f"❌ File '{filename}' doesn't exist!")
                create = input("Create it? (y/n): ").lower()
                if create == 'y':
                    with open(filename, 'w') as f:
                        f.write("You created this file!")
                    print(f"✅ Created '{filename}' for you!")
                    
        elif choice == '6':
            print("\n🎉 Thanks for visiting the Exception Fun House!")
            print("Remember: Errors aren't scary when you handle them! 🚀")
            break
            
        else:
            print("❌ Invalid choice! Try 1-6")

# Run it!
if __name__ == "__main__":
    exception_fun_house()                



# MINI EXCEPTION DEMO - 15 lines only!

def mini_exceptions():
    while True:
        print("\n1. Divide 2. Index 3. Convert 4. Quit")
        choice = input("Choice: ")
        
        if choice == '1':
            try: print(f"10 / {n:=int(input('Number: '))} = {10/n}")
            except ZeroDivisionError: print("No zero!")
            except ValueError: print("Numbers only!")
                
        elif choice == '2':
            items = ['a','b','c']
            try: print(f"Item: {items[int(input('Index (0-2): '))]}")
            except (IndexError, ValueError): print("Invalid index!")
                
        elif choice == '3':
            try: print(f"Number: {int(input('Enter number: '))}")
            except ValueError: print("That's not a number!")
                
      