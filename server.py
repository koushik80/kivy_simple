import socket
import threading 

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST,PORT))
server.listen()

def run_server():
    while True:
        client, addr = server.accept()
        print(f"{addr} connected to server..")
        client.send("NICKNAME",encode('utf-8'))
if __name__ == '__main__':
    run_server()
