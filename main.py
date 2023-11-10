import pygame

# Initialize pygame
pygame.init()

# Set the window size
width, height = 800, 600

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Neon Purple Bordered Text Example")

# Define the font
titlefont = pygame.font.SysFont("Quicksand", 100)

# Function to draw bordered text
def draw_bordered_text(text, font, text_color, border_color, x, y, border_size):
    # Render the main text
    text_surface = font.render(text, True, text_color)
    
    # Draw the text with a border
    for i in range(-border_size, border_size + 1):
        for j in range(-border_size, border_size + 1):
            if i != 0 or j != 0:
                screen.blit(font.render(text, True, border_color), (x + i, y + j))
    
    # Blit the main text on top
    screen.blit(text_surface, (x, y))

# Draw the text with neon purple border
draw_bordered_text("Welcome", titlefont, (200, 200, 200), (148, 0, 211), 470, 40, 2)
draw_bordered_text("To", titlefont, (200, 200, 200), (148, 0, 211), 560, 140, 2)
draw_bordered_text("Sudoku", titlefont, (200, 200, 200), (148, 0, 211), 380, 240, 2)
draw_bordered_text("Game", titlefont, (200, 200, 200), (148, 0, 211), 660, 240, 2)

# Update the display
pygame.display.flip()

# Main loop and event handling
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
