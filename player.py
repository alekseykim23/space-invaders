import pygame
from bullet import Bullet

class Player:
    def __init__(self, settings):
        self.settings = settings
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize image
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 480)
        self.speed = 5
        self.lives = 3
        self.respawn_delay = 2000  # 2 seconds delay before respawning
        self.last_hit_time = None
        self.alive = True

    def update(self):
        if self.alive:
            keys = pygame.key.get_pressed()
            if self.rect.right > self.settings.screen_width + 40:
                self.rect.right = 0
                self.rect.left = 0
            if self.rect.left < -40:
                self.rect.left = self.settings.screen_width
                self.rect.right = self.settings.screen_width
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
        else:
            # Check if respawn delay has passed
            if pygame.time.get_ticks() - self.last_hit_time > self.respawn_delay:
                self.alive = True
                self.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 30)  # Respawn at starting position

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)

    def shoot(self):
        return Bullet(self.rect.centerx, self.rect.top, True)
    
    def hit(self):
        self.lives -= 1
        self.last_hit_time = pygame.time.get_ticks()
