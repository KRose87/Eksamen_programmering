import pygame


class Ship:

    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.ship_img = pygame.image.load("img/ship.png")
        self.rect = self.ship_img.get_rect()

    def ship_collision(self, other):
        retValue = 0
        if self.rect.colliderect(other):
            retValue = 1
        return retValue

    def move_ship(self, movement):
        self.rect.center = movement

    def blitme(self):
        self.screen.blit(self.ship_img, self.rect)

