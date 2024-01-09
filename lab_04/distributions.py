import numpy.random as nprand
from abc import ABC, abstractmethod
from math import exp
from random import random

class Distribution(ABC):
    @abstractmethod
    def generate(self):
        pass


class Uniform(Distribution):

    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)


    def generate(self):
        return nprand.uniform(self.a, self.b)


class Poisson(Distribution):

    def __init__(self, lam):
        self.lam = lam


    def generate(self):
        return nprand.poisson(self.lam)

class Uniform2(Distribution):

    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)


    def generate(self):
        R = random()
        return self.a + (self.b - self.a) * R

class Poisson2(Distribution):

    def __init__(self, lam):
        self.lam = lam


    def generate(self):
        l = exp(-self.lam)
        p = 1
        k = 0
        while True:
            k += 1
            p *= random()
            if p < l:
                break
        return k - 1

if __name__ == "__main__":
    uniform = Uniform(0, 10)
    print(uniform.generate())

    uniform = Uniform2(0, 10)
    print(uniform.generate())

    poisson = Poisson(1)
    print(poisson.generate())

    poisson = Poisson2(1)
    print(poisson.generate())