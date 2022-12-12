from pybricks.parameters import Port, Button, Color
from Neck import Neck
from Body import Body

class Guitar:
    def __init__(self, ev3):
        self.speaker = Speaker(ev3)
        #self.neck = Neck()
        #self.body = Body()
        
    def start(self):
        while button.CENTER not in buttons.pressed():
            self.speaker.play('C4/4') #'C4/4', 'G4/4'

class Speaker:
    def __init__(self, ev3):
        self.ev3 = ev3
        self.TEMPO = 120
        
    def play(self, chord):
        self.ev3.speaker.play_notes([chord], tempo=self.TEMPO)
        