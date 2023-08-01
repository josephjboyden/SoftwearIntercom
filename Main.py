from Audio import Audio
from Networking import *
import sys
from TkinterApp import TkinterApp

networking = None
def onHostClicked(port):
    networking = Server(port)

def onConnectClicked(ip, port):
    networking = Client(ip, port)

app = TkinterApp()

app.onConnectClicked = onConnectClicked
app.onHostClicked = onHostClicked

app.mainloop()