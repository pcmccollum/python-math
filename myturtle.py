from turtle import *
shape('circle')
speed(10)


def turtleSquare(sideLength=100):
    for i in range(4):
        forward(sideLength)
        right(90)


def turtleSquares(sideLength=5):
    for j in range(60):
        for i in range(4):
            forward(sideLength)
            right(90)
        right(5)
        sideLength += 5


def turtleTriangle(sideLength=100):
    for i in range(3):
        forward(sideLength)
        right(120)


def turtlePolygon(sides=5, sideLength=100):
    for i in range(sides):
        forward(sideLength)
        right(360/sides)


def turtleStar(sideLength=100):
    for i in range(5):
        forward(sideLength)
        right(180 - (180/5))


def turtleStars(sideLength=5):
    for j in range(60):
        for i in range(5):
            forward(sideLength)
            right(180 - (180/5))
        right(5)
        sideLength += 5


# turtleStar()
# turtleStars()
turtleSquares()
# turtleSquares()
# turtleTriangle()
# turtlePolygon(10)
