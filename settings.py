class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置。"""
        self.screen_width = 800
        self.screen_height = 600
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.0
        #子弹的设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3

        