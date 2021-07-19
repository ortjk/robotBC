import socket
import json

DEFAULT_IP_ADDRESS = "127.0.0.1"
DEFAULT_PORT = 33355

#TODO: Extract logic from methods and put them into external functions.

class TCPRobotController():
    def __init__(self, ip = DEFAULT_IP_ADDRESS, port = DEFAULT_PORT, socket_args = list(), socket_kwargs = dict()):
        self.ip = ip
        self.port = port

    def connect(self, ip = None, port = None):
        ip = self.ip if ip is None else ip
        port = self.port if port is None else port
        self.conn = socket.create_connection((ip, port))

    def forward(self, y):
        self.send_command_dictionary({
            "command_type": "move",
            "x": 0,
            "y": -y
        })

    def backward(self, y):
        self.send_command_dictionary({
            "command_type": "move",
            "x": 0,
            "y": y
        })

    def left(self, x):
        self.send_command_dictionary({
            "command_type": "move",
            "x": -x,
            "y": 0
        })

    def right(self, x):
        self.send_command_dictionary({
            "command_type": "move",
            "x": x,
            "y": 0
        })

    def rotate_clockwise(self, degrees):
        self.send_command_dictionary({
            "command_type": "rotate",
            "degrees": degrees,
            "rotate_direction": "clockwise"
        })

    def rotate_counterclockwise(self, degrees):
        self.send_command_dictionary({
            "command_type": "rotate",
            "degrees": degrees,
            "rotate_direction": "counterclockwise"
        })

    def scan_for_people(self):
        return self.send_command_dictionary({"command_type":"scan_people"})['response_args'][0]

    def scan_for_fire(self):
        return self.send_command_dictionary({"command_type":"scan_fire"})['response_args'][0]

    #def scan_for_marker(self):
    #    return self.send_command_dictionary({"command_type":"scan_marker"})['response_args'][0]

    def extinguish_fire(self):
        return self.send_command_dictionary({"command_type":"extinguish_fire"})['response_args'][0]

    def rescue_person(self):
        return self.send_command_dictionary({"command_type":"rescue_person"})['response_args'][0]

    def take_temperature(self):
        return self.send_command_dictionary({"command_type":"take_temperature"})['response_args'][0]

    def read_marker(self):
        return self.send_command_dictionary({"command_type":"read_marker"})['response_args'][0]

    def send_command_dictionary(self, command_dict):
        return send_command_dictionary_over_tcp_socket(self.conn, command_dict)

    def disconnect(self):
        self.conn.shutdown()
        self.conn.close()

def send_command_dictionary_over_tcp_socket(conn, command_dictionary):
    conn.send(json.dumps(command_dictionary).encode('utf-8'))
    resp = b''
    while "response_type" not in resp.decode('utf-8'):
        resp = conn.recv(4096)
    return json.loads(resp.decode('utf-8'))

#Export:
RobotController = TCPRobotController