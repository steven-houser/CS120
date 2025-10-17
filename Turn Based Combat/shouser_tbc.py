# Steven Houser
# Turn Based Combat Module
# 10/17/25

import random

class Character:
    # Represents a character in turn-based combat with stats and combat abilities
    
    def __init__(self, name="", hitPoints=0, hitChance=0, maxDamage=0, armor=0):
        # Initialize a character with combat stats
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    
    def testInt(self, value, min=0, max=100, default=0):
        # Checks if value is an int between min and max
        # Returns value if legal, otherwise returns default
        # Prints error messages for invalid inputs
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an integer")
        return out
    
    @property
    def name(self):
        # Get character name
        return self.__name
    
    @name.setter
    def name(self, value):
        # Set character name
        self.__name = value
    
    @property
    def hitPoints(self):
        # Get character hit points
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        # Set character hit points (can be negative or zero)
        self.__hitPoints = self.testInt(value, min=-999999, max=999999, default=0)
    
    @property
    def hitChance(self):
        # Get character hit chance percentage
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        # Set character hit chance (0-100)
        self.__hitChance = self.testInt(value, min=0, max=100, default=0)
    
    @property
    def maxDamage(self):
        # Get character maximum damage
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        # Set character maximum damage (minimum 0)
        self.__maxDamage = self.testInt(value, min=0, max=999999, default=0)
    
    @property
    def armor(self):
        # Get character armor value
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        # Set character armor (minimum 0)
        self.__armor = self.testInt(value, min=0, max=999999, default=0)
    
    def printStats(self):
        # Print character statistics
        print(self.__name)
        print(f"Hit Points: {self.__hitPoints}")
        print(f"Hit Chance: {self.__hitChance}%")
        print(f"Max Damage: {self.__maxDamage}")
        print(f"Armor: {self.__armor}")
        print()
    
    def hit(self, opponent):
        # Attack an opponent character
        print(f"{self.__name} attacks!")
        
        # Generate hit roll
        hitRoll = random.randint(1, 100)
        
        # Check if hit succeeds
        if hitRoll <= self.__hitChance:
            # Generate damage roll if maxDamage > 0
            if self.__maxDamage > 0:
                damageRoll = random.randint(1, self.__maxDamage)
            else:
                damageRoll = 0
            
            # Calculate actual damage after armor
            actualDamage = damageRoll - opponent.armor
            if actualDamage < 0:
                actualDamage = 0
            
            # Apply damage
            opponent.hitPoints -= actualDamage
            print(f"Hit for {actualDamage} damage!")
            
            # Check if opponent is defeated
            if opponent.hitPoints <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print("Miss!")

def fight(char1, char2):
    # Simulate combat between two characters
    keepGoing = True
    
    while keepGoing:
        # Character 1 attacks
        char1.hit(char2)
        print(f"{char2.name} HP: {char2.hitPoints}")
        print()
        
        # Check if character 2 is defeated
        if char2.hitPoints <= 0:
            print(f"{char1.name} is victorious!")
            keepGoing = False
        
        # Character 2 attacks if still alive
        if keepGoing:
            char2.hit(char1)
            print(f"{char1.name} HP: {char1.hitPoints}")
            print()
            
            # Check if character 1 is defeated
            if char1.hitPoints <= 0:
                print(f"{char2.name} is victorious!")
                keepGoing = False
        
        # Pause before next round
        if keepGoing:
            input("Press enter for next round: ")
    
    print("Combat ended")

def main():
    # Test the Character class and fight function
    # Create test character with default values
    testChar = Character()
    testChar.name = "Test Hero"
    testChar.hitPoints = 15
    testChar.hitChance = 60
    testChar.maxDamage = 6
    testChar.armor = 1
    
    # Create second character with parameters
    enemy = Character("Test Monster", 20, 40, 8, 2)
    
    # Print stats
    testChar.printStats()
    enemy.printStats()
    
    # Fight
    fight(testChar, enemy)

if __name__ == "__main__":
    main()

