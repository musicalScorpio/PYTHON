class Settings:
    def __init__(self,width,height,color):
        self.screen_width = width
        self.screen_height = height
        self.color = color
        self.ship_speed = 1.5
        self.bg_color = color
        self.ship_limit = 3
        #bullet
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        #Aliens
        self.alien_speed = .25
        self.fleet_direction = -1
        self.fleet_drop_speed = 10

