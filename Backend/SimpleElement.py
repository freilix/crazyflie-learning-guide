from Backend import Element
from cflib.crazyflie import Crazyflie

@Element.register
class SimpleElement(Element):
    def run(self, crazyflie):
        cf = crazyflie
        cf.commander.send_setpoint()