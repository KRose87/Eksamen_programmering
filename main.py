import pygame

from settings import Settings
from game_utilities import GameUtils
from game_stats import GameStats
from game_control import GameControls
from daleks import Daleks
from ship import Ship


# Init pygame
pygame.init()

# Settings
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
screen_rect = screen.get_rect()
g_utils = GameUtils(settings, screen)
g_controls = GameControls(settings)
g_stats = GameStats(settings, screen)

# Clock
clock = pygame.time.Clock()

# Player
ship = Ship(settings, screen)

# Enemy
daleks = Daleks(settings, screen)

# Variables
dalek_counter = 1
frame_counter = 0

# Caption and logo
pygame.display.set_caption("Dalek Invasion")
img = pygame.image.load('img/logo.png')
img = pygame.transform.scale(img, (10, 10))
pygame.display.set_icon(img)


"""Main loop"""
while True:
    pygame.mouse.set_visible(False)
    frame_counter += 1

    # Check events
    g_controls.check_events()

    if frame_counter % settings.frequency == 0:
        dalek_counter += 1
        if dalek_counter == len(daleks.list_of_daleks):
            dalek_counter = 1
            daleks = Daleks(settings, screen)

    if settings.start_game:
        ship.move_ship(pygame.mouse.get_pos())
        g_utils.blit_bg()

        # Moving objects
        for dalek in daleks.list_of_daleks[:dalek_counter]:
            g_utils.blit_asteroid()

            if ship.ship_collision(dalek.dalek_rect):
                g_stats.score += 1
                dalek.killme()

            # Hvorfor laver den game over før dalek rammer bunden hvis man griber de første?
            if dalek.dalek_rect.bottom >= screen_rect.bottom:
                g_utils.game_over()
                break

            else:
                dalek.dalek_rect.centery += dalek.speed
                screen.blit(dalek.dalek_img, dalek.dalek_rect)

        ship.blitme()

    else:
        # Draw start screen
        screen.fill(settings.black)
        g_utils.blit_title()
        g_utils.blit_btn()
        pygame.mouse.set_visible(True)

    g_stats.blit_text()
    pygame.display.update()
    clock.tick(settings.framerate)
