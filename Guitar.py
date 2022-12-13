from pybricks.parameters import Port, Button, Color
from Neck import Neck
from Body import Body

class Guitar:
    def __init__(self, ev3):
        self.ev3 = ev3
        #self.neck = Neck()
        self.tempo = 200
        VOLUME = 25
        self.ev3.speaker.set_volume(VOLUME)
        self.body = Body()
        
    def start(self):
        while Button.CENTER not in self.ev3.buttons.pressed():
            pressed = self.body.getPressed()
            if pressed != []:
                self.play_freq(pressed[0].getChord())
    
    def play_note(self, chord):
        self.ev3.speaker.play_notes([chord], tempo=self.tempo)
    
    def play_freq(self, freq):
        self.ev3.speaker.beep(freq)        