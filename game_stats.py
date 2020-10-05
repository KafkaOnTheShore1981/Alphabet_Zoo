class GameStats:
    def __init__(self, az_settings):
        self.az_settings = az_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.lives_left = self.az_settings.lives_limit
        self.score = 0
