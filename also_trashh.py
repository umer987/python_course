
        if random.random() < 0.1:  # 10% chance of special event
            events = [
                (self.happiness + 10, f"✨ {self.name} found a sparkly toy!"),
                (self.hunger - 5, f"🌧️ {self.name} found some food!"),
                (self.energy + 10, f"🌈 {self.name} feels energized!"),
                (self.happiness - 5, f"☔ {self.name} got wet in the rain...")
            ]
            effect, message = random.choice(events)
            
            if effect > 0:
                self.happiness = min(100, self.happiness + effect)
            else:
                self.happiness = max(0, self.happiness + effect)
                
            print(f"\n{message}")

def main():
    print("=" * 40)
    print("🌈 WELCOME TO MOOD PET! 🌈")
    print("Your digital emotional companion")
    print("=" * 40)
    
    # Name your pet
    name = input("\nWhat would you like to name your pet? ").strip()
    if not name:
        name = "Buddy"
        print(f"Okay, we'll call your pet {name}!")
    
    pet = MoodPet(name)
    
    # Game loop
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


