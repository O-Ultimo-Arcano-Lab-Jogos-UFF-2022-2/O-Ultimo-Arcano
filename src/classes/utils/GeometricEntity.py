class GeometricEntity():
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int | float):
        return self.__class__(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int | float):
        return self.__class__(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'