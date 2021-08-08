from math import sqrt


def quad(a, b, c):
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2

def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug():
    x = -100  # start at -100
    while x < 100:
        if g(x) == 0:
            return x
        x += 1


def equation(a, b, c, d):
    '''solves equations of the form ax + b = cx + d = 0'''
    return (d-b) / (a-c)


print(plug())
print(equation(1, 2, 3, 4))
x = equation(12, 18, -34, 67)
print(12*x + 18)
print(-34*x + 67)
print(equation((1/2), (2/3), (1/5), (7/8)))
print(quad(2, 7, -15))

