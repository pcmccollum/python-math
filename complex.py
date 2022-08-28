from math import sqrt


def cAdd(a, b):
    '''adds two complex numbers'''
    return [a[0]+b[0], a[1]+b[1]]


def cMult(u, v):
    '''multiplies two complex numbers'''
    return [u[0]*v[0] - u[1]*v[1], u[1]*v[0] + u[0]*v[1]]


def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
