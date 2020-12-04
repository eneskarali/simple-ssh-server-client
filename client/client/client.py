import helpers
from user import User
import commandService

import socket

import signal
from functools import partial

from dotenv import load_dotenv
import os


def Main():
    load_dotenv(verbose=True)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((os.getenv("SERVER_IP"), int(os.getenv("SERVER_PORT"))))

    signal.signal(signal.SIGINT, partial(helpers.signal_handler, s))

    user_name = input("username: ")
    path = s.recv(1024)
    user = User(path.decode("utf-8")[:-1], user_name)

    while True:
        command = input(user.user_name + ":~" + user.path+"$ ")
        prev_path = user.path

        if not command:
            continue
        elif command == "exit":
            break

        ok, message = commandService.command_checker(user, command)
        if not ok:
            if message:
                print(message)

            s.send(helpers.message_encoder("ls", user.path))
            server_response = s.recv(1024)

            if  helpers.check_path_exist_error(server_response):
                user.path = prev_path

            continue
        
        s.send(helpers.message_encoder(command, user.path))

        server_response = s.recv(1024)
        if  helpers.message_decoder(server_response).strip():
            print(helpers.message_decoder(server_response))

    s.close()


if __name__ == '__main__':
    Main()
