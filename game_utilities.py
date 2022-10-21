import pygame


class GameUtils:

    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.bg = pygame.image.load("img/background.png")
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))
        self.asteroid = pygame.image.load("img/asteroid.png")
        self.asteroid2 = pygame.image.load("img/asteroid2.png")
        self.asteroid3 = pygame.image.load("img/asteroid3.png")

        # Start screen settings
        self.title = pygame.image.load("img/title.png").convert()
        self.start_btn = pygame.image.load("img/start.png").convert()
        self.quit_btn = pygame.image.load("img/quit.png").convert()
        self.title.set_colorkey((0, 0, 0))
        self.start_btn.set_colorkey((0, 0, 0))
        self.quit_btn.set_colorkey((0, 0, 0))

        # Game over settings
        self.go_text = pygame.image.load("img/ggame_over.png").convert()
        self.go_text.set_colorkey((0, 0, 0))
        self.myfont = pygame.font.SysFont('times new roman', self.settings.font_size)

    def blit_bg(self):
        self.screen.blit(self.bg, (0, 0))

    def blit_asteroid(self):
        self.screen.blit(self.asteroid, (100, 100))
        self.screen.blit(self.asteroid2, (500, 350))
        self.screen.blit(self.asteroid3, (700, 500))

    def blit_title(self):
        self.screen.blit(self.title, (self.settings.screen_width/4, self.settings.screen_height/6))

    def blit_btn(self):
        self.screen.blit(self.start_btn, (self.settings.screen_width/6, self.settings.screen_height/2))
        self.screen.blit(self.quit_btn, (self.settings.screen_width/2, self.settings.screen_height/2))

    def game_over(self):
        self.screen.fill(self.settings.black)
        self.screen.blit(self.go_text, (self.settings.screen_width/4, self.settings.screen_height/3))
        text = self.myfont.render(f"Press 'S' for menu", self.settings.black, self.settings.white)
        text_rect = text.get_rect(midbottom=(self.settings.screen_width/2, self.settings.screen_height/7))
        self.screen.blit(text, text_rect)
