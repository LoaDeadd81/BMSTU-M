import numpy.random as nprand
from abc import ABC, abstractmethod

class Distribution(ABC):
    @abstractmethod
    def Generate(self):
        pass


class Uniform(Distribution):

    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)

    def Generate(self):
        return nprand.uniform(self.a, self.b)