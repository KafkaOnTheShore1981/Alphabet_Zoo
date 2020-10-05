import sys
import pygame
from letter import Letter


def letter_generator(stats, az_settings, screen, letters):
    if stats.lives_left > 0:
        new_letter = Letter(az_settings, screen)
        letters.add(new_letter)
    else:
        letters.empty()
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_events(az_settings, letters, stats, sb, play_button, screen):
    screen_rect = screen.get_rect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(az_settings, stats, play_button, mouse_x, mouse_y, sb)

        elif event.type == pygame.KEYDOWN:
            for ltr in letters:
                if ltr.ascii == event.key and ltr.rect.bottom < screen_rect.bottom:
                    s1 = pygame.mixer.Sound("hit.wav")
                    s1.play()
                    stats.score += az_settings.letter_points
                    sb.prep_score()
                    check_high_score(stats, sb)
                    letters.remove(ltr)
                elif ltr.ascii != event.key and ltr.rect.bottom < screen_rect.bottom and stats.score > 0:
                    s2 = pygame.mixer.Sound("wrong_hit.wav")
                    s2.play()
                    stats.score -= az_settings.letter_points
                    sb.prep_score()


def check_play_button(az_settings, stats, play_button, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        sb.prep_score()
        az_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.game_active = True
        pygame.mixer.music.load("bg_music.mp3")
        pygame.mixer.music.play(-1)


def letter_fallen(stats):
    if stats.lives_left > 0:
        stats.lives_left -= 1


def check_letter_bottom(screen, letters, stats):
    screen_rect = screen.get_rect()
    for ltr in letters.sprites():
        if ltr.rect.bottom > screen_rect.bottom:
            s3 = pygame.mixer.Sound("oops.wav")
            s3.play()
            ltr.rect.bottom = screen_rect.bottom
            letter_fallen(stats)


def update_screen(az_settings, stats, screen, letters, sb, play_button):
    check_letter_bottom(screen, letters, stats)
    letters.draw(screen)
    letters.update()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    az_settings.increase_speed()
    pygame.display.flip()


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        with open('high_score.txt', 'w') as file_object:
            file_object.write(str(stats.high_score))
        sb.prep_high_score()
