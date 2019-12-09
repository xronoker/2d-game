class Settings(object):
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализируем ностройки статистики игры."""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Настройки корабля.
        self.ship_limit = 3

        # Настройки пуль.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 100, 60)
        self.bullets_allowed = 3

        # Настройки пришельца.
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.05
        # Как быстро увеличивается значение очков.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализация настроек, которые меняются на протяжении всей игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.8

        # fleet_direction = 1 обозначает движение вправо; а -1 влево.
        self.fleet_direction = 1

        # Подсчет очков.
        self.alien_points = 55

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
