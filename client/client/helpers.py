import sys


def signal_handler(socket, sig, frame):
    print("\nconnection closed!")
    socket.close()
    sys.exit(0)


def message_encoder(command, cwd):
    return (command+"&cwd&"+cwd).encode('utf-8')

def message_decoder(server_message):
    return str(server_message.decode('utf-8'))[:-1]


def check_path_exist_error(server_message):
    msg = str(server_message.decode('utf-8')).split("!!!")
    if msg[0] == "ERROR":
        print(msg[1])
        return True
    return False
