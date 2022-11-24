def distance(gameObjectA, gameObjectB):
    distance_x = (gameObjectB.x - gameObjectA.x) ** 2
    distance_y = (gameObjectB.y - gameObjectA.y) ** 2
    return (distance_x + distance_y) ** 0.5