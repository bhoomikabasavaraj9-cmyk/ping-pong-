# ping-pong/main.py
import pygame
from game.game_engine import GameEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Ping Pong")

    clock = pygame.time.Clock()
    game = GameEngine(800,600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.handle_input()
        game.update()
        game.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
