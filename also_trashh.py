
    while True:
        pet.show_status()
        
        # Check if pet is too unhappy
        if pet.happiness <= 0:
            print(f"\n💔 {pet.name} has run away... Game Over!")
            break
        
        print("\nWhat would you like to do?")
        print("1. 🍕 Feed")
        print("2. 🎾 Play")
        print("3. 💤 Sleep")
        print("4. 🎁 Give gift")
        print("5. ⏰ Let time pass")
        print("6. 👋 Quit")
        
        choice = input("\nYour choice (1-6): ").strip()
        
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.give_gift()
        elif choice == '5':
            print("\n⏰ Time passes...")
            pet.time_passes()
        elif choice == '6':
            print(f"\n👋 Goodbye! Thanks for playing with {pet.name}!")
            print(f"Final stats: {pet.get_mood()} mood, {pet.age} days old")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")
        
        time.sleep(1)  # Small pause for better experience


