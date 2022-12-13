from pybricks.parameters import Port
from String import String

# NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]
class Body:
    def __init__(self):
        #self.b1 = String(0,Port.S1,"C4/4")
        #self.b2 = String(0,Port.S2,"G4/4")
        #self.b3 = String(0,Port.S3,"C4/4")
        #self.buttons = [self.b1, self.b2, self.b3]
        
        self.b1 = String(0, Port.S1, 1318)
        self.b2 = String(0, Port.S2, 659)
        
        self.buttons = [self.b1, self.b2]
    
    def anyPressed(self):
        any([button.isPressed() for button in self.buttons])
        
    def getPressed(self):
        pressed = []
        for button in self.buttons:
            if button.isPressed():
                pressed.append(button)
        return pressed