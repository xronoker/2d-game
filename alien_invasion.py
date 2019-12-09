import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_function as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализируем pygame, settings и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Где ведется статистика игры.
    highscore_file = 'data\highscore.txt'

    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings, highscore_file)
    sb = Scoreboard(ai_settings, screen, stats)

    # создание корабля, создание группы для хранения пуль
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Создание кнопки PLay внизу.
    play_button = Button(ai_settings, screen, "Play")

    # Запуск основного цикла игры
    while True:
        gf.check_events(highscore_file, ai_settings, screen, stats, sb,
            play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                    bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                    bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                play_button)

run_game()

