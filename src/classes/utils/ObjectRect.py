from src.pplay.gameobject import GameObject

class ObjectRect:
    def __init__(self, obj: GameObject):
        self.left = obj.x
        self.top = obj.y
        self.right = obj.x + obj.width
        self.bottom = obj.y + obj.height
        self.center = [ 
            obj.x + obj.width / 2,
            obj.y + obj.height / 2 
        ]
    
    # Util caso seja necessário printar
    def to_dict(self):
        return {
            'left': self.left,
            'right': self.right,
            'top': self.top,
            'bottom': self.bottom,
            'center': self.center
        }
        