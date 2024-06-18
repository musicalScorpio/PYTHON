import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image =pygame.image.load('images/rocket_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left =False
        self.moving_up = False
        self.moving_down = False
        self.settings = ai_game.settings
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed
        #up or down
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.x)
        #Put the ship at the bottom
        self.y = float(self.settings.screen_height - self.rect.size[1])