from src.pplay.window import Window

class ProjectileManager():
    projectiles = []
    window: Window
    game = None

    @classmethod
    def add(cls, projectile):
        cls.projectiles.append(projectile)
    
    @classmethod
    def remove(cls, projectile):
        cls.projectiles = [ p for p in cls.projectiles if p != projectile ] 

    @classmethod
    def loop(cls):
        for projectile in cls.projectiles:
            projectile.loop()

    @classmethod
    def draw(cls):
        for projectile in cls.projectiles:
            projectile.draw()

        