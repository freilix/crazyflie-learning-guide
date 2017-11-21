import abc
from cflib.crazyflie import Crazyflie
from cflib.crazyflie import Commander

class Element():
    def __init__(self, crazyflie):
        self.cf = crazyflie

    @abc.abstractmethod
    def run(self, crazyflie):
        raise NotImplementedError("abstract method")
        return