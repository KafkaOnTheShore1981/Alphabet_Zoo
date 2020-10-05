class Settings:
    def __init__(self):
        self.falling_speed_increment = 0.01
        self.letter_generating_increment = 0.1
        self.lives_limit = 10
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.letter_speed_factor = 5
        self.letter_generating_factor = 3
        self.letter_points = 50

    def increase_speed(self):
        self.letter_speed_factor += self.falling_speed_increment
        self.letter_generating_factor -= self.letter_generating_increment
