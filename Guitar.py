from InputType import InputType

class Guitar:
    def __init__(args):
        self.neck = Neck()
        self.body = Body()
         
class Neck:
    def __init__(self, port):
        self.neck = InfraredSensor(port)
    
    def getDistance(self):
        return self.neck.distance()
    
class Body:
    def __init__(self):
        self.s1 = String(Port.S1, 0.3)
        self.s2 = String(Port.S2, 0.6)
        self.s3 = String(Port.S3, 0.9)
        self.strings[self.b1, self.b2, self.b3]
    
    def run(self):
        pass
    
    def anyPressed(self):
        any([string.isPressed() for string in self.strings])
        
    def getStringFreq(self, string_index):
        string = self.strings[string_index]
        if not string.isPressed():
            return 0
        
        return self.calcNeckFreq(string.getFreq())
    
    def calcNeckFreq(self, freq):
        return freq * self.neck.getDistance()
    
    def calcFreqs(self):
        freqs = [None]*len(strings)
        for i in range(len(strings)):
            freq[i] = self.getstringFreq(i)
        return freq
        