from src.classes.utils.GeometricEntity import GeometricEntity

class Vector(GeometricEntity):

    def __init__(self, x, y):
        super().__init__(x, y)

    # Retorna a norma do vetor. 
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Retorna a versão unitária deste vetor. Isso pode ser
    # usado para gerar um vetor que da a direção
    # da velocidade.
    def unit(self):
        return self / self.norm()


    def setDirection(self, unitVector):
        if (unitVector.norm() != 1):
            unitVector = unitVector.unit()
        
        self.x = unitVector.x
        self.y = unitVector.y

    # Cria um vetor que vai de objectA para
    # objectB.
    def fromObjects(objectA, objectB):
        return Vector(objectB.x - objectA.x, objectB.y - objectA.y)

    def copy(vector):
        return Vector(vector.x, vector.y)
        