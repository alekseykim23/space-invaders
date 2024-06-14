import pygame
from game import Game
from settings import Settings

def main():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Space Invaders")
    
    game = Game(screen, settings)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()
