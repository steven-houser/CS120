# Steven Houser
# Slide and Catch Game - Part I
# 10/31/25

import pygame, random, simpleGE


class Cauldron(simpleGE.Sprite):
    # Cauldron sprite controlled by player
    
    def __init__(self, scene):
        # Initialize cauldron sprite
        super().__init__(scene)
        
        # Load cauldron image with error handling
        try:
            self.setImage("cauldron.png")
        except FileNotFoundError:
            print("Error loading cauldron.png")
            self.setImage(simpleGE.makeColorRect("red", 50, 50))
        
        # Set sprite properties
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        # Check for left arrow key
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        
        # Check for right arrow key
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class Candy(simpleGE.Sprite):
    # Falling candy sprite worth 1 point
    
    def __init__(self, scene):
        # Initialize candy sprite
        super().__init__(scene)
        
        # Load candy image with error handling
        try:
            self.setImage("candy1.png")
        except FileNotFoundError:
            print("Error loading candy1.png")
            self.setImage(simpleGE.makeColorRect("yellow", 25, 30))
        
        # Set sprite size, points value, and initial position
        self.setSize(25, 30)
        self.points = 1
        self.reset()
    
    def reset(self):
        # Reset candy to top with random position and speed
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        self.dx = 0
    
    def checkBounds(self):
        # Check if candy fell off bottom of screen
        if self.bottom > self.screenHeight:
            self.reset()


class Candy2(simpleGE.Sprite):
    # Falling candy sprite worth 2 points
    
    def __init__(self, scene):
        # Initialize candy2 sprite
        super().__init__(scene)
        
        # Load candy2 image with error handling
        try:
            self.setImage("candy2.png")
        except FileNotFoundError:
            print("Error loading candy2.png")
            self.setImage(simpleGE.makeColorRect("orange", 25, 30))
        
        # Set sprite size, points value, and initial position
        self.setSize(25, 30)
        self.points = 2
        self.reset()
    
    def reset(self):
        # Reset candy to top with random position and speed
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        self.dx = 0
    
    def checkBounds(self):
        # Check if candy fell off bottom of screen
        if self.bottom > self.screenHeight:
            self.reset()


class Game(simpleGE.Scene):
    # Main game scene
    
    def __init__(self):
        # Initialize game scene
        super().__init__()
        
        # Load background image with error handling
        try:
            self.setImage("background.png")
        except FileNotFoundError:
            print("Error loading background.png")
            self.background.fill((0, 0, 0))
        
        # Load sound effect with error handling
        try:
            self.sndCatch = simpleGE.Sound("catch.wav")
        except FileNotFoundError:
            print("Warning: could not load catch.wav")
            self.sndCatch = None
        
        # Create cauldron sprite
        self.cauldron = Cauldron(self)
        
        # Create candy sprites (1 point each)
        self.numCandies = 10
        self.candies = []
        for i in range(self.numCandies):
            self.candies.append(Candy(self))
        
        # Create candy2 sprites (2 points each)
        self.numCandies2 = 5
        for i in range(self.numCandies2):
            self.candies.append(Candy2(self))
        
        # Add all sprites to the scene
        self.sprites = [self.cauldron, self.candies]
    
    def process(self):
        # Check for collisions between cauldron and candies
        for candy in self.candies:
            if self.cauldron.collidesWith(candy):
                # Play sound effect if available
                if self.sndCatch:
                    self.sndCatch.play()
                
                # Print message to console with points
                print(f"Caught! +{candy.points} point(s)")
                
                # Reset candy position
                candy.reset()


def main():
    # Create and start game
    game = Game()
    game.start()


if __name__ == "__main__":
    main()


