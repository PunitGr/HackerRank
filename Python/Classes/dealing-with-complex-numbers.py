#!/usr/local/bin/python3
import math


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        a = self.real
        b = self.imag
        c = other.real
        d = other.imag
        return Complex(a * c - b * d,
                       b * c + a * d)

    def __truediv__(self, other):
        a = self.real
        b = self.imag
        c = other.real
        d = other.imag
        return Complex((a * c + b * d) / (c * c + d * d),
                       (b * c - a * d) / (c * c + d * d))

    def mod(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return "{:.2f}{}{:.2f}i".format(self.real,
                                        sign,
                                        abs(self.imag))

(r, i) = map(float, input().split())
C = Complex(r, i)

(r, i) = map(float, input().split())
D = Complex(r, i)

print (C + D)
print (C - D)
print (C * D)
print (C / D)
print ("{:.2f}+0.00i".format(C.mod()))
print ("{:.2f}+0.00i".format(D.mod()))

