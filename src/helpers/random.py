def randomNumber(minVal: int | float, maxVal: int | float):
    from random import random

    if (minVal > maxVal):
        minVal, maxVal = maxVal, minVal

    return (random() * (maxVal - minVal)) + minVal