from random import randint
from dalek import Dalek


class Daleks:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.list_of_daleks = self.init_targets()

    def init_targets(self):
        daleks = []
        for number in range(self.settings.num_of_daleks):
            xpos = randint(self.settings.delta, self.settings.screen_width - self.settings.delta)
            ypos = 0
            speed = randint(1, 3)
            dalek = Dalek(self.screen, self.settings, xpos=xpos, ypos=ypos, speed=speed)
            daleks.append(dalek)
        return daleks
