from abc import abstractmethod
from PPlay.sprite import Sprite

class Enemy():

    def __init__(self, wave):
        self.wave = wave
        self.gameObject: Sprite = None
        self.life = 1

    """
    Setters & Getters:
    - Permitem interagir com o gameObject sem a necessidade
    de acessa-lo diretamente.
    """
    @property
    def x(self):
        return self.gameObject.x
    
    @x.setter
    def x(self, value):
        self.gameObject.x = value
    
    @property
    def y(self):
        return self.gameObject.y
    
    @y.setter
    def y(self, value):
        self.gameObject.y = value


    """
    Realiza todos os procedimentos para esconder o sprite
    e chama o destroyEnemy da wave em que está.
    """
    def destroy(self):
        # Todo o algorítimo para tirar o inimigo da tela
        # e esconder.
        self.wave.destroyEnemy(self)

    def loop(self): 
        if (self.gameObject is None):
            return

        