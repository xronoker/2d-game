import os


class GameStats(object):
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings, highscore_file):
        """Инициализируем статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд никогда не должен сбрасываться.
        self.highscore_file = highscore_file
        if os.path.exists(self.highscore_file):
            f_obj = open(highscore_file, 'r')
            content = f_obj.read()
            if len(content) > 0:
                self.high_score = int(content.rstrip())
            else:
                self.high_score = 0
        else:
            self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1