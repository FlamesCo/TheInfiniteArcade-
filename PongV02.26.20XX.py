import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set window size and title
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
paddle_width = 10
paddle_height = 60

# Ball properties
ball_width = 10
ball_height = 10

# Paddle speed
paddle_speed = 5

# AI
ai_speed = 3

# Score
font = pygame.font.Font(None, 36)
player_score = 0
ai_score = 0

# Winning and losing score
winning_score = 11


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((paddle_width, paddle_height))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, y):
        self.rect.y += y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.surf = pygame.Surface((ball_width, ball_height))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
            return True
        return False


def main():
    global player_score, ai_score
    clock = pygame.time.Clock()

    player = Paddle(20, screen_height // 2 - paddle_height // 2)
    ai = Paddle(screen_width - 20 - paddle_width, screen_height // 2 - paddle_height // 2)
    ball = Ball(screen_width // 2 - ball_width // 2, screen_height // 2 - ball_height // 2, 5, 5)

    playing = True
    while playing:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(-paddle_speed)
        if keys[pygame.K_DOWN]:
            player.move(paddle_speed)

        # Update AI position
        if ai.rect.centery < ball.rect.centery:
            ai.move(ai_speed)
        elif ai.rect.centery > ball.rect.centery:
            ai.move(-ai_speed)

        # Update ball position
        ball.move()
        collision = ball.move()

        # Check for paddle collision
        if ball.rect.colliderect(player.rect):
            ball.speed_x = abs(ball.speed_x)
            ball.speed_y = (ball.rect.centery - player.rect.centery) // 8
        elif ball.rect.colliderect(ai.rect):
            ball.speed_x = -abs(ball.speed_x)
            ball.speed_y = (ball.rect.centery - ai.rect.centery) // 8

        # Update scores
        if collision:
            if ball.rect.left < 0:
                ai_score += 1
            elif ball.rect.right > screen_width:
                player_score += 1
            time.sleep(1)
            ball.rect.x = screen_width // 2 - ball_width // 2
            ball.rect.y = screen_height // 2 - ball_height // 2

        # Draw
        screen.blit(player.surf, player.rect)
        screen.blit(ai.surf, ai.rect)
        screen.blit(ball.surf, ball.rect)
        screen.blit(font.render(f'Player: {player_score}', True, WHITE), (30, 10))
        screen.blit(font.render(f'AI: {ai_score}', True, WHITE), (screen_width - 130, 10))

        # Check for winning conditions
        if player_score == winning_score or ai_score == winning_score:
            winner = 'Player' if player_score > ai_score else 'AI'
            playing = False

        pygame.display.flip()
        clock.tick(60)

    # Display the winner for 3 seconds
    screen.blit(font.render(f'{winner} wins!', True, WHITE), (screen_width // 2 - 80, screen_height // 2 - 20))
    pygame.display.flip()
    time.sleep(3)

    # Quit the game
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()