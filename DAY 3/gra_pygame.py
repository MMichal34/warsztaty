from gra import kolko_krzyzyk
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 128, 255)

# Set up font
font = pygame.font.Font("Grand9K Pixel.ttf", 50)
game_over_font = pygame.font.Font("Grand9K Pixel.ttf", 45)
small_font = pygame.font.Font("Grand9K Pixel.ttf", 25)

# Create an instance of the Tic Tac Toe game
game = kolko_krzyzyk()

# Button properties
button_width, button_height = 200, 50
button_x = width // 2 - button_width // 2
button_y = height - 100

# Set up game state
game_over = False

# Function to reset the game
def reset_game():
    global game, game_over
    game = kolko_krzyzyk()
    game_over = False

# Set up game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            if game.plansza[row][col] == ' ':
                game.ruch((row, col))
                if game.wygranko() or game.remis():
                    game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_x < event.pos[0] < button_x + button_width and button_y < event.pos[1] < button_y + button_height:
                reset_game()

    screen.fill(WHITE)

    # Draw the grid
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 100), (width, i * 100), 2)
        pygame.draw.line(screen, BLACK, (i * 100, 0), (i * 100, height), 2)

    # Draw X and O
    for i in range(3):
        for j in range(3):
            if game.plansza[i][j] == 'x':
                text = font.render('X', True, BLACK)
                screen.blit(text, (j * 100 + 35, i * 100 + 10))
            elif game.plansza[i][j] == 'o':
                text = font.render('O', True, BLACK)
                screen.blit(text, (j * 100 + 35, i * 100 + 10))

    # Draw game over text and play again button
    if game_over:
        screen.fill(WHITE)

        game_over_text = game_over_font.render("Game Over", True, PURPLE)
        screen.blit(game_over_text, (width // 2 - 130, height - 280))

        if game.wygranko():
            winner_info = game_over_font.render(f"{game.gracz.upper()} won!", True, PURPLE)
            screen.blit(winner_info, (width // 2 - 75, height - 200))
        
        if game.remis():
            draw_info = game_over_font.render(f"Draw!!", True, PURPLE)
            screen.blit(draw_info, (width // 2 - 60, height - 200))

        play_again_text = small_font.render("Play Again", True, BLACK)
        pygame.draw.rect(screen, PURPLE, (button_x, button_y, button_width, button_height))
        screen.blit(play_again_text, (width // 2 - 70, button_y))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
