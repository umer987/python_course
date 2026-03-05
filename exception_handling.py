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
           
