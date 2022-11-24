from src.classes.utils.GeometricEntity import GeometricEntity
from math import acos, degrees

class Vector(GeometricEntity):

    def __init__(self, x, y):
        super().__init__(x, y)

    """ Retorna a norma do vetor. """ 
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    """ Retorna a versão unitária deste vetor. Isso pode ser
    usado para gerar um vetor que da a direção
    da velocidade. """
    def unit(self):
        return self / self.norm()

    """ Trocar a direção do vetor para a mesma do que um
    outro vetor. """
    def setDirection(self, unitVector):
        if (unitVector.norm() != 1):
            unitVector = unitVector.unit()
        
        self.x *= unitVector.x
        self.y *= unitVector.y
        return self

    """ Copia a direção de um outro vetor sem alterar
    a instância. """
    def copyDirection(self, unitVector):
        copy = Vector.copy(self)
        copy.setDirection(unitVector)
        return copy

    """ Retorna o produto interno entre este vetor e
    um outro vetor. """
    def dotProduct(self, vector):
        return self.x * vector.x + self.y * vector.y

    """ Retorna o ângulo entre este e um outro vetor. """
    def angleBetween(self, vector):
        if (vector.norm() == 0):
            return 0

        cos = self.dotProduct(vector) / self.norm() * vector.norm()
        return degrees(acos(cos))
        
        
    """
    STATIC    
    """

    """ Cria um vetor que vai de objectA para
    objectB. """
    def fromObjects(objectA, objectB):
        return Vector(objectB.x - objectA.x, objectB.y - objectA.y)

    """ Faz uma cópia do vetor. """
    def copy(vector):
        return Vector(vector.x, vector.y)
        