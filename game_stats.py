import pygame


class GameStats:

    def __init__(self, settings, screen):
        self.score = 0
        self.screen = screen
        self.settings = settings
        self.myfont = pygame.font.SysFont('times new roman', self.settings.font_size)

    def blit_text(self):
        text = self.myfont.render(f"Score: {self.score}", self.settings.black, self.settings.white)
        self.screen.blit(text, text.get_rect())



