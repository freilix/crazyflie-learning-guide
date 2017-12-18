import abc
from cflib.crazyflie import Crazyflie
from cflib.crazyflie import Commander

class Element(metaclass=abc.ABCMeta):
    def __init__(self):
        self.test = 1

    @abc.abstractmethod
    def run(self, crazyflie):
        raise NotImplementedError("abstract method")
        return