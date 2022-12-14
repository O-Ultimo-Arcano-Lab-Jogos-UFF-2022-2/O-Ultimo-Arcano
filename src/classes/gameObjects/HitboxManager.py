from src.pplay.window import Window

class HitboxManager():
    hitboxes = []
    window: Window

    @classmethod
    def add(cls, hitbox):
        cls.hitboxes.append(hitbox)
    
    @classmethod
    def remove(cls, hitbox):
        cls.hitboxes = [ h for h in cls.hitboxes if h != hitbox ] 

    @classmethod
    def loop(cls):
        for hitbox in cls.hitboxes:
            hitbox.loop()

    @classmethod
    def draw(cls):
        for hitbox in cls.hitboxes:
            hitbox.draw()

        