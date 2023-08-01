from tkinter import *

class TkinterApp(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
         
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  
        for F in (MainMenu, Connect, Host):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.lastFrame = []
  
        frame = self.frames[MainMenu]
        frame.tkraise()
        self.currentFrame = frame

        backButton = Button(container, text = "Back", command = self.backButtonCallback)
        backButton.grid(column = 0, row = 1)

        self.onConnectClicked = lambda ip, port: None
        self.onHostClicked = lambda port: None

    def show_frame(self, cont):
        self.lastFrame.append(type(self.currentFrame))
        frame = self.frames[cont]
        frame.tkraise()
        self.currentFrame = frame
        print(len(self.lastFrame))

    def backButtonCallback(self):
        frame = self.frames[self.lastFrame.pop(-1)]
        frame.tkraise()
        self.currentFrame = frame
        print(len(self.lastFrame))

    def connectButtonCallback(self):
        self.onConnectClicked("0.0.0.0", 1)

    def hostButtonCallback(self):
        self.onHostClicked(1)

class MainMenu(Frame):
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)

        connectButton = Button(self, text = "Connect", command = lambda : controller.show_frame(Connect))
        connectButton.grid(column = 0, row = 0)

        hostButton = Button(self, text = "Host", command = lambda : controller.show_frame(Host))
        hostButton.grid(column = 1, row = 0)

class Connect(Frame):
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)

        ipLabel = Label(self, text = "IP:")
        ipLabel.grid(column = 0, row = 0)

        ipInput = Entry(self)
        ipInput.grid(column = 1, row = 0)

        portLabel = Label(self, text = "Port:")
        portLabel.grid(column = 0, row = 1)

        portInput = Entry(self)
        portInput.grid(column = 1, row = 1)

        connectButton = Button(self, text = "Connect", command = controller.connectButtonCallback)
        connectButton.grid(column = 0, columnspan = 2, row = 2)

class Host(Frame):
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)

        portLabel = Label(self, text = "Port:")
        portLabel.grid(column = 0, row = 0)

        portInput = Entry(self)
        portInput.grid(column = 1, row = 0)

        hostButton = Button(self, text = "Host", command = controller.hostButtonCallback)
        hostButton.grid(column = 0, columnspan = 2, row = 1)

