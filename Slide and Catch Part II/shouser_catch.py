# Steven Houser
# Slide and Catch Game - Part II
# 11/07/25

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


class LblScore(simpleGE.Label):
    # Score label widget
    
    def __init__(self):
        # Initialize score label
        super().__init__()
        
        # Set label properties
        self.text = "Score: 0"
        self.center = (100, 30)
        self.bgColor = (0, 0, 0)
        self.fgColor = (255, 255, 255)
        self.clearBack = True


class LblTime(simpleGE.Label):
    # Time label widget
    
    def __init__(self):
        # Initialize time label
        super().__init__()
        
        # Set label properties
        self.text = "Time Left: 10"
        self.center = (500, 30)
        self.bgColor = (0, 0, 0)
        self.fgColor = (255, 255, 255)
        self.clearBack = True


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
        
        # Set up game timer
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        
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
        
        # Create label widgets
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        # Add all sprites to the scene
        self.sprites = [self.cauldron,
                        self.candies,
                        self.lblScore,
                        self.lblTime]
    
    def process(self):
        # Check for collisions between cauldron and candies
        for candy in self.candies:
            if self.cauldron.collidesWith(candy):
                # Play sound effect if available
                if self.sndCatch:
                    self.sndCatch.play()
                
                # Reset candy position and increase score by candy's points value
                candy.reset()
                self.score += candy.points
                self.lblScore.text = f"Score: {self.score}"
        
        # Update time remaining display
        timeLeft = self.timer.getTimeLeft()
        self.lblTime.text = f"Time Left: {timeLeft:.2f}"
        
        # Check if time has expired
        if timeLeft < 0:
            print(f"Final Score: {self.score}")
            self.stop()


class Instructions(simpleGE.Scene):
    # Instructions scene
    
    def __init__(self, score):
        # Initialize instructions scene
        super().__init__()
        
        # Load background image with error handling
        try:
            self.setImage("background.png")
        except FileNotFoundError:
            print("Error loading background.png")
            self.background.fill((0, 0, 0))
        
        # Set default response and save previous score
        self.response = "Play"
        self.prevScore = score
        
        # Create instructions multi-label widget
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Slide and Catch Game",
            "",
            "Use LEFT and RIGHT arrow keys to move the cauldron",
            "Catch as many candies as you can",
            "in only ten seconds!",
            "",
            "Good Luck!"]
        self.instructions.center = (320, 240)
        self.instructions.size = (600, 250)
        self.instructions.bgColor = (0, 0, 0)
        self.instructions.fgColor = (255, 255, 255)
        
        # Create score label to display previous score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        self.lblScore.size = (300, 30)
        self.lblScore.bgColor = (0, 0, 0)
        self.lblScore.fgColor = (255, 255, 255)
        self.lblScore.clearBack = False
        
        # Create Play button
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        # Create Quit button
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        # Add all widgets to the scene
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnPlay,
                        self.btnQuit]
    
    def process(self):
        # Check if Quit button was clicked
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
        # Check if Play button was clicked
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()


def main():
    # Main game loop
    keepGoing = True
    score = 0
    
    # Loop until player chooses to quit
    while keepGoing:
        # Show instructions screen
        instructions = Instructions(score)
        instructions.start()
        
        # Check player's response
        if instructions.response == "Play":
            # Start game and save score
            game = Game()
            game.start()
            score = game.score
        else:
            # Player chose to quit
            keepGoing = False


if __name__ == "__main__":
    main()

