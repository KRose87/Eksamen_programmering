
class Settings:

    def __init__(self):
        self.start_game = False

        # Screen settings:
        self.screen_width = 1000
        self.screen_height = 800
        self.delta = self.screen_width / 10
        self.framerate = 60

        # Score text and colour settings:
        self.font_size = 32
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # Dalek settings:
        self.frequency = 30
        self.num_of_daleks = 20
