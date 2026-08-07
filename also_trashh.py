
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


