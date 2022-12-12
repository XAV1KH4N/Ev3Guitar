from pybricks.parameters import Port
from String import String

class Body:
    def __init__(self):
        self.b1 = String(0,Port.S1,"C4/4")
        self.b2 = String(0,Port.S2,"C4/4")
        self.b3 = String(0,Port.S3,"C4/4")
        self.buttons[self.b1, self.b2, self.b3]
    
    def anyPressed(self):
        any([button.isPressed() for button in self.buttons])