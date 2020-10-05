import pygame
import time
from pygame.locals import *
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    az_settings = Settings()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Alphabet Zoo")
    play_button = Button(screen, "Play")
    stats = GameStats(az_settings)
    sb = Scoreboard(az_settings, screen, stats)
    letters = pygame.sprite.Group()
    start = time.time()
    sleeptime = az_settings.letter_generating_factor
    pygame.mixer.init()
    bg_image1 = pygame.image.load('bg_image.jpg')

    while True:
        screen.blit(bg_image1, (0, 0))
        with open('high_score.txt') as file_object:
            stats.high_score = int(file_object.read())
        sb.prep_high_score()
        now = time.time()
        gf.check_events(az_settings, letters, stats, sb, play_button, screen)
        if stats.game_active:
            gf.update_screen(az_settings, stats, screen, letters, sb, play_button)
            if now - start > sleeptime:
                gf.letter_generator(stats, az_settings, screen, letters)
                start = now
        else:
            gf.update_screen(az_settings, stats, screen, letters, sb, play_button)
            pygame.mixer.music.stop()


run_game()
