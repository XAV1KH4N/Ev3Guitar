from pybricks.ev3devices import ColorSensor, TouchSensor
from pybricks.parameters import Port

class String: # 0 = touch button, 1 = colour sensor
    def __init__(self, input_type, port, chord):
        if input_type == 0:
            self.sensor = TSensor(port)
            
        elif input_type == 1:
            self.sensor = CSensor(port)
        
        self.chord = chord
        
    def isPressed(self):
        return self.sensor.isPressed()
    
    def getChord(self):
        return self.chord

class Sensor:
    pass

class TSensor(Sensor):
    def __init__(self, port):
        self.touchSensor = TouchSensor(port)
    
    def isPressed(self):
        return self.touchSensor.pressed()
    
class CSensor(Sensor):
    def __init__(self, port):
        self.colourSensor = ColorSensor(port)
    
    def isPressed(self):
        return False
