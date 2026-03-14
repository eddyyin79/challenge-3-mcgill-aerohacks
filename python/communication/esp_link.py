import socket
from python.utils.config import *

class ESPLink:

    def __init__(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((DRONE_IP, DRONE_PORT))

    def send_command(self, roll, pitch, throttle):

        msg = f"{roll},{pitch},{throttle}\n"

        self.sock.send(msg.encode())