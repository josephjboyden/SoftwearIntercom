import threading

class Printer:
    def __init__(self):
        self.lock = threading.Lock()

    def print(message):
        with self.lock:
            print(message)