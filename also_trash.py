"""
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
        
       