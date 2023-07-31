import sys
from pyaudio import *

class Audio:
    def __init__(self):
        self.CHUNK = 1024
        FORMAT = paInt16
        CHANNELS = 1 if sys.platform == 'darwin' else 2
        RATE = 48000

        p = PyAudio()

        self.inputStream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True)

        self.outputStream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, output = True)
    
    def readAudioBytes(self):
        return self.inputStream.read(self.CHUNK)
    
    def playAudioBytes(self, data):
        self.outputStream.write(data)