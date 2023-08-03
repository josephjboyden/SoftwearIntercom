from tkinter import *

class TkinterApp(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        self.onConectButtonPressed = lambda : None

        ipLabel = Label(self, text = "IP:")
        ipLabel.grid(column = 0, row = 0)

        self.ipEntry = Entry(self)
        self.ipEntry.grid(column = 1, row = 0)
        self.ipEntry.insert(0,"127.0.0.1")

        hostPortLabel = Label(self, text = "Host Port:")
        hostPortLabel.grid(column = 0, row = 1)

        self.hostPortEntry = Entry(self)
        self.hostPortEntry.grid(column = 1, row = 1)
        self.hostPortEntry.insert(0,"5005")

        targetPortLabel = Label(self, text = "Target Port:")
        targetPortLabel.grid(column = 0, row = 2)

        self.targetPortEntry = Entry(self)
        self.targetPortEntry.grid(column = 1, row = 2)
        self.targetPortEntry.insert(0,"5006")

        connectButton = Button(self, text = "Connect", command = self.connectButtonCallback)
        connectButton.grid (column = 0, columnspan = 2, row = 3)

    def connectButtonCallback(self):
        ip = self.ipEntry.get()
        hostPort = int(self.hostPortEntry.get())
        targetPort = int(self.targetPortEntry.get())
        self.onConectButtonPressed(ip, hostPort, targetPort)
