from pybricks.ev3devices import InfraredSensor
from pybricks.parameters import Port

class Neck:
    def __init__(self):
        self.sensor = InfraredSensor(Port.S4)
    
    def getDistance(self):
        return self.sensor.distance()