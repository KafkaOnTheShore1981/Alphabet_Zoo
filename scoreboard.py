import pygame.font


class Scoreboard:
    def __init__(self, az_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.az_settings = az_settings
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score_str = 'Current Score:' + "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            (14, 111, 108))

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        high_score_str = 'Highest Score: ' + "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, (14, 111, 108))

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
