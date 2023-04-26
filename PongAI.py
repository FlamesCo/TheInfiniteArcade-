import pygame

# Initialize Pygame
pygame.init()

# Set up the display window (width, height)
screen = pygame.display.set_mode((600, 400))

# Define colors for easier reference later on
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the positions of the paddles
player1_paddle_x = 20
player1_paddle_y = 200
player2_paddle_x = 580
player2_paddle_y = 200

# Define the position of the ball
ball_x = 300
ball_y = 200

# Define the speed of the ball
ball_x_speed = 5
ball_y_speed = 5

# Define the score
player1_score = 0
player2_score = 0

# Set the window title
pygame.display.set_caption("Pong AI 0.A BETA WIP")

# Start the main loop
while True:

    # Check for events
    for event in pygame.event.get():
        # Check for the QUIT event
        if event.type == pygame.QUIT:
            break

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_paddle_y -= 5
            elif event.key == pygame.K_DOWN:
                player1_paddle_y += 5

    # Update the position of the ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Check if the ball hit the top or bottom of the screen
    if ball_y < 0 or ball_y > 400:
        ball_y_speed *= -1

    # Check if the ball hit the paddles
    if ball_x < player1_paddle_x + 10 and ball_y > player1_paddle_y and ball_y < player1_paddle_y + 75:
        ball_x_speed *= -1
    elif ball_x > player2_paddle_x - 10 and ball_y > player2_paddle_y and ball_y < player2_paddle_y + 75:
        ball_x_speed *= -1

    # Check if the ball went out of bounds
    if ball_x < 0 or ball_x > 600:
        if ball_x < 0:
            player2_score += 1
        else:
            player1_score += 1
        ball_x = 300
        ball_y = 200

    # Draw the background
    screen.fill(BLACK)

    # Draw the paddles
    pygame.draw.rect(screen, WHITE, (player1_paddle_x, player1_paddle_y, 10, 75))
    pygame.draw.rect(screen, WHITE, (player2_paddle_x, player2_paddle_y, 10, 75))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # Draw the score
    text = "Player 1: {}   Player 2: {}".format(player1_score, player2_score)
    pygame.font.init()
    myfont = pygame.font.SysFont("Arial", 20)
    textSurface = myfont.render(text, True, WHITE)
    screen.blit(textSurface, (200, 10))

    # Flip the display
    pygame.display.flip()

    # Limit the frames per second to 30
    pygame.time.delay(30)

# Close the window
pygame.quit()
