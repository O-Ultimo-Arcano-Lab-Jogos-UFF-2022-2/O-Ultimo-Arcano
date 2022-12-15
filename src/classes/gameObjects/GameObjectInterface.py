from abc import abstractmethod
from src.helpers.math import distance, distanceCenter
from src.classes.utils.ObjectRect import ObjectRect
from src.pplay.gameobject import GameObject
from src.pplay.sprite import Sprite

""" Esta classe é uma interface de GameObject
com métodos e propriedades comuns aos GameObjects. """
class GameObjectInterface():
    def __init__(self):
        self.gameObject: GameObject

        # Essas propriedades para coordenadas
        # são usadas quando não
        self._x: int | float = 0
        self._y: int | float = 0
        self._width: int | float = 0
        self._height: int | float = 0

        

    """
    Setters & Getters:
    - Permitem interagir com o gameObject sem a necessidade
    de acessa-lo diretamente.
    """
    @property
    def x(self):
        if (self.gameObject is None):
            return self._x

        return self.gameObject.x

    @x.setter
    def x(self, value):
        if (self.gameObject is None):
            self._x = value

        self.gameObject.x = value

    @property
    def y(self):
        if (self.gameObject is None):
            return self._y

        return self.gameObject.y

    @y.setter
    def y(self, value):
        if (self.gameObject is None):
            self._y = value
            
        self.gameObject.y = value

    @property
    def width(self):
        if (self.gameObject is None):
            return self._width
            
        return self.gameObject.width


    # Propositalmente não permite que o 
    # sprite seja redimensionado.
    @width.setter
    def width(self, value):
        self._width = value
            
        
    @property
    def height(self):
        if (self.gameObject is None):
            return self._height

        return self.gameObject.height

    @height.setter
    def height(self, value):
        self._height = value


    def distanceTo(self, gameObject, center = False):
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

    def loop(self):
        if (self.gameObject is None):
            return

    def draw(self):
        if (isinstance(self.gameObject, Sprite)):
            self.gameObject.draw()