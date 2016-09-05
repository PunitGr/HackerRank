#!/usr/local/bin/python3
import math


class Points(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __sub__(self, number):
        a = self.a - number.a
        b = self.b - number.b
        c = self.c - number.c
        return (Points(a, b, c))

    def dot(self, number):
        a = self.a * number.a
        b = self.b * number.b
        c = self.c * number.c
        return (a + b + c)

    def cross(self, number):
        a = self.b * number.c - self.c * number.b
        b = self.c * number.a - self.a * number.c
        c = self.a * number.b - self.b * number.a
        return Points(a, b, c)

    def absolute_scale(self):
        return (pow((self.a ** 2 + self.b ** 2 + self.c ** 2), .5))


def solve(A, B, C, D):
    A, B, C, D = Points(*A), Points(*B), Points(*C), Points(*D)
    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    angle = math.acos(X.dot(Y) / (X.absolute_scale() * Y.absolute_scale()))
    print ("%.2f" % math.degrees(angle))

points = list()
for i in range(4):
    a = map(float, input().split())
    points.append(a)
solve(*points)
