import pygame


def draw_board(screen, colors, square_size):
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            posX, posY = col * square_size, row * square_size
            pygame.draw.rect(screen, color, (posX, posY, square_size, square_size))


def main():
    pygame.init()

    square_size = 80
    screen_size = 8 * square_size
    screen = pygame.display.set_mode((screen_size, screen_size))

    colors = [(240, 240, 240), (128, 128, 128)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(screen, colors, square_size)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
