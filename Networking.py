from socket import *
import threading
from Printer import *

class Networking:
    def __init__(self, ip, hostPort, targetPort):
        self.ip = ip
        self.hostPort = hostPort
        self.targetPort = targetPort

        self.onDataRecived = lambda data : None

        self.running = True

    def start(self):
        print("Punching hole")

        sock = socket(AF_INET, SOCK_DGRAM)

        try:
            sock.bind(("0.0.0.0", self.hostPort))
        except error as e:
            print("Failed to bind port, Error:\n", e)

        sock.sendto(b'0', (self.ip, self.targetPort))

        print('ready to exchange messages\n')

        listenThread = threading.Thread(target = self.listen, daemon = True)
        listenThread.start()

        self.UDPSocket = socket(AF_INET, SOCK_DGRAM)
        self.UDPSocket.bind(("0.0.0.0", self.targetPort))

    def listen(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(('0.0.0.0', self.hostPort))
        while self.running:
            try:
                data = sock.recv(1024)
                print('\rpeer: {}\n> '.format(data.decode()), end='')
                self.onDataRecived(data)
            except error as e:
                
                continue

    def sendData(self, data):
        try:
            self.UDPSocket.sendto(data, (self.ip, self.hostPort))
        except error as e:
            print("Failed to send data, Error:\n", e)

    def stop(self):
        self.UDPSocket.close()
        self.running = False
