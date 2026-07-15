
  
        """Ask if user wants to play again"""
        while True:
            choice = input("\nPlay again? (yes/no): ").lower().strip()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            print("⚠️  Please enter 'yes' or 'no'.")

    def run(self):
        """Main game loop"""
        playing = True
        
        while playing:
            self.score = 0
            self.shuffle_questions()
            self.display_welcome()
            
            # Ask each question
            for i, question in enumerate(self.questions, 1):
                self.ask_question(question, i)
                time.sleep(0.5)
            
            # Show results
            self.display_results()
            
            # Ask to play again
            playing = self.play_again()
        
        print("\n👋 Thanks for playing! Goodbye!")

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()
        
        print(f"\n🎾 You play with {self.name}...")
        self.happiness = min(100, self.happiness + 25)
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 15)
        print(f"{self.name}: That was fun! Let's play again!")
    
    def sleep(self):
        """Put the pet to sleep"""
        print(f"\n💤 {self.name} goes to sleep...")
        time.sleep(2)
        self.energy = min(100, self.energy + 40)
        self.happiness = max(0, self.happiness - 5)
        print(f"{self.name}: *Yawn* That was a good nap!")
    
    def give_gift(self):
        """Give a random gift to the pet"""
        gifts = ["🎈 balloon", "🧸 teddy bear", "🎮 video game", 
                "🦴 bone", "🐟 fish", "🏀 ball"]
        gift = random.choice(gifts)
        print(f"\n🎁 You give {self.name} a {gift}!")
        
        if random.random() > 0.3:  # 70% chance they like it
            self.happiness = min(100, self.happiness + 20)
            print(f"{self.name}: I love it! Thank you!")
        else:
            self.happiness = max(0, self.happiness - 5)
            print(f"{self.name}: Hmm... not really my thing...")
    
    def time_passes(self):
        """Simulate time passing"""
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 3)
        self.energy = max(0, self.energy - 2)
        self.age += 1
        
        # Random events
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


