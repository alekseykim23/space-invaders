import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self.settings)
        # Load explosion sound
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        # self.enemies = [Enemy(self.settings) for _ in range(1)]  # Number of times you need to hit to destroy the enemy

        self.enemies = []
        self.bullets = []

        self.score = 0
        self.lives = 3

        self.font = pygame.font.Font(None, 36)
        self.player_life_image = pygame.transform.scale(pygame.image.load("images/player.png"), (30, 30))

        self.explosion_image = pygame.transform.scale(pygame.image.load("images/explosion.png"), (70, 70))

        self.explosions = []
        self.spawn_enemies()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = self.player.shoot()
                    if bullet:
                        self.bullets.append(bullet)

    def update(self):
        self.player.update()
        for enemy in self.enemies[:]:
            enemy.update()

            # Emeny and bullet collision detection
            for bullet in self.bullets:
                if pygame.sprite.collide_rect(enemy, bullet) and bullet.fired_by_player:
                    self.bullets.remove(bullet)
                    self.score += 1
                    self.explosions.append((enemy.rect.topleft, 255))  # Add explosion with initial opacity
                    self.explosion_sound.play() 
                    self.enemies.remove(enemy)
                    break  # Exit bullet loop once enemy is destroyed
            
            # Enemy shooting
            bullet = enemy.shoot()
            if bullet:
                self.bullets.append(bullet)

        # Player and bullet collision detection
        for bullet in self.bullets[:]:
            if pygame.sprite.collide_rect(self.player, bullet) and not bullet.fired_by_player:
                self.bullets.remove(bullet)
                self.lives -= 1
                self.explosions.append((self.player.rect.topleft, 255))  # Add player explosion
                self.explosion_sound.play()  # Play explosion sound
                self.player.hit()
                if self.lives <= 0:
                    self.running = False  # End the game if no lives left
                break  # Exit loop after collision

        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        # Update explosions opacity
        for i, (pos, alpha) in enumerate(self.explosions):
            alpha -= 3  # Decrease opacity
            if alpha <= 0:
                self.explosions.pop(i)
            else:
                self.explosions[i] = (pos, alpha)

        if not self.enemies:
            self.spawn_enemies()

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Draw ground
        pygame.draw.rect(self.screen, (0, 255, 0), (0, self.settings.screen_height - 20, self.settings.screen_width, 20))

        # Draw header
        pygame.draw.rect(self.screen, (0, 128, 0), (0, 0, self.settings.screen_width, 45))
        score_text = f"Score: {self.score}"
        score_render = self.font.render(score_text, True, (255, 255, 255))
        self.screen.blit(score_render, (10, 10))

        # Draw lives
        lives_text = f"Lives:"
        lives_render = self.font.render(lives_text, True, (255, 255, 255))
        self.screen.blit(lives_render, (600, 10))
        for i in range(self.lives):
            self.screen.blit(self.player_life_image, (self.settings.screen_width - 40 - i * 40, 10))

        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)

        # Draw explosions
        for pos, alpha in self.explosions:
            explosion_surface = self.explosion_image.copy()
            explosion_surface.set_alpha(alpha)  # Set alpha value for transparency
            self.screen.blit(explosion_surface, pos)

        pygame.display.flip()

    def spawn_enemies(self):
        # Calculate the number of enemies to spawn
        num_enemies = random.randint(1, 10)  # Randomly choose between 1 and 10 enemies
        for _ in range(num_enemies):
            # Randomly generate x-coordinate within the top 2 rows
            x = random.randint(0, self.settings.screen_width - 40)  # Width of enemy image is 40
            # Randomly generate y-coordinate within the top 2 rows
            y = random.randint((self.settings.screen_height // 2 - 250), self.settings.screen_height // 2 )  # Adjusted to avoid spawning on the header

            enemy = Enemy(self.settings)
            enemy.rect.topleft = (x, y)
            self.enemies.append(enemy)
