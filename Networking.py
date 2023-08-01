from socket import *
import threading

class Networking:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class Server(Networking):
    def __init__(self, port):
        Networking.__init__(self, "127.0.0.1", port)

class Client(Networking):
    def __init__(self, ip, port):
        Networking.__init__(self, ip, port)