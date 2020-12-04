import terminalService
import helpers
import socket

from _thread import start_new_thread
import threading

import signal
from functools import partial

from dotenv import load_dotenv
import os


def threaded(c):
    while True:
        command = c.recv(1024)
        print(command)
        if not command:
            break

        output = terminalService.send_command(command)
        c.send(output)

    c.close()


def Main():
    load_dotenv(verbose=True)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((os.getenv("SERVER_IP"), int(os.getenv("SERVER_PORT"))))
    print("socket binded to port", os.getenv("SERVER_PORT"))

    signal.signal(signal.SIGINT, partial(helpers.signal_handler, s))

    s.listen(5)
    print("Command Server Started! Socket is listening...")

    while True:
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])

        c.send(terminalService.send_command(helpers.message_encoder("pwd")))
        start_new_thread(threaded, (c,))

    s.close()


if __name__ == '__main__':
    Main()
