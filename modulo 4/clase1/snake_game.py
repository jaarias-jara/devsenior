try:
    import pygame
except ImportError:
    import sys
    print("Error: Pygame no está instalado")
    sys.exit()
import random
import time

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
screen_width = 600
screen_height = 400
cell_size = 20

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def draw_snake(snake_list):
    """Draw the snake on the screen"""
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], cell_size, cell_size])

def message(msg, color):
    """Display a message on the screen"""
    text = font.render(msg, True, color)
    screen.blit(text, [screen_width / 6, screen_height / 3])

def game_loop():
    game_over = False
    game_exit = False
    
    # Starting position of the snake (using integer values to avoid floating point issues)
    x = int(screen_width / 2)
    y = int(screen_height / 2)
    
    # Align to grid
    x = x - (x % cell_size)
    y = y - (y % cell_size)
    
    # Initial movement direction
    x_change = 0
    y_change = 0
    
    # Snake body (starts with one block)
    snake_list = []
    snake_length = 1
    
    # Initial food position
    food_x = round(random.randrange(0, screen_width - cell_size) / cell_size) * cell_size
    food_y = round(random.randrange(0, screen_height - cell_size) / cell_size) * cell_size
    
    # Game loop
    while not game_exit:
        
        # Game over loop
        while game_over:
            screen.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        # Restart the game without recursive call
                        return game_loop()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:  # Prevent 180 degree turns
                    x_change = -cell_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = cell_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -cell_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = cell_size
                    x_change = 0
                    
        # Check if snake hits the boundaries
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_over = True
            
        # Update snake position
        x += x_change
        y += y_change
        
        # Fill the screen with black
        screen.fill(BLACK)
        
        # Draw the food
        pygame.draw.rect(screen, RED, [food_x, food_y, cell_size, cell_size])
        
        # Update snake list with new head position
        snake_head = [x, y]  # Use a single list instead of appending
        snake_list.append(snake_head)
        
        # Remove extra pieces of the snake if it's longer than it should be
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        # Check if snake hits itself - fixed comparison
        for block in snake_list[:-1]:
            if block[0] == snake_head[0] and block[1] == snake_head[1]:
                game_over = True
                
        # Draw the snake
        draw_snake(snake_list)
        
        # Display score
        score = font.render(f"Score: {snake_length - 1}", True, WHITE)
        screen.blit(score, [0, 0])
        
        # Update the display
        pygame.display.update()
        
        # Check if snake eats food
        if x == food_x and y == food_y:
            # Generate new food
            food_x = round(random.randrange(0, screen_width - cell_size) / cell_size) * cell_size
            food_y = round(random.randrange(0, screen_height - cell_size) / cell_size) * cell_size
            # Increase snake length
            snake_length += 1
            
        # Control game speed
        clock.tick(10)
    
    # Quit pygame
    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":  # Add this guard to prevent code from running when imported
    game_loop() 