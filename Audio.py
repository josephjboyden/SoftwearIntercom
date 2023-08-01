import sys
from pyaudio import *

class Audio:
    
    CHUNK = 1024
    FORMAT = paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 48000

    def __init__(self):

        p = PyAudio()

        self.inputStream = p.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.RATE, input = True)

        self.outputStream = p.open(format = self.FORMAT, channels =self. CHANNELS, rate = self.RATE, output = True)
    
    def readAudioBytes(self):
        return self.inputStream.read(self.CHUNK)
    
    def playAudioBytes(self, data):
        self.outputStream.write(data)