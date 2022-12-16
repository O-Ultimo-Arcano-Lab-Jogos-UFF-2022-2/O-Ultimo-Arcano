from abc import abstractmethod
from src.helpers.math import distance, distanceCenter
from src.classes.utils.ObjectRect import ObjectRect
from src.pplay.gameobject import GameObject
from src.pplay.sprite import Sprite

""" Esta classe é uma interface de GameObject
com métodos e propriedades comuns aos GameObjects. """


class GameObjectInterface(GameObject):
    def __init__(self):
        self._gameObject: GameObject

        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self.needsToBeDrawn = True

    """
    Setters & Getters:
    - Permitem interagir com o gameObject sem a necessidade
    de acessa-lo diretamente.
    """
    @property
    def gameObject(self):
        return self._gameObject

    @gameObject.setter
    def gameObject(self, obj: GameObject):
        if (obj):
            self.width = obj.width
            self.height = obj.height

        self._gameObject = obj

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

        if (self.gameObject):
            self.gameObject.x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

        if (self.gameObject):
            self.gameObject.y = value

    @property
    def width(self):
        return self._width

    # Propositalmente não permite que o
    # sprite seja redimensionado.
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def distanceTo(self, gameObject, center=False):
        return\
            distance(self, gameObject) \
            if (not center) \
            else distanceCenter(self, gameObject)

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

    @abstractmethod
    def loop(self): pass

    def draw(self):
        if (isinstance(self.gameObject, Sprite) and self.needsToBeDrawn):
            self.gameObject.draw()
