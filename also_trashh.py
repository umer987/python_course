oooojkkkmnknnjjnnnbbniiihuuyppphhhubbjjbhhhjbhjjbbbh
MOOD PET - Your Digital Emotional Companion
A simple, interactive pet that responds to your actions with different moods
"""

import time
import random

class MoodPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.age = 0
        
    def get_mood(self):
        """Determine pet's mood based on stats"""
        if self.happiness > 70 and self.energy > 60:
            return "😄 HAPPY"
        elif self.hunger > 80:
            return "😫 HUNGRY"
        elif self.energy < 30:
            return "😴 SLEEPY"
        elif self.happiness < 30:
            return "😢 SAD"
        elif self.happiness > 80:
            return "🎉 EXCITED"
        else:
            return "😐 NEUTRAL"
    
    def show_status(self):
        """Display pet's current status with emojis"""
        mood = self.get_mood()
        print(f"\n{'-'*30}")
        print(f"🐾 {self.name} the Pet")
        print(f"{'-'*30}")
        print(f"Mood: {mood}")
        print(f"Hunger: {'🍖' * (self.hunger//10)} {self.hunger}%")
        print(f"Happiness: {'❤️' * (self.happiness//10)} {self.happiness}%")
        print(f"Energy: {'⚡' * (self.energy//10)} {self.energy}%")
        print(f"Age: {self.age} days")
        print(f"{'-'*30}")
    
    def feed(self):
        """Feed the pet"""
        print(f"\n🍕 You feed {self.name}...")
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 10)
        self.energy = min(100, self.energy + 5)
        print(f"{self.name}: Yum! Thanks for the food!")
    
    def play(self):
        """Play with the pet"""
        if self.energy < 20:
            print(f"\n😴 {self.name} is too tired to play!")
            return
        
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

if __name__ == "__main__":
    main()
