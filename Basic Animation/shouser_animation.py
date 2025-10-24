# Steven Houser
# Basic Animation Lab
# 10/24/25

# Initialize
import pygame

def main():
    pygame.init()
    
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Animation")
    
    # Entities
    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    # load and set up main image
    try:
        image = pygame.image.load("image.png")
        image = image.convert_alpha()
        image = pygame.transform.scale(image, (100, 100))
    except:
        print("Error loading image.png")
        pygame.quit()
        return
    
    # Set up position variables
    image_x = 0
    image_y = 0
    
    # Set up movement variables
    dx = 5
    dy = 3
    
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
        
        # Check boundaries (wrapping)
        if image_x > screen.get_width():
            image_x = 0
        if image_x < 0:
            image_x = screen.get_width()
        if image_y > screen.get_height():
            image_y = 0
        if image_y < 0:
            image_y = screen.get_height()
    
        # Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(image, (image_x, image_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()