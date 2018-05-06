# -*- coding:utf-8 -*-

#
import time
from parking_simulation import SocketClient
def main(port):
    running = True
    while running:
        time.sleep(1)
        client = SocketClient(port=port)
        try:
            print(client.get_data().decode())
        except:
            running = False
            print("connection lost")

if __name__ == "__main__":
    with open("port.txt") as file:
        port = int(file.read())
    main(port)
