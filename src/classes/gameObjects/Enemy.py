from abc import abstractmethod
from src.pplay.sprite import Sprite
from src.helpers.math import distance
from src.classes.utils.ObjectRect import ObjectRect
from src.classes.utils.Vector import Vector

class Enemy():
    def __init__(self, wave):
        self.speed: Vector

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

    @property
    def width(self):
        return self.gameObject.width

    @property
    def height(self):
        return self.gameObject.height


    def distanceTo(self, gameObject):
        return distance(self, gameObject)

    """ 
    Verifica se o inimigo está colidindo com uma das
    bordas da janela. Também pode ser usado para
    verificar se o objeto está fora da tela.
    """
    def isInWindowEdge(self):
        window = self.wave.window
        rect = self.getRect()

        return (
            rect.top <= 5 or
            rect.right >= window.width - 5 or
            rect.bottom >= window.height - 5 or
            rect.left <= 5
        )

    def willBeInWindownEdge(self):
        window = self.wave.window

        nextPosition = (
            self.x + self.speed.x * window.delta_time(),
            self.y + self.speed.y * window.delta_time()
        )

        return (
            nextPosition[0] <= 5 or
            nextPosition[1] <= 5 or
            nextPosition[0] + self.width >= window.width - 5 or
            nextPosition[1] + self.height >= window.height - 5
        )

    """
    Realiza todos os procedimentos para esconder o sprite
    e chama o destroyEnemy da wave em que está.
    """

    def getRect(self):
        return ObjectRect(self.gameObject)

    def destroy(self):
        # Todo o algorítimo para tirar o inimigo da tela
        # e esconder.
        self.wave.destroyEnemy(self)

    def loop(self):
        if (self.gameObject is None):
            return
