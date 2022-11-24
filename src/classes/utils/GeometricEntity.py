""" Esta classe representa uma entidade geométrica
genérica. Pode ser extendida por outras classes, como
os vetores e os pontos. """
class GeometricEntity():
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    """ Implementa soma de coordenadas """
    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    """ Implementa subtração de coordenadas """
    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    """ Implementa multplicação coordenada * escalar """
    def __mul__(self, scalar: int | float):
        return self.__class__(self.x * scalar, self.y * scalar)

    """ Implementa divisão coordenada / escalar """
    def __truediv__(self, scalar: int | float):
        return self.__class__(self.x / scalar, self.y / scalar)

    """ Formata bonitinho o print de entidades geométricas. """
    def __str__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'