from abc import abstractmethod
from src.helpers.math import distance
from src.classes.utils.ObjectRect import ObjectRect
from src.pplay.gameobject import GameObject

""" Esta classe é uma interface de GameObject
com métodos e propriedades comuns aos GameObjects. """
class GameObjectInterface():
    def __init__(self):
        self.gameObject: GameObject

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

    """
    Realiza todos os procedimentos para esconder o sprite
    e chama o destroyEnemy da wave em que está.
    """
    def getRect(self):
        return ObjectRect(self.gameObject)

    @abstractmethod
    def destroy(self): pass

    def loop(self):
        if (self.gameObject is None):
            return