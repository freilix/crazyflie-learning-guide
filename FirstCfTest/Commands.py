from cflib.crazyflie import Crazyflie
currentPosition = (0, 0, 0)

class Commands():
    def __init__(self, pCrazyflie, x, y, z):
        self.crazyflie = pCrazyflie
        currentPosition[0] = x;
        currentPosition[1] = y;
        currentPosition[2] = z;

    def goToPoints(x,y,z):
        currentPosition[0] = x;
        currentPosition[1] = y;
        currentPosition[2] = z;
    def increaseX(x):
        currentPosition[0] += x
    def increaseY(y):
        currentPosition[1] += y
    def increaseY(z):
        currentPosition[2] += z
