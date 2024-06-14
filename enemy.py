import pygame
from bullet import Bullet

class Enemy:
    def __init__(self, settings):
        self.settings = settings
        self.image = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 50)  # Example starting position
        self.speed = 3
        self.last_shot = pygame.time.get_ticks()  # Time when the last shot was fired

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.settings.screen_width or self.rect.left < 0:
            self.speed = -self.speed
            self.rect.y += 10  # Move down when hitting the screen edge

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        # Check if enough time has passed since the last shot
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.settings.enemy_shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.bottom, False)  # Create bullet at enemy's position
            return bullet
        return None

    def explode(self):
        pass
