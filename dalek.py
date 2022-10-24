import pygame


class Dalek:
    def __init__(self, screen, settings, xpos, ypos):
        self.screen = screen
        self.settings = settings
        self.xpos = xpos
        self.ypos = ypos
        self.dalek_img = pygame.image.load("img/dalek.png")
        self.dalek_rect = self.dalek_img.get_rect(center=(self.xpos, self.ypos))

    def blitme(self):
        self.screen.blit(self.dalek_img, self.dalek_rect)


