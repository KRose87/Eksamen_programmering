import sys
import pygame


class GameControls:

    def __init__(self, settings):
        self.settings = settings

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_s:
                    self.settings.start_game = not self.settings.start_game








