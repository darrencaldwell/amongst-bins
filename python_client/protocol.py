import protocol_pb2
import struct
import socket

HOST = "127.0.0.1"
PORT = 8080

# create socket to connect to server
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

# methods to send certain protocol to server?
#   join game
#   movement update

def send_protocol_preface(s, protocol_type, protocol_len, m):
    protocol_type = struct.pack("<I", protocol_type)
    protocol_len = struct.pack("<I", protocol_len)

    s.sendall(protocol_type)
    s.sendall(protocol_len)
    s.sendall(m)

def join_game(s, username):
    # create object
    jg = protocol_pb2.JoinGame()
    jg.username = username
    # serialize and send, sending protocol number and size of message first
    msg = jg.SerializeToString()

    send_protocol_preface(s, 1, jg.ByteSize(), msg)

    # rec protocol number, length then get message
    protocol_rx = s.recv(1)
    protocol_rx = int.from_bytes(protocol_rx, "little")
    if protocol_rx != 2:
        return -1
    # read len of message
    length_rx = s.recv(1)
    length_rx = int.from_bytes(length_rx, "little")
    # read message and parse it
    message = s.recv(length_rx)
    eg = protocol_pb2.EchoJoinGame()
    eg.ParseFromString(message)
    print(eg)

    return eg.player_id

# methods to recieve player locations
def rx_player_pos(s):
    spu = protocol_pb2.ServerPositionUpdate()
    protocol_rx = s.recv(1)
    protocol_rx = int.from_bytes(protocol_rx, "little")
    if protocol_rx != 5:
        return -1
    # read len of message
    length_rx = s.recv(1)
    length_rx = int.from_bytes(length_rx, "little")
    # read message and parse it
    message = s.recv(length_rx)
    return message


def tx_player_pos(s, player_id, x, y):
    # create object
    pp = protocol_pb2.PlayerPosition()
    pp.player_id = player_id
    pp.x = x
    pp.y = y
    # serialize and send, sending protocol number and size of message first
    msg = pp.SerializeToString()

    send_protocol_preface(s, 3, pp.ByteSize(), msg)
