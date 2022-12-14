def distance(gameObjectA, gameObjectB):
    distance_x = (gameObjectB.x - gameObjectA.x) ** 2
    distance_y = (gameObjectB.y - gameObjectA.y) ** 2
    return (distance_x + distance_y) ** 0.5

def distanceCenter(gameObjectA, gameObjectB):
    xa, ya = gameObjectA.getRect().center
    xb, yb = gameObjectB.getRect().center

    distance_x = (xb - xa) ** 2
    distance_y = (yb - ya) ** 2
    return (distance_x + distance_y) ** 0.5