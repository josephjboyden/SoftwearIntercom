from Audio import Audio
from Networking import *
from TkinterApp import TkinterApp
from Printer import *
import threading

audio = Audio()

def onDataRecived(data):
    print(data.decode("utf-8"))

def audioLoop(ip, hostPort, targetPort, networking):
    pass

def onConectButtonPressed(ip, hostPort, targetPort):
    networking = Networking(ip, hostPort, targetPort)
    networking.onDataRecived = onDataRecived
    networking.start()
    networking.sendData("Hello".encode("utf-8"))
        
closed = False
app = TkinterApp()

app.onConectButtonPressed = onConectButtonPressed

app.mainloop()
closed = True