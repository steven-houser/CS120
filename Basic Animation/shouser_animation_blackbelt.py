# Steven Houser
# Basic Animation Lab - Blackbelt Extension
# 10/24/25

# Initialize
import pygame

def main():
    pygame.init()
    
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Animation - Blackbelt")
    
    # Entities
    # load and set up background image
    try:
        background = pygame.image.load("background.png")
        background = background.convert()
        background = pygame.transform.scale(background, (640, 480))
    except:
        print("Error loading background.png")
        pygame.quit()
        return
    
    # load and set up main image
    try:
        image = pygame.image.load("image.png")
        image = image.convert_alpha()
        image = pygame.transform.scale(image, (100, 100))
    except:
        print("Error loading image.png")
        pygame.quit()
        return
    
    # get image dimensions for collision detection
    image_rect = image.get_rect()
    image_width = image_rect.width
    image_height = image_rect.height
    
    # Set up position variables
    image_x = 0
    image_y = 0
    
    # Set up movement variables
    dx = 8
    dy = 8
    
    # Action
    
        # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        # Loop
    while keepGoing:
    
        # Timer
        clock.tick(30)
    
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        # Update position
        image_x += dx
        image_y += dy
        
        # Check boundaries and bounce
        # Horizontal boundaries
        if image_x <= 0:
            image_x = 0
            dx = -dx
        if image_x + image_width >= screen.get_width():
            image_x = screen.get_width() - image_width
            dx = -dx
            
        # Vertical boundaries
        if image_y <= 0:
            image_y = 0
            dy = -dy
        if image_y + image_height >= screen.get_height():
            image_y = screen.get_height() - image_height
            dy = -dy
    
        # Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(image, (image_x, image_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
