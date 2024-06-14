import pygame

class Bullet:
    def __init__(self, x, y, fired_by_player):
        self.image = pygame.image.load("images/bullet.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.fired_by_player = fired_by_player
        self.speed = -10 if fired_by_player else 10  # Move up if fired by player, down if fired by enemy


    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
