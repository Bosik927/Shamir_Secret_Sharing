from random import *

from scipy.interpolate import lagrange


class Shamir:

    def __init__(self, secret, k, parts):
        self.secret = secret

        self.parts = parts
        self.numbers = []
        self.dict = {}
        self.k = k

        self.numbers.append(secret)

        for i in range(0, self.k - 1):
            self.numbers.append(randint(1, self.secret))

        self.calcparts()

        self.poly = self.lagra()

    def calcparts(self):
        for part in range(0, self.parts):
            sum = 0
            for i in range(0, len(self.numbers)):
                sum += part ** i * self.numbers[i]
            self.dict[part] = sum

    def lagra(self):
        xcoords = []
        ycoords = []
        for i in range(1, self.k+1):
            xcoords.append(i)
            ycoords.append(self.dict[i])
        return lagrange(xcoords, ycoords)

    def deshamir(self):
        return self.poly[0]


    def points(self):
        for i in s.dict:
            print(str(i) + " " + str(s.dict[i]))



secret = 160
k = 3
parts = 6

s = Shamir(secret, k, parts)
print("Calculation of Shamir Secret with:")
print("secret=" + str(secret))
print("k=" + str(k))
print("number of parts=" + str(parts))
print()

print("Parts:")
s.points()
print()

print("Polynomial:")
print(s.poly)
print()

print("Secret:")
print(int(s.deshamir()))
