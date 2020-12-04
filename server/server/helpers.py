import sys


def signal_handler(socket, sig, frame):
    print("\nserver closed!")
    socket.close()
    sys.exit(0)

def message_encoder(message):
    return str(message).encode("utf-8")

def message_decoder(message):
    return message.decode("utf-8")