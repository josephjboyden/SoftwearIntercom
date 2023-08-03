import threading
import builtins

lock = threading.Lock()

def print(*args, **kwargs):
    with lock:
        builtins.print(*args, **kwargs)