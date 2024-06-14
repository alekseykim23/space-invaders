class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right, -1 represents left

        # Enemy settings
        self.enemy_shoot_delay = 1000  # Delay between enemy shots in milliseconds
