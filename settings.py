class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置。"""
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 0)

        # 飞船设置
        self.ship_limit = 3
        
        #子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10
        # fleet_driection 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings() 

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变的设置。"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

    def increase_speed(self):
        """提高速度设置。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
